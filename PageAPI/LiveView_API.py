
import random
import time

import cv2
# from persiantools.jdatetime import JalaliDate, JalaliDateTime
from datetime import datetime
import numpy as np

from uiUtils.GUIComponents import defectNotification
from uiUtils.GUIComponents import VerifyUser
from PageUI.LiveView_UI import LiveView_UI
from Detection.Defect import Defect
from Detection.beltInspection import beltInspection
from backend.Utils.Filter import applyFilter
from Constants import Constant

class LiveView_API:

    """Description of the code

    :param
    """

    def __init__(self, uiHandeler:LiveView_UI , db_Report, belt_incpetcion:beltInspection):
        self.uiHandeler = uiHandeler
        self.beltInspection = belt_incpetcion

        self.compareFilters = applyFilter()

        self.external_run_stop_event_func = None
        self.is_running = False

        self.uiHandeler.set_notification_click_event(self.notification_click)
        
        self.__button_connector()

        self.logined_user_username = Constant.User.UNLOGIN_USER_USERNAME
        self.logined_user_password = Constant.User.UNLOGIN_USER_PASSWORD

    def startup(self,):
        pass

    def endup(self,):
        return True
    

    def new_defect_event(self, defect:Defect):
        info = defect.get_info_for_filter()
        if self.compareFilters.check_filter(info):
            self.uiHandeler.append_notification( defect.id,
                                                'material_side', 
                                                'new',
                                                defect.datetime, 
                                                'should be change', 
                                                (100,200,20)
                                                )

    def __button_connector(self,):
        self.uiHandeler.sliderMenu.button_connector('apply_filters', self.apply_filter)
        self.uiHandeler.sliderMenu.button_connector('clear_filters', self.clear_filters)
        self.uiHandeler.button_connector('run_stop', self.run_stop)

    def set_logined_user(self, username, password):
        self.logined_user_username = username
        self.logined_user_password = password

    def run_stop(self,):
        # verify = VerifyUser(self.logined_user_username, self.logined_user_password)
        # res = verify.render()
        # if not res:
        #     return
        self.is_running = not(self.is_running)
        self.uiHandeler.set_run_stop_icon('pause' if self.is_running else 'play')
        self.external_run_stop_event_func()

    def set_run_stop_event(self, func):
        self.external_run_stop_event_func = func

    def notification_click(self, _id):
        defect:Defect
        defect = self.beltInspection.find_defect(_id)
        info = defect.get_info()

        self.uiHandeler.show_defect_info(info)
    

    def apply_filter(self,):
        filters = self.uiHandeler.sliderMenu.get_filters()
        self.compareFilters.set_filters_refrence(filters)

        ids = self.uiHandeler.notifications.ids()
        defect:Defect
        for _id in ids:
            defect = self.beltInspection.find_defect(_id)
            if self.compareFilters.check_filter(defect.get_info_for_filter()):
                self.uiHandeler.visible_notification(_id, True)
            else:
                self.uiHandeler.visible_notification(_id, False)
        

    def clear_filters(self,):
        self.uiHandeler.sliderMenu.deactive_filters()
        self.apply_filter()
