
import random
import time

import cv2
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import numpy as np

from uiUtils.GUIComponents import defectNotification
from PageUI.LiveView_UI import LiveView_UI
from Detection.Defect import Defect
from Detection.beltInspection import beltInspection

class LiveView_API:

    """Description of the code

    :param
    """

    def __init__(self, uiHandeler:LiveView_UI , db_Report, belt_incpetcion:beltInspection):
        self.uiHandeler = uiHandeler
        self.beltInspection = belt_incpetcion

        self.uiHandeler.set_notification_click_event(self.notification_click)




    def startup(self,):
        pass

    def endup(self,):
        return True
    

    def new_defect_event(self, defect:Defect):
        self.uiHandeler.append_notification( defect.id,
                                            'material_side', 
                                            'new',
                                            defect.jdatetime, 
                                            'should be change', 
                                            (100,200,20)
                                            )

    def button_connector(self,):
        self.uiHandeler.button_connector(self.connect_camera_API,self.dis_connect_camera_API)    ############## for getting image from camera
        ########self.uiHandeler.button_connector(self.start_selection)  # for getting image from folder

    def notification_click(self, _id):
        defect = self.beltInspection.find_defect(_id)
        info = {'x':1,
                'y':2, 
                'width': defect.widthInfo.max,
                'lenght': defect.lenght, 
                'min depth':defect.depthInfo.min, 
                'max depth':defect.depthInfo.max, 
                'date': defect.jdatetime.strftime('%Y/%m/%d'),
                'time': defect.jdatetime.strftime('%H:%M:%S'),
                }

        self.uiHandeler.show_defect_info(info)