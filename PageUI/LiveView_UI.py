import numpy as np
import random

from PySide6.QtWidgets import *
from functools import partial
from .Common_Function_UI import Common_Function_UI
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer
from PySide6 import QtGui
import time
from UIFiles.main_UI import Ui_MainWindow
from uiUtils.GUIComponents import defectNotification
from persiantools.jdatetime import JalaliDateTime, JalaliDate

class LiveView_UI(Common_Function_UI):

    """Description of the code

    :param
    """

    def __init__(self, ui:Ui_MainWindow):
        """Description of the code"""

        self.ui = ui

        layout = self.ui.defects_notifications_widget.layout()
        for i in range(15):
            not1 = defectNotification('clean side', 
                                  random.choice([JalaliDate.today(), JalaliDate(year=1402, month=10, day=10), JalaliDate(year=1402, month=10, day=30)]),
                                  JalaliDateTime.today(),
                                  'normal',
                                  (np.random.randint(0, 254), np.random.randint(0, 254), np.random.randint(0, 254)))
        
            layout.insertWidget(0, not1)
    #     self.general_information_live = {
    #         "Length": self.ui.Length,
    #         "Width": self.ui.Width,
    #         "Depth": self.ui.Depth,
    #         "Total_Number_Defect": self.ui.Total_Number_Defect,
    #         "Total_Number_Critical_defect": self.ui.Total_Number_Critical_defect,
    #     }
    #     self.style_information_live = {
    #         "Not_Critical_live_view": self.ui.Not_Critical_live_view,
    #         "Critical_live_view": self.ui.Critical_live_view,
    #         "Normal_live_view": self.ui.Normal_live_view,
    #     }

    #     self.style_information_laser={

    #      "Laser" : self.ui.Laser_Connection

    #     }

    #     self.style_information_Camera={

    #      "Camera" : self.ui.Laser_Connection_Check

    #     }

    #     self.ui.Stop_connection.setEnabled(False)
    #     self.ui.live.setEnabled(False)
    #     self.ui.Stop.setEnabled(False)
    #     self.camera_connection=False
       
    #     #self.camera=False
    #     self.t = time.time()
    #     self.picktimer=None



    # #def button_connector(self,camera_connection):   # input fun for getting image from folder
    # def button_connector(self,fun1,fun2):   # input fun for getting image from folder
    #     #self.camera_connection=camera_connection
    #    ####### self.ui.Camera_connection.clicked.connect(partial(self.connect_camera))
    #    ########## self.ui.Stop_connection.clicked.connect(partial(self.disconnect_camera))
    #     self.ui.Camera_connection.clicked.connect(partial(fun1))
    #     self.ui.Stop_connection.clicked.connect(partial(fun2))
       

    #    # self.ui.live.clicked.connect(
    #    #     fun
    #    # )  ###################  for getting image from  folder

    # def Set_fn(self, fun):
    #     self.fn = fun

    # def Get_fn(self):
    #     return self.fn

    # def button_connector_QTimer(self, fun):
    #     self.Set_fn(fun)
    #     self.ui.live.clicked.connect(self.button_connector_QTimer_fun)

    # def button_connector_stop(self):
        
    #    self.ui.Stop.clicked.connect(self.stop_live)
      

    # def stop_live(self):
    #     self.picktimer.stop()
    #     self.ui.live.setEnabled(True)
    #     self.ui.Stop.setEnabled(False)

    # def button_connector_QTimer_fun(self):
    #     fun = self.Get_fn()
    #     self.picktimer = QTimer()
    #     #self.picktimer.setInterval(0.001)
    #     self.picktimer.timeout.connect(fun)
    #     #self.picktimer.start(20)
    #     self.picktimer.start(5)


    #    ################ self.time = QTimer()
    #     #self.picktimer.setInterval(0.001)
    #    ################# self.time.timeout.connect(self.show_time)
    #   #############  self.time.start(1000)


    # def show_time(self):

    #     print(time.time()-self.t)


    # def connect_camera(self):
    #     ##print("connect_camera")
    #     ##self.enable_disable_camera_btns(True)
    #     pass
    # def disable_live(self):
    #     self.ui.live.setEnabled(False)

    # def enable_stop(self):
    #     self.ui.Stop.setEnabled(True)


    # def connect_Camera_liveView_button(self):
    #         self.ui.Camera_connection.setEnabled(False)
    #         self.ui.Stop_connection.setEnabled(True)
    #         self.ui.live.setEnabled(True)




    # def disconnect_Camera_liveView_button(self):
    #         if self.picktimer:
    #          self.picktimer.stop()
    #         self.ui.live.setEnabled(False)
    #         self.ui.Stop_connection.setEnabled(False)
    #         self.ui.Camera_connection.setEnabled(True)
    #         self.ui.Stop.setEnabled(False)
        
    # def disconnect_camera(self):  
    #    pass

    # def set_general_information(self, infoes: dict):
    #     for name, value in infoes.items():
    #         self.general_information_live[name].setText(value)

    # def set_style_information(self, styles: dict):
    #     for name, value in styles.items():
    #         self.style_information_live[name].setStyleSheet(value)


    # def set_style_laser(self, styles: dict):
    #       for name, value in styles.items():
    #         self.style_information_laser[name].setStyleSheet(value)


    # def set_style_Camera(self, styles: dict):
    #       for name, value in styles.items():
    #         self.style_information_Camera[name].setStyleSheet(value)





    # def set_Meassage_on_API(self, text_on_UI):
    #         self.set_message(
    #             label_name=self.ui.Message_LiveView,
    #             text=text_on_UI,
    #         )



    # def set_Pixmap(self, img_data, w, h, bytes_per_line):
    #     convert_to_Qt_format = QImage(
    #         img_data,
    #         w,
    #         h,
    #         bytes_per_line,
    #         QImage.Format_BGR888,  # This is used to show the heatmap of the defect in output
    #     )
    #     ######self.ui.Showlive.setPixmap(QPixmap.fromImage(convert_to_Qt_format))
    #     self.ui.Showlive.setPixmap(QPixmap.fromImage(convert_to_Qt_format).transformed(QtGui.QTransform().rotate(90)))    ########## for rotate image
