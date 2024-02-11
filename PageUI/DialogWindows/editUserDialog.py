import time

from PySide6.QtWidgets import QDialog, QApplication
from PySide6 import QtCore

from Constants import Constant
from Constants import IconsPath
from uiUtils.guiBackend import GUIBackend
from UIFiles.edit_user import Ui_editUserDialogWin

class editUserDialog(QDialog):
    def __init__(self) -> None:
        super(editUserDialog, self).__init__()

        self.ui = Ui_editUserDialogWin()
        self.ui.setupUi(self)

        GUIBackend.set_win_frameless(self)
        GUIBackend.set_win_attribute(self, QtCore.Qt.WA_TranslucentBackground)

        self.fields = {
            'username': self.ui.username_input, 
            'password': self.ui.password_input,
            'role': self.ui.role_combobox,
        }

        GUIBackend.button_connector(self.ui.cancel_btn, self.close_win)
        GUIBackend.button_connector(self.ui.close_btn, self.close_win)
        # GUIBackend.button_connector(self.ui.eye_btn, self.show_hide_password)

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

    def show_hide_password(self):
        self.show_password = not self.show_password
        if self.show_password:
            GUIBackend.set_input_normal(self.ui.password_input)
            GUIBackend.set_button_icon(self.ui.eye_btn, IconsPath.IconsPath.BLACK_HIDE_PASSWORD)
        else:
            GUIBackend.set_input_password(self.ui.password_input)
            GUIBackend.set_button_icon(self.ui.eye_btn, IconsPath.IconsPath.BLACK_SHOW_PASSWORD)

    def save_button_connector(self, func):
        GUIBackend.button_connector(self.ui.save_btn, func)

    def set_inputs(self, user):
        for field_name, field in self.fields.items():
            if field_name == 'password':
                value = '•'*8
            else:
                value = user[field_name]
            GUIBackend.set_input( field, value )


    def get_inputs(self):
        user_info = {}
        for field_name, field in self.fields.items():
            user_info[field_name] = GUIBackend.get_input( field, )
        return user_info
    
    def set_role_items(self, roles:list[str]):
        GUIBackend.set_combobox_items(self.ui.role_combobox, roles)


    def write_edit_user_error(self, txt:str):
        """Write Errors message in change password

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.ui.error_lbl, True)
            GUIBackend.set_label_text(self.ui.error_lbl, txt)
    
    def close_win(self,):
        GUIBackend.close_window(self)
        for field_name, field in self.fields.items():
            GUIBackend.set_input( field, "")

    def show_win(self, user:dict):
        self.set_inputs(user)
        self.write_edit_user_error(None)
        GUIBackend.show_window(self, True)
        
        