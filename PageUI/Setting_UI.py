from .Common_Function_UI import Common_Function_UI
from functools import partial
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6 import QtWidgets
from UIFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from uiUtils.GUIComponents import MULTISTEP_SELECT_STYLE, MULTISTEP_UNSELECT_STYLE
import copy


class Setting_UI:
    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui
        self.CameraSetting = CameraSetting_UI(ui)
        self.AlgorithmSetting = AlgorithmSetting_UI(ui)

    def get_tabname(self):
        return GUIBackend.get_current_tab_text(self.ui.settings_tabs)
    
class CameraSetting_UI(Common_Function_UI):

    """Description of the code"""

    def __init__(self, ui:Ui_MainWindow):
        super(CameraSetting_UI, self).__init__()
        self.ui = ui  # self.Page_CameraSetting = CameraSetting_UI(self.ui)   on main_UI
        #self.serial_number_cobobox = self.ui.serial_number_spinBox

        self.camera_setting_fields = {
            "gain": self.ui.gain_spinbox,
            "exposure": self.ui.expo_spinbox,
            "width": self.ui.width_spinbox,
            "height": self.ui.height_spinbox,
            "offset_x": self.ui.offsetx_spinbox,
            "offset_y": self.ui.offsety_spinbox,
        }
        
        self.enable_on_playing = {
            "gain":     True,
            "exposure": True,
            "width":    False,
            "height":   False,
            "offset_x": False,
            "offset_y": False,
        }
        
        
        self.buttons = {
            'save': self.ui.save_camera_settings,
            'play': self.ui.connect_camera_switch,
        }
        
        self.parms_camera = {
            "Serial": 0,
            "Gain": 0,
            "Exposure": 0,
            "Width": 0,
            "Height": 0,
            "offsetX": 0,
            "offsetY": 0,
            "Serial_2": 0,
            "Gain_2": 0,
            "Exposure_2": 0,
            "Width_2": 0,
            "Height_2": 0,
            "offsetX_2": 0,
            "offsetY_2": 0,
        }

        # self.general_information_algorithm = {
        #     "GRADIENT_SIZE": self.ui.SpinBox_GRADIENT_SIZE,
        #     "Critical_Depth": self.ui.SpinBox_Critical_Depth,
        #     "TEAR_DEPTH": self.ui.SpinBox_TEAR_DEPTH,
        #     "MAX_ERROR": self.ui.SpinBox_MAX_ERROR,
        #     "pix_length":self.ui.pix_length,
        #     "pix_width":self.ui.pix_width,
        #     "gradient_number":self.ui.gradient_number
           
        # }
        
        self.parms_algorithm = {
            "GRADIENT_SIZE": 0,
            "Critical_Depth": 0,
            "TEAR_DEPTH": 0,
            "MAX_ERROR": 0,
            "pix_length":0,
            "pix_width":0,
            "gradient_number": 0
        }

        # self.ui.Stop_connection_Camera_setting.setEnabled(False)

    def button_connector(self, btn_name:str, function):
        if isinstance(self.buttons[btn_name], QtWidgets.QPushButton):
            self.buttons[btn_name].clicked.connect( function )
        elif isinstance(self.buttons[btn_name], QtWidgets.QCheckBox):
            self.buttons[btn_name].stateChanged.connect( function )
        
    def setting_change_connector(self, func):
        for name, field in self.camera_setting_fields.items():
            field.valueChanged.connect( self.__create_event_func__(func, (name,)) )
            
    def set_playing_status(self, is_playing):
        GUIBackend.set_signal_connection(self.buttons['play'], False)
        GUIBackend.set_checkbox_value(self.buttons['play'], is_playing)
        GUIBackend.set_signal_connection(self.buttons['play'], True)
 
        self.handle_fields_enablity(is_playing)

    def handle_fields_enablity(self, is_playing):
        for name, flag in self.enable_on_playing.items():
            field = self.camera_setting_fields[name]
            if is_playing:
                if flag:
                    field.setEnabled(True)
                else:
                    field.setEnabled(False)
                    
            else:
                field.setEnabled(True)
                    
                    

    def show_tear_depth(self,max):
         self.ui.Show_Tear_Depth_Label.setText(str(max))


    def connect_camera(self):
        # self.ui.Camera_connection_Camera_setting.setEnabled(False)
        self.set_message(
            label_name=self.ui.Message_Camera,
            text="Connect to Camera Successfully",
        )

        self.ui.Stop_connection_Camera_setting.setEnabled(True)

    def disconnect_camera(self):
        # print("disconnect_camera")
        # self.enable_disable_camera_btns(False)
        # self.ui.Camera_connection_Camera_setting.setEnabled(True)
        # self.ui.Stop_connection_Camera_setting.setEnabled(False)
        self.set_message(
            label_name=self.ui.Message_Camera,
            text="Disconnect to Camera Successfully",
        )

    def set_message_on_label(self, txt):
        self.set_message(
            label_name=self.ui.Message_Camera,
            text=txt,
        )

    def set_camera_parms_UI(self, infoes: dict):
        for name, value in infoes.items():
            if name in self.camera_setting_fields.keys():
                self.camera_setting_fields[name].setValue(value)
            else:
                print(f'CAMERA_SETTING_UI: no filed find for camera {name} parm')
                
    
    def set_camera_parms_available_value(self, infoes:dict):
        for name, avaiable_value in infoes.items():
            field = self.camera_setting_fields.get(name)
            if field is not None:
                if isinstance(field, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
                    field.setMinimum(avaiable_value[0])
                    field.setMaximum(avaiable_value[1])



    def get_camera_parms_UI(self):
        res = {}
        for name, field in self.camera_setting_fields.items():
            res[name] = field.value()

        return res
    
    
    
    def get_camera_name(self,):
        return 'main'
    
    
    def get_serial_number(self,):
        return self.ui.devices_sn_combobox.currentText()
    
    def set_serial_number(self, item:str):
        if item is not None:
            self.ui.devices_sn_combobox.setCurrentText(item)
    
    
    def set_serial_number_tems(self, items:list[str]):
        self.ui.devices_sn_combobox.blockSignals(True)
        
        current = self.get_serial_number()
        self.ui.devices_sn_combobox.clear()
        self.ui.devices_sn_combobox.insertItems(0, items)
        self.set_serial_number(current)
        
        self.ui.devices_sn_combobox.blockSignals(False)
        
        


    def show_image(self, image):
        GUIBackend.set_label_image(self.ui.camera_settings_live_label, image )

class AlgorithmSetting_UI(Common_Function_UI):

    def __init__(self, ui:Ui_MainWindow):
        super().__init__()

        self.ui = ui

        self.setting_parms = {
            'background_thresh': self.ui.alghoritm_background_thresh,
            'conv_window_size': self.ui.alghoritm_conv_window_size,
            'anomaly_algorithm': self.ui.anomaly_alghorithm_combo,
            'diff_thresh': self.ui.anomaly_thresh_error,
            'defect_min_width': self.ui.defect_extractor_min_width
        }

        self.combobox_items = {}

        self.images_lbl = {
            'step1': self.ui.algorithm_image1,
            'step2': self.ui.algorithm_image2,
            'step3': self.ui.algorithm_image3,
        }

        self.multistep_buttons = {
            'step1': self.ui.step1_btn,
            'step2': self.ui.step2_btn,
            'step3': self.ui.step3_btn,
        }

        self.buttons = {
            'save': self.ui.save_algorithm_settings
        }

        self.multistep_button_connector('step1', lambda: self.change_steps_stackedwidget_page(0, 'step1') )
        self.multistep_button_connector('step2', lambda: self.change_steps_stackedwidget_page(1, 'step2') )
        self.multistep_button_connector('step3', lambda: self.change_steps_stackedwidget_page(2, 'step3') )

        self.change_steps_stackedwidget_page(0, 'step1')

    def button_connector(self, name:str, func):
        GUIBackend.button_connector(self.buttons[name], func)

    def multistep_button_connector(self, name:str, func):
        GUIBackend.button_connector(self.multistep_buttons[name], func)

    def get_parms(self,):
        parms = {}
        for name, field in self.setting_parms.items():
            value = GUIBackend.get_input(field)
            parms[name] = value
        return parms
    
    def get_parm(self, name:str):
        return GUIBackend.get_input(self.setting_parms[name])


    def set_parms(self, parms:dict):
        for name, value in parms.items():
            field = self.setting_parms.get(name)
            if field:
                GUIBackend.set_input(field, value)
            else:
                print(f'{name} not exist in UI fields in algorithm setting')
    
    def set_parm(self, name:str, value):
        field = self.setting_parms.get(name)
        if field:
            GUIBackend.set_input(field, value)
        else:
            print(f'{name} not exist in UI fields in algorithm setting')


    def set_combobox_items(self, name:str, items:list[str]):
        items = list(items)
        GUIBackend.set_combobox_items(self.setting_parms[name],
                                      items)

    def set_image(self, name: str, image):
        GUIBackend.set_label_image(self.images_lbl[name], image)

    def change_steps_stackedwidget_page(self, idx: int, name: str):
        GUIBackend.set_stack_widget_idx(self.ui.algorithm_stackedWidget, idx)
        for key in self.multistep_buttons:
            if key == name:
                GUIBackend.set_style(self.multistep_buttons[key], MULTISTEP_SELECT_STYLE)
            else:
                GUIBackend.set_style(self.multistep_buttons[key], MULTISTEP_UNSELECT_STYLE)

    def setting_change_connector(self, func):
        for name, field in self.setting_parms.items():
            GUIBackend.connector(field, self.__create_event_func__(func, (name,)) )









