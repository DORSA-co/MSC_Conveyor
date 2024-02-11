import threading
import os
import time

from PySide6.QtCore import QObject, Signal

from Database.Defects_DB import Defect_DB
from Database.DefectFileManager import DefectFileManager
from PageUI.Report_UI import Report_UI
from backend.Utils.Filter import applyFilter
from Constants.Constant import ViewerInfo

class Report_API:

    """Description of the code

    :param
    """

    def __init__(self, ui: Report_UI, db: Defect_DB):
        self.uiHandler = ui
        self.db = db

        self.uiHandler.button_connector('apply', self.apply_filters)
        self.uiHandler.button_connector('delete_all', self.delete_all)
        self.uiHandler.button_connector('reload', self.startup)
        self.uiHandler.table_widget_connector(self.table_event)
        self.uiHandler.deleteProgressDialog.cancel_button_connector(self.cancel_removing_defects)

        self.view_defect_process = None
        self.external_delete_event_func = None

    def startup(self,):
        self.uiHandler.startup()
        self.load_from_database()
        self.apply_filters()

    def endup(self,):
        return True

    
    def load_from_database(self):
        self.defects = self.db.load()

    def apply_filters(self):
        filters = self.uiHandler.get_filters()
        apply_filter = applyFilter(filters)
        filter_results = []
        for defect in self.defects:
            defect_dict = {}
            defect_dict['width'] = (defect['min_width'], defect['max_width'])
            defect_dict['length'] = defect['length']
            defect_dict['depth'] = (defect['min_depth'], defect['max_depth'])
            defect_dict['date'] = defect['date']
            defect_dict['torn'] = True

            res = apply_filter.check_filter(defect_dict)
            if res:
                filter_results.append(defect)

        self.uiHandler.show_filter_results(filter_results)


    def table_event(self, result, action):
        if action == 'delete':
            self.delete_defect(result)
            self.apply_filters()

        elif action == 'view':
            self.view_defect(result)

    def delete_defect(self, result, show_confirm=True):
        if show_confirm:
            response = self.uiHandler.show_confirm_box("Delete Defect",
                                                    "Are you sure you want to delete defect ?",
                                                    buttons=['yes', 'cancel'],
                                                    icon_type='question')
            if response == 'cancel':
                return
        
        self.db.remove_record('defect_id', result['defect_id'])
        defect_file_manager = DefectFileManager(main_path=result['main_path'])
        defect_file_manager.remove(result['defect_id'])
        self.load_from_database()

        if self.external_delete_event_func:
            self.external_delete_event_func(result)
    
    def delete_all(self,):
        defect_records = self.uiHandler.get_selected_defects()

        #check user select any defect or not
        if len(defect_records) == 0:
            self.uiHandler.show_confirm_box(title='Delete Sample', 
                                 message=f'No defects selected',
                                 buttons=['ok'],
                                 icon_type='warning')
            return
        
        response = self.uiHandler.show_confirm_box("Delete Defects",
                                                    "Are you sure you want to delete selected defects ?",
                                                    buttons=['yes', 'cancel'],
                                                    icon_type='question')
        if response == 'cancel':
            return
        

        self.uiHandler.deleteProgressDialog.show_win()
        self.remove_worker = removeDefectsWorker( defect_records, 
                                                  self.db,
                                                  )
        
        self.thread_remove = threading.Thread(target=self.remove_worker.run)

        self.remove_worker.finished.connect(self.uiHandler.deleteProgressDialog.close_win)
        self.remove_worker.finished.connect(self.load_from_database)
        self.remove_worker.finished.connect(self.apply_filters)
        self.remove_worker.sample_remove.connect(self.external_delete_event_func)
        self.remove_worker.progressBar.connect(self.uiHandler.deleteProgressDialog.set_delete_progress_value)
        self.thread_remove.start()

    def cancel_removing_defects(self,):
        self.remove_worker.pause(True)
        res = self.uiHandler.deleteProgressDialog.show_confirm_massage( title='Cancel Removing',
                                                                text= 'Are you sure cancel the progress?',
                                                                buttons=['yes','no'],
                                                                icon_type='question'
        )
        if res == 'yes':
            self.remove_worker.stop()
        else:
            self.remove_worker.pause(False)
        
    def view_defect(self, result):
        if not self.view_defect_process or self.view_defect_process.poll() is not None:
            # self.view_defect_process = subprocess.Popen(
            #                 [ViewerInfo.PYTHON_COMMAND, ViewerInfo.FILE_PATH, str(result['defect_id'])]
            #                 )
            th = threading.Thread(target=self.run_viewer_app, args=(result,))
            th.start()

    def run_viewer_app(self, result):
            if os.name == 'nt':
                os.system(f"python {ViewerInfo.FILE_PATH} --defect_id={result['defect_id']} --path=\"{os.getcwd()}\"")
            else:
                os.system(f"/bin/python3.9 {ViewerInfo.FILE_PATH} --defect_id={result['defect_id']} --path=\"{os.getcwd()}\"")

    def set_external_delete_event_function(self, func):
        self.external_delete_event_func = func


    










#-------------------------------------------------------------------------------------
#                                    Remove worker
#-------------------------------------------------------------------------------------
class removeDefectsWorker(QObject):
    progressBar = Signal(int, int)
    finished = Signal()
    sample_remove = Signal(dict)

    def __init__(self, defects:list[dict], db:Defect_DB) -> None:
        super(removeDefectsWorker, self).__init__()

        self.defects = defects
        self.db = db
        self.pause_flag = False
        self.stop_flag = False

    def remove_record(self, defect:dict):
        self.db.remove_record('defect_id', defect['defect_id'])
        defect_file_manager = DefectFileManager(main_path=defect['main_path'])
        defect_file_manager.remove(defect['defect_id'])

    def pause(self, status):
        self.pause_flag = status

    def stop(self,):
        self.stop_flag = True

    def run(self,):
        total_count = len(self.defects)

        complete_i = 0
        i = 0
        while complete_i < total_count:
            #stop and paus on last defect make problem on signals
            #so we only accept stop and pault until total_count-1
            if self.stop_flag:
                break
            if self.pause_flag:
                time.sleep(0.02)
                continue
            try:
                defect = self.defects.pop(i)
                self.remove_record(defect)
                complete_i+=1
                self.progressBar.emit(complete_i, total_count)
                self.sample_remove.emit(defect)
                    
            except Exception as e:
                print(e)
                i+=1

            #delay for help to user to cancel soon
            time.sleep(0.2)

        print('remove finished')
        self.finished.emit()
#-------------------------------------------------------------------------------------
#                                    Remove worker
#-------------------------------------------------------------------------------------