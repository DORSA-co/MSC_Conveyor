import numpy as np
import random
from functools import partial

from persiantools.jdatetime import JalaliDateTime, JalaliDate
from PySide6.QtWidgets import *
from .Common_Function_UI import Common_Function_UI
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, QRect
from PySide6 import QtGui

from UIFiles.main_UI import Ui_MainWindow
from uiUtils.GUIComponents import defectNotification
from uiUtils.guiBackend import GUIBackend
from UIFiles.popup_slider import Ui_slider
from uiUtils.GUIComponents import singleAnimation
from Constants.IconsPath import IconsPath
from uiUtils import GUIComponents 
from backend.Utils.Filter import applyFilter
from backend.Utils.idList import idList

            

class LiveView_UI(Common_Function_UI):

    """Description of the code

    :param
    """

    def __init__(self, ui:Ui_MainWindow):
        """Description of the code"""

        self.ui = ui
        #self.notifications:list[defectNotification] = [] 
        self.notifications = idList()

        self.buttons = {
            'run_stop':self.ui.run_stop_btn,
        }
        
        self.defect_info_tables_header = ['x',
                                          'y', 
                                          'min_width',
                                          'mean_width',
                                          'max_width',
                                          'length', 
                                          'min_depth', 
                                          'mean_depth', 
                                          'max_depth', 
                                          'date',
                                          'time'
                                          ]

        self.defect_info_tables_units = [
            '',
            '',
            ' (cm)',
            ' (cm)',
            ' (cm)',
            ' (m)',
            ' (mm)',
            ' (mm)',
            ' (mm)',
            '',
            ''
        ]
        
        self.sidebar_alamrms = {
            'system_status': self.ui.system_status_label
        }

        self.active_notificaion = None
        self.__blink_flag = False
        self.__blink_alarms_list = []
        self.external_select_notification_event = None
        self.compareFilters = applyFilter()


        self.setup_defect_info_talbe()
        self.sliderMenu = sliderMenu(self.ui.live_view_page)

        GUIBackend.button_connector_argument_pass(self.ui.system_status_btn,
                                                  self.sliderMenu.slide_in,
                                                  ('system_status',)
                                                )
        GUIBackend.button_connector_argument_pass(self.ui.notif_filter_btn,
                                                  self.sliderMenu.slide_in,
                                                  ('filters',)
                                                )
        GUIBackend.button_connector(self.ui.notif_remove_btn, self.remove_notifications)
        GUIBackend.checkbox_connector(self.ui.select_all_notif_checkbox, self.select_all_notification)
        #self.sliderMenu.apply_filter_connector(self.apply_filter)
        
        #ONLY FOR TEST
        self.sliderMenu.set_system_status('camera', True)
        self.sliderMenu.set_system_status('plc', False)
        self.set_sidebar_alarm('system_status', False)
        a = self.sliderMenu.get_filters()
        #ONLY FOR TEST


    def __blink_alarms(self):
        self.__blink_flag = not(self.__blink_flag)
        for name in self.__blink_alarms_list:
            obj = self.sidebar_alamrms[name]
            if self.__blink_flag:
                obj.setStyleSheet("background-color: #e83323;")
            else:
                obj.setStyleSheet("background-color: #303030;")
        
        #loop blink if any alarm exist 
        if len(self.__blink_alarms_list):
            GUIComponents.single_timer_runner(300, self.__blink_alarms)

    def set_run_stop_icon(self, state):
        if state=='play':
            GUIBackend.set_button_icon(self.buttons['run_stop'], IconsPath.PLAY_ICON)
        else:
            GUIBackend.set_button_icon(self.buttons['run_stop'], IconsPath.PAUSE_ICON)

    def set_sidebar_alarm(self, name, state):
        if state:
            if name in self.__blink_alarms_list:
                self.__blink_alarms_list.remove(name)
            self.sidebar_alamrms[name].setStyleSheet( "background-color:#5ad44e;")

        else:
            self.__blink_alarms_list.append(name)
            #check if it is first alarm, run blink, O.W the blink timer is running
            if len(self.__blink_alarms_list) == 1:
                self.__blink_alarms()

    def button_connector(self, name, func):
        GUIBackend.button_connector(self.buttons[name], func)      

    def setup_defect_info_talbe(self,):
        GUIBackend.set_table_dim(self.ui.defect_info_table, 1, len(self.defect_info_tables_header))
        GUIBackend.set_table_cheaders(self.ui.defect_info_table, 
                                      [self.defect_info_tables_header[i]+self.defect_info_tables_units[i] 
                                       for i in range(len(self.defect_info_tables_header))]
                                    )


    def set_liveview_belt_img(self, image:np.ndarray):
        self.ui.belt_live_view_lbl.set_image(image)
    
    def append_notification(self, 
                            _id: int,
                            side:str,
                            tag:str,
                            datetime:JalaliDateTime,  
                            defect_type:str,
                            defect_color:tuple
                            ):

        notif = defectNotification( _id, 
                                    side, 
                                    tag,
                                    datetime,
                                    defect_type,
                                    defect_color,
                                   )
        self.notifications.insert(0, notif, _id)

        layout = self.ui.defects_notifications_frame.layout()
        layout.insertWidget(0, notif)
        layout.setSpacing(9)
        layout.setContentsMargins(9, 9, 9, 9)
        
        self.ui.alarms_count_lbl.setText(f'{self.notifications.count()} Alarms')

        notif.select_connector(self.click_notification_event)
        notif.close_connector(self.close_notification_event)

    def pop_notification(self, notif:defectNotification):
        layout = self.ui.defects_notifications_frame.layout()
        layout.removeWidget(notif)
        notif.setParent(None)
        self.notifications.remove_by_id(notif.id)

        layout.setSpacing(9)
        layout.setContentsMargins(9, 9, 9, 9)

        self.ui.alarms_count_lbl.setText(f'{self.notifications.count()} Alarms')

    def remove_notifications(self,):
        ans = self.show_confirm_box('close notification',
                                    'Are you sure to close all selected notifications?',
                                    ['yes', 'cancel'],
                                    icon_type='question')
        if ans == 'yes':
            for notif in self.notifications.copy():
                if notif.is_checked():
                    self.pop_notification(notif)

    def select_all_notification(self, state):
        state = GUIBackend.get_checkbox_value(self.ui.select_all_notif_checkbox)
        notif:defectNotification
        for notif in self.notifications.main_list:
            notif.set_checkbox(state)

    def set_notification_click_event(self, func):
        self.external_select_notification_event = func

    def click_notification_event(self, notif:defectNotification):
        if self.active_notificaion is not None:
            self.active_notificaion.set_selected(False)

        notif.set_selected(True)
        self.active_notificaion = notif
        self.external_select_notification_event(notif.id)

    def close_notification_event(self, notif:defectNotification):
        ans = self.show_confirm_box('close notification',
                                    'Are you sure to close this notification?',
                                    ['yes', 'cancel'],
                                    icon_type='question')
        if ans == 'yes':
            self.pop_notification(notif)
    
    def visible_notification(self, _id, state):
        notif:defectNotification
        notif = self.notifications.get_by_id(_id)
        if state:
            notif.setMaximumHeight(10000)
        else:
            notif.setMaximumHeight(0)

    

    def show_defect_info(self, info:dict):
        for key, value in info.items():
            if key not in self.defect_info_tables_header:
                continue
            col = self.defect_info_tables_header.index(key)
            GUIBackend.set_table_cell_value(self.ui.defect_info_table,
                                            (0,col),
                                            value)


