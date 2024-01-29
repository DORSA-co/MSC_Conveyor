from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from PySide6 import QtWidgets, QtCore, QtGui
import cv2

from uiUtils.GUIComponents import confirmMessageBox, single_timer_runner, gifPlayer
from uiUtils.guiBackend import GUIBackend

class Common_Function_UI:
    def __init__(self):
        """Description of the code"""

        # self.ui = ui

    def __show_saved_massage__(self, is_saved, save_msg, gif_player):
        if is_saved:
            self.__show_is_saving__(save_msg, gif_player)
            single_timer_runner(400, lambda: self.__show_saved__(save_msg, gif_player))
            
        else:
            GUIBackend.set_label_text(save_msg, "")
        
    def __show_is_saving__(self, save_msg, gif_player):
        GUIBackend.set_label_text(save_msg, "Saving Settings...")
        gif_player.show_and_start_animation()

    def __show_saved__(self, save_msg, gif_player):
        GUIBackend.set_label_text(save_msg, "")
        gif_player.hide_and_stop_animation()

    def save_state(self, is_saved, save_btn, cancel_btn, save_msg, gif_player):
        if not is_saved:
            GUIBackend.set_enable(save_btn)
            GUIBackend.set_enable(cancel_btn)
            self.__show_saved_massage__(is_saved, save_msg, gif_player)
        
        else:
            GUIBackend.set_disable(save_btn)
            GUIBackend.set_disable(cancel_btn)
            self.__show_saved_massage__(is_saved, save_msg, gif_player)
        
    def __create_event_func__(self, func, args):
        def event():
            func(*args)
        return event
    
    def show_confirm_box(Self, title, massage, buttons):
        cmb = confirmMessageBox(title, massage, buttons = buttons)
        return cmb.render()

    def set_message(self, label_name, text, level=1):
        """Show warning with time delay 2 second , all labels for show warning has been set here"""

        if text != None:
            if level == 1:
                label_name.setText(" " + text + " ")
                label_name.setStyleSheet(
                    "background-color:rgb(140, 140, 140);border-radius:2px;color:black"
                )

            QTimer.singleShot(10000, lambda: self.set_message(label_name, None))

        else:
            label_name.setText("")
            label_name.setStyleSheet("")

    def show_alert_window(self, title, message, need_confirm=False, level=1):
        """this function is used to create a confirm window
        :param title: _description_, defaults to 'Message'
        :type title: str, optional
        :param message: _description_, defaults to 'Message'
        :type message: str, optional
        :return: _description_
        :rtype: _type_
        """

        level = 0 if level < 0 or level > 2 else level

        # create message box
        alert_window = QtWidgets.QMessageBox()

        # icon
        if level == 0:
            alert_window.setIcon(QtWidgets.QMessageBox.Information)
        elif level == 1:
            alert_window.setIcon(QtWidgets.QMessageBox.Warning)
        elif level == 2:
            alert_window.setIcon(QtWidgets.QMessageBox.Critical)

        # Message and title
        alert_window.setText(message)
        alert_window.setWindowTitle(title)
        # buttons
        if not need_confirm:
            alert_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
            alert_window.button(QtWidgets.QMessageBox.Ok).setText("ok")
        else:
            alert_window.setStandardButtons(
                QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok
            )
            alert_window.button(QtWidgets.QMessageBox.Ok).setText("Yes")
            alert_window.button(QtWidgets.QMessageBox.Cancel).setText("Cancel")

        alert_window.setWindowFlags(
            QtCore.Qt.Dialog
            | QtCore.Qt.CustomizeWindowHint
            | QtCore.Qt.WindowTitleHint
            | QtCore.Qt.WindowCloseButtonHint
        )
        returnValue = alert_window.exec()

        if not need_confirm:
            return True if returnValue == QtWidgets.QMessageBox.Ok else True
        else:
            return True if returnValue == QtWidgets.QMessageBox.Ok else False
