from __future__ import annotations
import sys
import time

import numpy as np

from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from PySide6 import QtCore

from UIFiles.image_viewer import Ui_ViewerWindow
from UIFiles.belt_tile import Ui_Tile

from Constants import Constant
from Constants import IconsPath
from uiUtils.guiBackend import GUIBackend
from PageUI.Common_Function_UI import Common_Function_UI 
from uiUtils.guiBackend import GUIBackend
from uiUtils.GUIComponents import Color

class viewerUI(QMainWindow):

    """this class is used to build class for mainwindow to load GUI application

    :param QtWidgets: _description_

    """
    def __init__(self):
        """this function is used to laod ui file and build GUI application"""
        super(viewerUI, self).__init__()

        self.ui = Ui_ViewerWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

        self.common_func=Common_Function_UI()

        self.move_refresh_time = 0
        self.tile_external_event_func = None

        self.buttons_connection()

        self.buttons = {
            'view_3d': self.ui.view_3d_btn
        }

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = QtCore.QPoint(event.position().x(),event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton and event.y() < self.ui.top_frame.height():
            if time.time() - self.move_refresh_time > Constant.RefreshRates.MOUSE_MOVE:
                self.move_refresh_time = time.time()
                self.move(self.pos() + QtCore.QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)

        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event):
        if event.y() < self.ui.top_frame.height():
            self.maxmize_minimize()
            super().mouseDoubleClickEvent(event)

    def button_connector(self, name, func):
        GUIBackend.button_connector(self.buttons[name], func)

    def buttons_connection(self):
        """main butoons connect -- exit , minize , maximize, help --"""
        self.ui.close_btn.clicked.connect(self.close_win)
        self.ui.minimize_btn.clicked.connect(self.minimize)
        self.ui.maximize_btn.clicked.connect(self.maxmize_minimize)

    def minimize(self):
        """Minimize winodw"""
        self.showMinimized()

    def close_win(self):
        """
        this function closes the app
        Inputs: None
        Returns: None
        """

        res = self.common_func.show_alert_window(
            title="Exit",
            message="Do you want to exit?",
            need_confirm=True,
            level=1,
        )

        if res:
            self.app_close_flag = True
            self.close()
            sys.exit()

    def maxmize_minimize(self):
        """Maximize or Minimize window"""
        if self.isMaximized():
            self.showNormal()
            GUIBackend.set_button_icon(self.ui.maximize_btn, IconsPath.IconsPath.MAXIMIZE_ICON)
        else:
            self.showMaximized()
            GUIBackend.set_button_icon(self.ui.maximize_btn, IconsPath.IconsPath.MINIMIZE_ICON)


    def set_image(self, image: np.ndarray):
        self.ui.tile_image_viewer.set_image(image)

    def add_tile(self, _id, color, meterage):
        tile = Tile(_id, meterage=meterage, color=color)
        tile.select_connector(self.tile_select_event)
        layout = self.ui.tiles_frame.layout()
        layout.addWidget(tile)
    
    def tile_select_connector(self, func):
        self.tile_external_event_func = func

    def tile_select_event(self, tile:Tile):
        self.tile_external_event_func(tile.id)
        


class Tile(QtWidgets.QWidget):
    def __init__(self,_id, meterage, color):
        """this function is used to laod ui file and build GUI application"""
        super(Tile, self).__init__()
        self.id = _id

        self.ui = Ui_Tile()
        self.ui.setupUi(self)

        self.external_select_event_func = None

        self.set_meterage(meterage)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.external_select_event_func(self)

    def select_connector(self, func):
        self.external_select_event_func = func

    def set_meterage(self, meterage:tuple):
        GUIBackend.set_label_text(self.ui.meterage_label, '{} - {}'.format(meterage[0], meterage[1]))

    def set_color(self, color):
        color_obj = Color(color)
        GUIBackend.set_style(self.ui.frame, "background-color: {};".format(color_obj.hex_color))
        
