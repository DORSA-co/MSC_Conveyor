
import random
import time

import cv2
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import numpy as np

from uiUtils.GUIComponents import defectNotification
from PageUI.LiveView_UI import LiveView_UI
from Detection.Defect import Defect
from Detection.beltInspection import beltInspection
from backend.Utils.Filter import applyFilter

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
                                                defect.jdatetime, 
                                                'should be change', 
                                                (100,200,20)
                                                )

    def __button_connector(self,):
        self.uiHandeler.button_connector('apply_filters', self.apply_filter)
        self.uiHandeler.button_connector('run_stop', self.run_stop)

    
    def run_stop(self,):
        self.is_running = not(self.is_running)
        self.external_run_stop_event_func()

    def set_run_stop_evetn(self, func):
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
        

            
