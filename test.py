import time

import sys
import os
sys.path.append(os.path.join('UIFiles', 'assets'))
sys.path.append('uiUtils')

from PySide6.QtWidgets import QApplication, QToolButton
from PySide6 import QtWidgets, QtCore, QtGui
from UIFiles.calendar import Ui_CalendarDialog
from uiUtils.guiBackend import GUIBackend

from Constants import Constant

class Calendar(QtWidgets.QDialog):
    def __init__(self) -> None:
        super(Calendar, self).__init__()

        self.ui = Ui_CalendarDialog()
        self.ui.setupUi(self)

        GUIBackend.set_win_frameless(self)
        GUIBackend.set_win_attribute(self, QtCore.Qt.WA_TranslucentBackground)

        GUIBackend.button_connector(self.ui.cancel_btn, self.close_win)
        GUIBackend.button_connector(self.ui.ok_btn, self.get_selected_date)

        self.move_refresh_time = 0
        self.offset = None

        self.selected_date = None

        self._center()
        self._styler()

    def _center(self):
        primary_screen = QApplication.primaryScreen()

        if primary_screen:
            screen_geometry = primary_screen.geometry()

            center_point = screen_geometry.center()

            self.move(center_point.x() - self.frameGeometry().width() // 2,
                      center_point.y() - self.frameGeometry().height() // 2)
            
    def _styler(self):
        self._style_next_prev()
        self._style_today()
            
    def _style_next_prev(self):
        prev_month_button = self.ui.calendar.findChild(QToolButton, 'qt_calendar_prevmonth')
        next_month_button = self.ui.calendar.findChild(QToolButton, 'qt_calendar_nextmonth')

        prev_month_button.setIcon(QtGui.QIcon(':/icons/icons/prev_gray.png'))
        next_month_button.setIcon(QtGui.QIcon(':/icons/icons/next_gray.png'))

        prev_month_button.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))
        next_month_button.setCursor(QtGui.QCursor(QtGui.Qt.PointingHandCursor))

    def _style_today(self):
        today_format = QtGui.QTextCharFormat()
        today_format.setForeground(QtGui.QColor('#4C7EFF'))

        self.ui.calendar.setDateTextFormat(QtCore.QDate.currentDate(), today_format)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
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

    def show_win(self):
        result = self.exec_()
        if result == QtWidgets.QDialog.Accepted:
            return self.selected_date
        else:
            return None

    def close_win(self):
        GUIBackend.close_window(self)
        self.reject()

    def get_selected_date(self):
        self.selected_date = self.ui.calendar.selectedDate()
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_ui = Calendar()
    ret = main_ui.show_win()
    print(ret)