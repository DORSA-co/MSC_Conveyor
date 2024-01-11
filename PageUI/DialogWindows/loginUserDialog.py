import time
from Constants import Constant
from Constants import IconsPath

from uiUtils.guiBackend import GUIBackend
from UIFiles.login_UI import Ui_Dialog
from PySide6.QtWidgets import QDialog
from PySide6 import QtCore
from PySide6 import QtGui

class loginUserDialog(QDialog):
    def __init__(self) -> None:
        super(loginUserDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        GUIBackend.set_input_password(self.ui.password_input)
        GUIBackend.set_win_frameless(self)
        GUIBackend.set_win_attribute(self, QtCore.Qt.WA_TranslucentBackground)
        GUIBackend.button_connector(self.ui.close_btn, self.close_win)
        GUIBackend.button_connector(self.ui.eye_btn, self.show_hide_password)

        self.move_refresh_time = 0
        self.show_password = False

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and event.y() < self.ui.top_frame.height():
            self.offset = QtCore.QPoint(event.position().x(),event.position().y())
        else:
            super().mousePressEvent(event)


    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            if time.time() - self.move_refresh_time > Constant.RefreshRates.MOUSE_MOVE:
                self.move_refresh_time = time.time()
                self.move(self.pos() + QtCore.QPoint(event.scenePosition().x(),event.scenePosition().y()) - self.offset)

        else:
            super().mouseMoveEvent(event)

    def keyPressEvent(self, event):
        if event.key() == 16777220:  # Enter key
            self.ui.login_btn.click()

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def login_button_connector(self, func):
        GUIBackend.button_connector(self.ui.login_btn, func)

    def show_win(self):
        # self.write_error(None)
        GUIBackend.show_window(self, always_on_top=True)

    def close_win(self):
        self.clear_inputs()
        GUIBackend.close_window(self)

    def show_hide_password(self):
        self.show_password = not self.show_password
        if self.show_password:
            GUIBackend.set_input_normal(self.ui.password_input)
            GUIBackend.set_button_icon(self.ui.eye_btn, IconsPath.IconsPath.HIDE_PASSWORD)
        else:
            GUIBackend.set_input_password(self.ui.password_input)
            GUIBackend.set_button_icon(self.ui.eye_btn, IconsPath.IconsPath.SHOW_PASSWORD)

    def get_inputs(self):
        username = GUIBackend.get_input(self.ui.username_input)
        password = GUIBackend.get_input(self.ui.password_input)
        return {'username':username.lower(), 'password':password}

    def clear_inputs(self):
        GUIBackend.set_input(self.ui.username_input, "")
        GUIBackend.set_input(self.ui.password_input, "")

    def write_error(self, txt:str):
        """Write Errors message in Logun

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.login_error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.ui.login_error_lbl, True)
            GUIBackend.set_label_text( self.ui.login_error_lbl, txt)




            

