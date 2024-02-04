import pickle
import cv2
import numpy as np
import time



from backend.Camera.dorsaPylon import Camera
from PageUI.Setting_UI import Setting_UI, CameraSetting_UI, AlgorithmSetting_UI
from Database.Setting_DB import settingDB, cameraSettingDB, algorithmSettingDB
from Detection.beltInspection import beltInspection
from Detection.AnomalyDetection import ANOMALY_ALGORITHMS
from backend.Utils.mapDictionary import mapDictionary

class SettingAPI:
    
    def __init__(self, uiHandeler:Setting_UI, 
                 cameras:dict[str,Camera],
                 db:settingDB, 
                 belt_inspection: beltInspection) -> None:
        self.uiHandeler = uiHandeler

        self.cameraSettingAPI = CameraSetting_API(uiHandeler.CameraSetting, 
                                                  cameras, 
                                                  db.camera_setting_db)
        
        self.AlgorithmSettingAPI = AlgorithmSetting_API(uiHandeler.AlgorithmSetting,
                                                        belt_inspection,
                                                        db.algorithm_setting_db)
        
    
    def grab_image_event(self, image):
        name = self.uiHandeler.get_tabname()
        if name == 'camera_tab':
            self.cameraSettingAPI.grab_image_event(image)
        elif name == 'algorithm_tab':
            self.AlgorithmSettingAPI.grab_image_event(image)
        
    
    def startup(self,):
        self.cameraSettingAPI.startup()
        self.AlgorithmSettingAPI.startup()


    def endup(self,):
        self.AlgorithmSettingAPI.load_algorithm_settings()
        self.cameraSettingAPI.load_camera_settings()

class CameraSetting_API:

    """Description of the code

    :param
    
    """

    def __init__(self, ui:CameraSetting_UI, cameras:dict[str,Camera], db:cameraSettingDB):
        self.ui_cam = ui  # ui =self.ui.Page_CameraSetting    =====>  self.ui.Page_CameraSetting=CameraSetting_UI(self.ui)  on main_UI page
        self.cameras = cameras
        self.db = db
        
        
        self.ui_cam.button_connector('save', self.save_camera_settings)
        self.ui_cam.button_connector('cancel', self.load_camera_settings)
        self.ui_cam.button_connector('default', self.reset_camera_settings)
        self.ui_cam.button_connector('play', self.play_camera)
        self.ui_cam.setting_change_connector(self.camera_setting_change_event)
        
        self.setup_camera_settings_availables_value()
        self.load_camera_settings()

    def startup(self,):
        name = self.ui_cam.get_camera_name()
        grabbing = self.cameras[name].Status.is_grabbing()
        self.ui_cam.set_playing_status(grabbing)
        
    def update_devices_event(self, items:list[str]):
        items.insert(0,'--select--')
        self.ui_cam.set_serial_number_tems(items)
        
    
    def grab_image_event(self, image):
            self.ui_cam.show_image(image)
        
    def save_camera_settings(self, ):
        parms = self.ui_cam.get_camera_parms_UI()
        parms['name'] = self.ui_cam.get_camera_name()
        parms['serial_number'] = self.ui_cam.get_serial_number()
        self.db.save(parms)
        self.ui_cam.save_state(True)

    def reset_camera_settings(self, ):
        self.db.restor_default()
        self.load_camera_settings()
        self.ui_cam.save_state(True)

    def play_camera(self,):
        name = self.ui_cam.get_camera_name()
        grabbing = self.cameras[name].Status.is_grabbing()
        if grabbing:
            self.cameras[name].Operations.stop_grabbing()
        else:
            self.cameras[name].Operations.start_grabbing()
        
        grabbing = self.cameras[name].Status.is_grabbing()
        self.ui_cam.set_playing_status(grabbing)

    
    def load_camera_settings(self, ):
        name = self.ui_cam.get_camera_name()
        parms = self.db.load(name)
        self.ui_cam.set_serial_number(parms.get('serial_number'))
        self.ui_cam.set_camera_parms_UI(parms)
        self.ui_cam.save_state(True)
        
    
    def setup_camera_settings_availables_value(self,):
        name = self.ui_cam.get_camera_name()
        data = {}
        data['gain'] = self.cameras[name].Parms.get_gain_range()
        data['exposure'] = self.cameras[name].Parms.get_exposureTime_range()
        
        h_range, w_range, x_range, y_range =  self.cameras[name].Parms.get_roi_range()
        data['width'] = w_range
        data['height'] = h_range
        data['offset_x'] = x_range
        data['offset_y'] = y_range
        
        self.ui_cam.set_camera_parms_available_value(data)

    
    def camera_setting_change_event(self, name):
        parms = self.ui_cam.get_camera_parms_UI()
        value = parms[name]
        camera_name = self.ui_cam.get_camera_name()
        
        if name == 'gain':
            self.cameras[camera_name].Parms.set_gain(value)
            
        elif name == 'exposure':
            self.cameras[camera_name].Parms.set_exposureTime(value)
            
        elif name == 'width':
            self.cameras[camera_name].Parms.set_roi(None, value, None, None)
        
        elif name == 'height':
            self.cameras[camera_name].Parms.set_roi(value, None, None, None)
        
        elif name == 'offset_x':
            self.cameras[camera_name].Parms.set_roi(None, None, value, None)
        
        elif name == 'offset_y':
            self.cameras[camera_name].Parms.set_roi(None, None, None, value)
        
            
        else:
            print(f'{name} Setting is not available')
        

    # def calculate_tear_depth(self):
    #    perspective = np.cos(60 * 3.14159 / 180)  
    #    if self.camera !=None:
    #        #self.camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)         ###################  for getting image from  camera
    #        # self.camera.Operations.start_grabbing()
    #         #self.camera.Parms.set_exposureTime(5000)
    #        # self.camera.Parms.set_gain(517)  #217   #### get the good answer
    #        parms_camera = self.ui_cam.get_camera_parms_UI()
    #        Exposure=parms_camera["Exposure"]
    #        Gain=parms_camera["Gain"]

    #        self.camera.Parms.set_exposureTime(Exposure)      # Get good answer for second version ----- 5000
    #        self.camera.Parms.set_gain(Gain)  #217   #### get the good answer         # Get good answer for second version ----- 517
    #        img = self.camera.getPictures()
    #        img = img[:, 25:620]
    #        img = cv2.blur(img, (5, 1))
    #        h, w = img.shape
    #        total_sum = 0
    #        total_count = 0

    #        for i in range(w-1):
    #           for j in range (h-1):
    #               if  img[j,i]>100:
    #                   #print(img[i,j])
    #                   total_count += 1
    #                   total_sum += j
    #           if total_count>0:
    #                 a=int((total_sum / total_count)) /(perspective + 0.01)
    #                 #print("sum of defect")
    #                 #print(a)
                      
    #        #max=defect_detection_find_max(img ,470)
    #        #print(a)
    #        self.ui_cam.show_tear_depth(a)

