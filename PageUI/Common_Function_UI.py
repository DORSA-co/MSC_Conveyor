from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
from PySide6 import QtWidgets, QtCore, QtGui
import cv2

class Common_Function_UI:
    def __init__(self):
        """Description of the code"""

        # self.ui = ui
        
    def __create_event_func__(self, func, args):
        def event():
            func(*args)
        return event
    
    
    def set_label_image(self, lbl: QtWidgets.QLabel, image) -> QtGui.QPixmap:

        if isinstance(image, str):
            image = cv2.imread(image)        

        #resie image to fix in label
        img_h, img_w = image.shape[:2]
        lbl_h, lbl_w = lbl.height(), lbl.width()
        
        scale = min(lbl_h/img_h, lbl_w/img_w)
        image = cv2.resize(image, None, fx= scale, fy=scale)

        #color image
        if len(image.shape)==3:
            #alpha channel image
            if image.shape[2] ==4:
                qformat=QtGui.QImage.Format_RGBA8888
            else:
                qformat=QtGui.QImage.Format_RGB888          

        #grayscale image
        if len(image.shape) == 2:
            qformat=QtGui.QImage.Format_Grayscale8

        img = QtGui.QImage(image.data,
            image.shape[1],
            image.shape[0], 
            image.strides[0], # <--- +++
            qformat)
        
        img = img.rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(img)
        lbl.setPixmap(pixmap)
        lbl.setAlignment(QtCore.Qt.AlignCenter)
        return pixmap
            

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
