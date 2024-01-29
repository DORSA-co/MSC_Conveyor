import cv2

from Database.Defects_DB import Defect_DB
from Database.DefectFileManager import DefectFileManager
from PageUI.Report_UI import Report_UI
from backend.Utils.Filter import applyFilter

class Report_API:

    """Description of the code

    :param
    """

    def __init__(self, ui: Report_UI, db: Defect_DB):
        self.uiHandler = ui
        self.db = db

        self.uiHandler.button_connector('apply', self.apply_filters)
        self.uiHandler.table_widget_connector(self.table_event)

        self.external_delete_event_func = None

    def startup(self,):
        self.uiHandler.startup()
        self.load_from_database()
        self.uiHandler.show_filter_results(self.defects)

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

            res = apply_filter.check_filter(defect_dict)
            if res:
                filter_results.append(defect)

        self.uiHandler.show_filter_results(filter_results)


    def table_event(self, result, action):
        if action == 'delete':
            self.db.remove_record('defect_id', result['defect_id'])
            defect_file_manager = DefectFileManager(main_path=result['main_path'])
            defect_file_manager.remove(result['defect_id'])
            self.load_from_database()
            self.apply_filters()

            if self.external_delete_event_func:
                self.external_delete_event_func(result)

    def set_external_delete_event_function(self, func):
        self.external_delete_event_func = func