class AlgorithmSetting_API:
    def __init__(self, 
                 uiHandeler:AlgorithmSetting_UI, 
                 belt_inspection:beltInspection, 
                 db:algorithmSettingDB):
        self.uiHandeler = uiHandeler
        self.db = db
        self.belt_inspection = belt_inspection

        self.map_items = {
            "anomaly_algorithm":{ANOMALY_ALGORITHMS.LINE_FIT: 'line',
                                 ANOMALY_ALGORITHMS.CURVE_FIT: 'curve'
                                }
        }


        self.mapDict = mapDictionary(self.map_items)

        self.uiHandeler.setting_change_connector(self.setting_change_event)

        self.uiHandeler.button_connector('save', self.save_algorithm_settings)
        self.uiHandeler.button_connector('reset', self.reset_algorithm_settings)
        self.uiHandeler.button_connector('cancel', self.load_algorithm_settings)

        for combo_name in self.mapDict.get_maps_names():
            items = self.mapDict.get_values(combo_name)
            self.uiHandeler.set_combobox_items(combo_name, items)

        
    def startup(self,):
        self.load_algorithm_settings()


    def setting_change_event(self, name):
        value = self.uiHandeler.get_parm(name)

        #if a map is exist for name, convert the value to key, o.w no chane on value
        value = self.mapDict.value2key(map_name=name, value=value)

        self.belt_inspection.kwargs[name] = value

    def grab_image_event(self, image:np.ndarray):
        
        res = np.zeros(image.shape + (3,), dtype=np.uint8)
        
        step1_img = self.belt_inspection.LaserScanner.draw(res)
        #cv2.imshow('step1', step1_img)
        self.uiHandeler.set_image('step1', step1_img)

        
        step2_img = self.belt_inspection.AnomalyDetection.draw(image=step1_img)
        self.uiHandeler.set_image('step2', step2_img)
        #cv2.imshow('step2', step2_img)
        #cv2.waitKey(1)

        step3_img = self.belt_inspection.DefectExtractor.draw(image=step2_img)
        self.uiHandeler.set_image('step3', step3_img)

        step5_img = self.belt_inspection.res_image
        self.uiHandeler.set_image('step5', step5_img)

    def load_algorithm_settings(self,):
        parms = self.db.load()
        parms = self.mapDict.multi_key2value(parms)
        self.uiHandeler.set_parms(parms)
        self.uiHandeler.save_state(True)
    
    def save_algorithm_settings(self,):
        parms = self.uiHandeler.get_parms()
        parms = self.mapDict.multi_value2key(parms)
        self.db.save(parms)
        self.uiHandeler.save_state(True)

    def reset_algorithm_settings(self):
        self.db.restor_default()
        self.load_algorithm_settings()
        self.uiHandeler.save_state(True)

    