class sliderMenu:

    def __init__(self, parent:QWidget) -> None:
        self.parent = parent
        self.__setup()
        
        self.pages_name = {
            'filters': self.ui.notification_filter_page,
            'system_status': self.ui.system_status_page,
        }
        self.system_status = {
            'camera': self.ui.camera_status,
            'plc': self.ui.plc_staus,
            'laser': self.ui.laser_status, 
            'database': self.ui.database_staus
        }

        self.filters = {
            'date': (self.ui.start_date_input, self.ui.end_date_input),
            'width': (self.ui.low_width_input, self.ui.high_width_input),
            'lenght': (self.ui.low_lenght_input, self.ui.high_lenght_input),
            'depth': (self.ui.low_depth_input, self.ui.high_depth_input),
        }

        self.filters_activation = {
            'date': self.ui.filter_date_checkBox,
            'width': self.ui.filter_width_checkBox,
            'lenght': self.ui.filter_lenght_checkBox,
            'depth': self.ui.filter_depth_checkBox,
        }

        self.buttons = {
            'apply_filters':self.ui.filters_apply_btn,
            'clear_filters': self.ui.notif_clear_filter_btn,
        }

        GUIBackend.button_connector(self.ui.close, self.slide_out)
        

        for name in self.filters.keys():
            low_field, high_feild = self.filters[name]
            GUIBackend.connector(low_field, self.__setup_input_limits(name,'low'))
            GUIBackend.connector(high_feild, self.__setup_input_limits(name,'high'))

            GUIBackend.checkbox_connector_argument_pass(self.filters_activation[name], 
                                                        self.__handle_fields_enablity, 
                                                        (name,))
            self.__handle_fields_enablity(False, name)

        self.__set_dates_default_values()

    def __set_dates_default_values(self):
        for field in self.filters['date']:
            GUIBackend.set_date_input(field, JalaliDateTime.now())

    def __setup_input_limits(self, name:str, limit_type:str ):
        def func():
            low_field,high_feild = self.filters[name]
            low_value = GUIBackend.get_input(low_field)
            high_value = GUIBackend.get_input(high_feild)

            if high_value < low_value:
                if limit_type == 'high':
                    GUIBackend.set_input(low_field, high_value, block_signal=True)
                elif limit_type == 'low':
                    GUIBackend.set_input(high_feild, low_value, block_signal=True)
        return func
    
    def __handle_fields_enablity(self,state, name):
        low_field, high_feild = self.filters[name]
        GUIBackend.set_disable_enable(low_field, state)
        GUIBackend.set_disable_enable(high_feild, state)

    def __setup(self,):
        self.ui = Ui_slider()
        self.ui.setupUi(self.parent)
        self.ui.GlobalStyleSheet.setParent(self.parent)
        parent_w = self.parent.width()
        self.ui.GlobalStyleSheet.setGeometry(parent_w,0,0,0)


    def __slider_animation_builder(self,):
        parent_w = self.parent.width()
        parent_h =self.parent.height()
        slider_w = self.ui.GlobalStyleSheet.width()

        self.slide_animation = singleAnimation(self.ui.GlobalStyleSheet, 
                                               b'geometry', 
                                               400, 
                                               QRect(parent_w,0,slider_w,parent_h),
                                               QRect(parent_w-slider_w,0,slider_w,parent_h)
                                               )
        
    def button_connector(self, name, func):
        GUIBackend.button_connector(self.buttons[name], func)

    def slide_in(self, page_name):
        self.ui.pages.setCurrentWidget(self.pages_name[page_name])
        self.__slider_animation_builder()
        self.slide_animation.forward()
        
    def slide_out(self,):
        self.__slider_animation_builder()
        self.slide_animation.backward()

    def disapear(self,):
        self.ui.GlobalStyleSheet.setGeometry(0,0,0,0)

    def set_system_status(self, name, state):
        icon_obj = self.system_status[name]
        if state:
            pixmap  = QPixmap(IconsPath.SUCCESS_ICON)
        else:
            pixmap  = QPixmap(IconsPath.ERROR_ICON)
        icon_obj.setPixmap(pixmap)


    def get_filters(self, ):
        res = {}
        for name in self.filters.keys():
            checkbox = self.filters_activation.get(name)
            if checkbox is not None:
                if not GUIBackend.get_checkbox_value(checkbox):
                    continue
                
            low_obj, high_obj = self.filters[name]
            low_value = GUIBackend.get_input(low_obj)
            high_value = GUIBackend.get_input(high_obj)
            res[name] = (low_value,high_value)
        return res

    def deactive_filters(self):
        for filter_activation in self.filters_activation.values():
            GUIBackend.set_checkbox_value(filter_activation, False)
    