import time
import threading
import os
import psutil

import numpy as np
from PySide6.QtCore import Signal, QObject
from pympler.asizeof import asizeof
from memory_profiler import profile
import tracemalloc


from PageAPI.Setting_API import SettingAPI
from PageAPI.AlgorithmCalibration_API import AlgorithmCalibration_API
from PageAPI.usersPageAPI import usersPageAPI
from PageAPI.LiveView_API import LiveView_API
from PageAPI.Report_API import Report_API
from Database.mainDatabase import mainDatabase
from backend.Camera.dorsaPylon import Collector, Camera
from backend.Camera.cameraThread import cameraWorker, DeviceCheckerWorker
from backend.Camera import dorsaPylon
from main_UI import mainUI
from uiUtils.GUIComponents import timerBuilder
from Detection.beltInspection import beltInspection
from Detection.Defect import Defect
from Constants import Constant
from Database.DefectFileManager import DefectFileManager


CAMERAS = {
     'name': 'main',
     'serial_number':'24555048'
}

class main_API:

    """
    Description of the code

    """
    DEBUG_PROCESS_THREAD = False
    DEBUG_CAMERA_CHECKER_THREAD = False
    DEVICE_CHECKer_TIMER = 5000
    CAMERA_SIMULATION = True
    REFRESH_RATE = 20
    
    
    def __init__(self, uiHandeler:mainUI) -> None:

        self.uiHandeler = uiHandeler
        self.db = mainDatabase()

        #--------------------------------------------------------
        kwargs = self.db.Setting_DB.algorithm_setting_db.load()
        self.beltIncpetcion = beltInspection(kwargs)
        self.beltIncpetcion.new_defect.connect(self.new_defect_event)
        self.beltIncpetcion.update_defect.connect(self.update_defect_event)
        self.beltIncpetcion.processing_finished.connect(self.processing_finished_event)


        self.DefectFileManager = DefectFileManager(Constant.SavePathes.DEFECTS_SAVE_PATH)
        #--------------------------------------------------------
        

        self.cameras: dict[str, Camera] = {}
        self.camera_workers:dict[str, cameraWorker] = {}
        self.camera_threads:dict[str, threading.Thread]= {}
        self.collector = Collector()
        
        self.checked_device_time = time.time()
        self.is_during_checking_device  = False
        self.is_during_process = False
        
        self.test_timer = time.time()
        self.fps = 0
        self.refresh_time = time.time()
        self.device_checker_timer = timerBuilder(self.DEVICE_CHECKer_TIMER, self.check_camera_devices_event)
        self.device_checker_timer.start()
        
        
        self.build_camera(CAMERAS)
        self.run_camera_thread(CAMERAS['name'])

        #self.cameras[CAMERAS['name']].Operations.start_grabbing()
        
        
        self.API_Page_Setting = SettingAPI( self.uiHandeler.Page_Setting, 
                                            self.cameras, 
                                            self.db.Setting_DB,
                                            self.beltIncpetcion )
        
        self.API_Page_Users = usersPageAPI(self.uiHandeler.Page_Users,
                                           self.db.Users_DB)
        
        self.API_Live_View = LiveView_API(self.uiHandeler.Page_LiveView,
                                          self.db,
                                          self.beltIncpetcion)
        
        self.API_Report = Report_API(self.uiHandeler.Page_Report,
                                     self.db.Defects_DB)
        

        self.uiHandeler.change_page_connector(self.page_change_event)
        self.API_Page_Users.set_login_event(self.login_user_event)
        self.API_Report.set_external_delete_event_function(self.delete_defect)
        self.API_Live_View.set_run_stop_event( self.run_stop_event)

        
        self.pages_api_dict = {
            'settings': self.API_Page_Setting,
            'users': self.API_Page_Users,
            'reports': self.API_Report,
        }

        self.login_user_event()
        self.API_Page_Users.loginUser.uiHandeler.loginDialog.show_win()
        self.startup()
        
    @staticmethod
    def print_memory_usage():
        process = psutil.Process(os.getpid())
        memory_usage = process.memory_info().rss # in bytes 
        print(f"Memory Usage: {memory_usage / 1024**2:.2f} MB")

    def startup(self,):
        for api in self.pages_api_dict.values():
            api.startup()

    def set_access(self, role):
        self.uiHandeler.set_access_pages( Constant.User.ACCESS[role]['pages'],)
        self.uiHandeler.set_access_tabs( Constant.User.ACCESS[role]['tabs'])


    def page_change_event(self,prev_page, new_page ):
        if self.pages_api_dict.get(prev_page):
            permision = self.pages_api_dict[prev_page].endup()
        else:
            permision = True

        if permision:
            if self.pages_api_dict.get(new_page):
                self.pages_api_dict[new_page].startup()

        
    def login_user_event(self,):
        role = self.API_Page_Users.data_passer.get_logined_user_role()
        password = self.API_Page_Users.data_passer.get_logined_user_password()
        username = self.API_Page_Users.data_passer.get_logined_user_username()
        self.set_access(role)
        self.API_Live_View.set_logined_user(username, password)
        #self.mainPageAPI.set_logined_user(username)
        #self.reportsPageAPI.set_user_login(username)

    #@profile
    def grabbed_image_event(self, image):
        # print('process time', time.time() - self.test_timer)
        # self.test_timer = time.time()
        
        
        if not self.is_during_process:
            self.is_during_process = True
            self.image = image
            
            if self.API_Live_View.is_running:
                self.fps += 1
                if (time.time() - self.test_timer) >= 1:
                    print('FPS: ', self.fps, time.time() - self.test_timer)
                    self.print_memory_usage()
                    self.test_timer = time.time()
                    self.fps = 0


                if not self.DEBUG_PROCESS_THREAD:
                    self.belt_inspection_thread = threading.Thread(target=self.beltIncpetcion.feed, args=(image,))  
                    self.belt_inspection_thread.start()
                
                else:
                    self.beltIncpetcion.feed(image)


    #@profile
    def processing_finished_event(self):
        self.is_during_process = False

        if (time.time() - self.refresh_time)*1000 > (1000/self.REFRESH_RATE):
            if self.uiHandeler.current_page_name == 'settings':
                self.API_Page_Setting.grab_image_event(self.image)

            elif self.uiHandeler.current_page_name == 'live':
                
                    self.refresh_time = time.time()
                    res_image = self.beltIncpetcion.get_result_image()
                    self.API_Live_View.uiHandeler.set_liveview_belt_img(res_image)

        
        

    def build_camera(self, camera_meta: dict):
        """get camera meta_data and build that camera
        meta data is a dictionary with two key
        {'serial_number': , 'name': }

        Args:
            camera_meta (dict): _description_
        """
        camera_name = camera_meta['name']
        sn = camera_meta['serial_number']
        camera = None
        if self.CAMERA_SIMULATION:
            self.collector.enable_camera_emulation(1)
            camera = self.collector.get_all_cameras(dorsaPylon.CamersClass.emulation)[0]

        else:
            camera = self.collector.get_camera_by_serial(sn)
        if camera is not None:
             camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)
             self.cameras[ camera_name ] = camera
        else:
            print('Warning: camera not exist')

    

    def run_camera_thread(self,camera_name:str): 
        if self.cameras.get(camera_name) is not None:
            try:
                self.cameras[camera_name].Operations.open()
                self.camera_workers[camera_name] = cameraWorker( self.cameras[camera_name] )
                self.camera_threads[camera_name] = threading.Thread(target=self.camera_workers[camera_name].grabber)
                self.camera_workers[camera_name].success_grab_signal.connect(self.grabbed_image_event)
                self.camera_workers[camera_name].grabb_image_error.connect(self.error_grab_image_event)
                self.camera_threads[camera_name].start()
            
            except Exception as e:
                print(e)

        else:
            print('Warning: camera {camera_name} is empty')


    def check_camera_devices_event(self,):
        if not self.is_during_checking_device:

            t = time.time()
            self.checked_device_time = time.time()
            self.is_during_checking_device = True

            self.device_checker_worker = DeviceCheckerWorker(self.collector)
            self.device_checker_thread = threading.Thread(target= self.device_checker_worker.serial_number_finder)
            self.device_checker_worker.serials_ready.connect(self.refresh_camera_devices_event)
            if self.DEBUG_CAMERA_CHECKER_THREAD:
                print('Device Checker on Debug mode')
                self.device_checker_worker.serial_number_finder()
            else:
                self.device_checker_thread.start()
        else:
            if time.time() - self.checked_device_time  > ( self.DEVICE_CHECKer_TIMER / 1000) + 1:
                self.is_during_checking_device = False

    def refresh_camera_devices_event(self):
        self.is_during_checking_device = False
        cameras_sn = self.device_checker_worker.get_available_serials()
        
        self.API_Page_Setting.cameraSettingAPI.update_devices_event(cameras_sn)
        
        if len(self.cameras) == 0:
            print('no camera founded')
            

        # for device_info in self.camera_device_info:
        #     application = device_info['application']
        #     sn = device_info['serial_number']
        #     if self.cameras.get(application) is None:
        #         if sn in cameras_sn:
        #             self.creat_camera(device_info)

        # for cam_aplication, camera in self.cameras.items():
        #     if camera.Infos.get_serialnumber() not in cameras_sn:
        #         self.mainPageAPI.set_system_status('camera_connection', status=False)
        #         #self.camera_disconnect_event()
                
        #     else:
        #         self.mainPageAPI.set_system_status('camera_connection',status=True)
            


             
    def error_grab_image_event(self,):
        print('ERROR GRABBING IMAGE')

    def new_defect_event(self, defect:Defect):
        pass
        self.API_Live_View.new_defect_event(defect)
        info = defect.get_info()
        info['main_path'] = self.DefectFileManager.main_path

        count = Constant.DatabaseLimits.DEFECT_COUNT
        if count is not None:
            if self.db.Defects_DB.count() <= count:
                self.db.Defects_DB.save(info)
                threading.Thread(target=self.DefectFileManager.save, args=(defect,)).start()
            else:
                pass
                #print('WARNING mainAPI: Database is full')
    
    def update_defect_event(self, defect:Defect):
        info = defect.get_info()
        info['main_path'] = self.DefectFileManager.main_path
        self.db.Defects_DB.update(info)
        threading.Thread(target=self.DefectFileManager.save, args=(defect,)).start()

    def delete_defect(self, defect:dict):
        defect_id = defect['defect_id']
        self.beltIncpetcion.DefectTracker.completed_defects.remove_by_id(defect_id)
        notif = self.API_Live_View.uiHandeler.notifications.get_by_id(defect_id)
        if notif !=None :
            self.API_Live_View.uiHandeler.pop_notification(notif)
    
    def run_stop_event(self,):
        self.is_during_process = False
        for camera in self.cameras.values():
            if self.API_Live_View.is_running:
                camera.Operations.start_grabbing()
            else:
                camera.Operations.stop_grabbing()

        #self.beltIncpetcion.Encoder.update_time = time.time()
