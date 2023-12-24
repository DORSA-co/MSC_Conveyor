import threading
import time

import cv2

from PageAPI.Setting_API import SettingAPI
from PageAPI.AlgorithmCalibration_API import AlgorithmCalibration_API
from PageAPI.LiveView_API import LiveView_API
from PageAPI.Report_API import Report_API
from Database.mainDatabase import mainDatabase
from backend.Camera.dorsaPylon import Collector, Camera
from backend.Camera.cameraThread import cameraWorker, DeviceCheckerWorker
from backend.Camera import dorsaPylon
from main_UI import mainUI
from uiUtils.GUIComponents import timerBuilder
from Detection.beltInspection import beltInspection


CAMERAS = {
     'name': 'main',
     'serial_number':'23287291'
}

class main_API:

    """
    Description of the code

    """
    DEBUG_PROCESS_THREAD = False
    DEVICE_CHECKer_TIMER = 5000
    CAMERA_SIMULATION = True
    
    
    def __init__(self, uiHandeler:mainUI) -> None:

        #########self.collector = Collector()   
        ########self.connect_to_Camera() 
        self.uiHandeler = uiHandeler  #============================== > API = main_API(main_ui)  on main_UI page
        self.db = mainDatabase()

        #--------------------------------------------------------
        kwargs = self.db.Setting_DB.algorithm_setting_db.load()
        self.beltIncpetcion = beltInspection(kwargs)
        #--------------------------------------------------------
        

        self.cameras: dict[str, Camera] = {}
        self.camera_workers:dict[str, cameraWorker] = {}
        self.camera_threads:dict[str, threading.Thread]= {}
        
        self.checked_device_time = time.time()
        self.is_during_checking_device  = False
        
        self.device_checker_timer = timerBuilder(self.DEVICE_CHECKer_TIMER, self.check_camera_devices_event)
        self.device_checker_timer.start()
        
        
        self.build_camera(CAMERAS)
        self.run_camera_thread(CAMERAS['name'])
        self.cameras[CAMERAS['name']].Operations.start_grabbing()
        
        
        self.API_Page_Setting = SettingAPI( self.uiHandeler.Page_Setting, 
                                            self.cameras, 
                                            self.db.Setting_DB,
                                            self.beltIncpetcion )
        
        
        
        self.uiHandeler.change_page_connector(self.page_change_event)
        
        self.pages_api_dict = {
            'settings': self.API_Page_Setting
        }

        
    
    
    def page_change_event(self,prev_page, new_page ):
        if self.pages_api_dict.get(prev_page):
            permision = self.pages_api_dict[prev_page].endup()
        else:
            permision = True

        if permision:
            if self.pages_api_dict.get(new_page):
                self.pages_api_dict[new_page].startup()

        
        

        return
        ###############################      AlgorithmCalibration_API    ################################
        self.API_Page_AlgorithmCalibration = AlgorithmCalibration_API(
            self.uiHandeler.Page_AlgorithmCalibration
        )  # Create Object of AlgorithmCalibration_API  =========== > self.Page_AlgorithmCalibration = AlgorithmCalibration_UI(self.uiHandeler)  on main_UI page
        self.API_Page_AlgorithmCalibration.set_back_event_func(self.get_calibration_paprameter_main_API)   #  introduce and send the name of the  "get_calibration_paprameter_main_API" function to AlgorithmCalibration_API to call this function when the parameters of the calibration is changed on "Save_Calibration_parms"  function in AlgorithmCalibration_API
        param_calibration_API=self.API_Page_AlgorithmCalibration.get_Calibration_parms()     # for getting the initial parameters of the Calibration
        



        ###############################      CameraSetting_API    ################################
        # Create Object of CameraSetting_API   =========== >self.uiHandeler.Page_CameraSetting=CameraSetting_UI(self.uiHandeler)  on main_UI page
        self.API_Page_Setting.set_back_event_func_camera(self.get_camera_paprameter_main_API)   # introduce and send the name of the  "get_camera_paprameter_main_API"  function to API_Page_Setting to call this function when the parameters of the camera is changed
        self.API_Page_Setting.set_back_event_func_algorithm(self.get_algorithm_paprameter_main_API)   # introduce and send the name of the  "get_camera_paprameter_main_API"  function to API_Page_Setting to call this function when the parameters of the camera is changed
        param_camera_API=self.API_Page_Setting.get_Camera_parms()        # for getting the initial parameters of the Camera_Setting
        param_Alghorithm_API=self.API_Page_Setting.get_Algorithhm_parms()        # for getting the initial parameters of the Camera_Setting






        ###############################      LiveView_API    ################################
        self.API_Page_LiveView = LiveView_API(
            self.uiHandeler.Page_LiveView,self.db.Report_DB 
        )  # Create Object of Page_LiveView   =========== > self.Page_LiveView = LiveView_UI(self.uiHandeler)  on main_UI page
        self.API_Page_LiveView.set_initial_param_calibration(param_calibration_API)  # set the initial param of the calibration on liveViewPage
        self.API_Page_LiveView.set_initial_param_camera(param_camera_API)            # set the initial param  of the camera on liveViewPage
        self.API_Page_LiveView.set_initial_param_algorithm(param_Alghorithm_API) 

        ################################      Report_API    ################################
        self.API_Page_Report = Report_API(
            self.uiHandeler.Page_Report,self.db.Report_DB
        )  # Create Object of Report_API   =========== >self.Page_Report = Report_UI(self.uiHandeler)  on main_UI page


        ###################  self.camera = self.collector.get_camera_by_serial(str(self.parms_camera_liveView["Serial"]))
      
        
    def build_camera(self, camera_meta: dict):
        """get camera meta_data and build that camera
        meta data is a dictionary with two key
        {'serial_number': , 'name': }

        Args:
            camera_meta (dict): _description_
        """
        camera_name = camera_meta['name']
        sn = camera_meta['serial_number']
        collector = Collector()
        camera = None
        if self.CAMERA_SIMULATION:
            collector.enable_camera_emulation(1)
            camera = collector.get_all_cameras(dorsaPylon.CamersClass.emulation)[0]

        else:
            camera = collector.get_camera_by_serial(sn)
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



    def grabbed_image_event(self, image):
        self.beltIncpetcion.feed(image)
        if self.uiHandeler.current_page_name == 'settings':
            self.API_Page_Setting.grab_image_event(image)


    
    def check_camera_devices_event(self,):
        if not self.is_during_checking_device:
            self.checked_device_time = time.time()
            self.is_during_checking_device = True

            
            self.device_checker_worker = DeviceCheckerWorker(Collector())
            self.device_checker_thread = threading.Thread(target= self.device_checker_worker.serial_number_finder)
            self.device_checker_worker.serials_ready.connect(self.refresh_camera_devices_event)
            if self.DEBUG_PROCESS_THREAD:
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