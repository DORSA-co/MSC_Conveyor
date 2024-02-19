import time

import sys
import os
sys.path.append(os.path.join('UIFiles', 'assets'))
sys.path.append('uiUtils')

from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets, QtCore
from UIFiles.verify_UI import Ui_verifyDialogWin
from backend.UserManager.userLoginRegister import passwordManager
from uiUtils.guiBackend import GUIBackend

from Constants import Constant
from Constants import IconsPath

class VerifyUser(QtWidgets.QDialog):
    def __init__(self, password) -> None:
        super(VerifyUser, self).__init__()

        self.ui = Ui_verifyDialogWin()
        self.ui.setupUi(self)

        GUIBackend.set_input_password(self.ui.verify_password_input)
        GUIBackend.set_win_frameless(self)
        GUIBackend.set_win_attribute(self, QtCore.Qt.WA_TranslucentBackground)
        GUIBackend.button_connector(self.ui.close_btn, self.close_win)
        GUIBackend.button_connector(self.ui.verify_eye_btn, self.show_hide_password)
        GUIBackend.button_connector(self.ui.verify_btn, self.verify_password)

        self.password = password

        self.move_refresh_time = 0
        self.show_password = False

        self.offset = None

        self._center()

    def _center(self):
        # Get primary screen
        primary_screen = QApplication.primaryScreen()

        if primary_screen:
            # Get geometry of the primary screen
            screen_geometry = primary_screen.geometry()

            # Calculate center point
            center_point = screen_geometry.center()

            # Set window position to be centered
            self.move(center_point.x() - self.frameGeometry().width() // 2,
                      center_point.y() - self.frameGeometry().height() // 2)

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

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        if event.key() == 16777220:  # Enter key
            self.ui.verify_btn.click()

    def verify_password(self):
        enterd_password = self.get_inputs()
        res = passwordManager.check_password(enterd_password, self.password)
        if not res:
            self.write_error('Invalid Password')
        else:
            self.accept()

    def show_win(self):
        self.write_error(None)
        return self.exec_()

    def close_win(self):
        self.clear_inputs()
        GUIBackend.close_window(self)

    def show_hide_password(self):
        self.show_password = not self.show_password
        if self.show_password:
            GUIBackend.set_input_normal(self.ui.verify_password_input)
            GUIBackend.set_button_icon(self.ui.verify_eye_btn, IconsPath.IconsPath.WHITE_HIDE_PASSWORD)
        else:
            GUIBackend.set_input_password(self.ui.verify_password_input)
            GUIBackend.set_button_icon(self.ui.verify_eye_btn, IconsPath.IconsPath.WHITE_SHOW_PASSWORD)

    def get_inputs(self):
        password = GUIBackend.get_input(self.ui.verify_password_input)
        return password

    def clear_inputs(self):
        GUIBackend.set_input(self.ui.verify_password_input, "")

    def write_error(self, txt:str):
        """Write Errors message in Logun

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.verify_error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.ui.verify_error_lbl, True)
            GUIBackend.set_label_text( self.ui.verify_error_lbl, txt)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    password = ''

    hashed_pass = passwordManager.hash_password(password)

    main_ui = VerifyUser(hashed_pass)
    ret = main_ui.show_win()
    print(ret)
    app.exec()