from UIFiles.main_UI import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6 import QtGui

class Styler:

    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui

        self.shadow_buttons: list[QtWidgets.QPushButton] = [
            self.ui.save_camera_settings,
            self.ui.save_algorithm_settings
        ]

    def render(self,):
        self.__set_shadow_buttons()

    
    def __set_shadow_buttons(self, ):
        for btn in self.shadow_buttons:
            shadow  = QtWidgets.QGraphicsDropShadowEffect(btn)
            shadow.setBlurRadius(15)
            shadow.setOffset(3,3)
            shadow.setYOffset(3)
            shadow.setColor(QtGui.QColor(0,0,0,100))
            btn.setGraphicsEffect(shadow)