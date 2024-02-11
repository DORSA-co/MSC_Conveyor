from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from PySide6 import QtWidgets, QtCore, QtGui
import cv2

from uiUtils.GUIComponents import MessageBox, single_timer_runner, gifPlayer
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
    
    def show_confirm_box(Self, title, message, buttons, icon_type):
        cmb = MessageBox(title, message, buttons=buttons, icon_type=icon_type)
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

