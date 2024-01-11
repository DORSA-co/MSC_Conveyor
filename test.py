import functools
from PyQt5 import QtCore, QtGui, QtWidgets


def helper_function(widget, color):
    widget.setStyleSheet('''
                            background-color: transparent;
                            border:5px solid #7E84A2;
                            border-radius: 32px;
                            min-width: 55px;
                            max-width: 55px;
                            min-height: 55px;
                            max-height: 55px;
                            font-size: 24px;
                            color: rgb(20, 20, 20);
                            font-weight: bold;
                            border: 5px solid {}
                        '''.format(color.name()))

def apply_color_animation(widget, start_color, end_color, duration=1000):
    anim = QtCore.QVariantAnimation(
        widget,
        duration=duration,
        startValue=start_color,
        endValue=end_color,
        loopCount=1,
    )
    anim.valueChanged.connect(functools.partial(helper_function, widget))
    anim.start(QtCore.QAbstractAnimation.DeleteWhenStopped)


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.button = QtWidgets.QPushButton()

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.button)

        self.button.clicked.connect(self.handle_timeout)
        self.button.setStyleSheet('''
                                background-color: transparent;
                                border:5px solid #7E84A2;
                                border-radius: 32px;
                                min-width: 55px;
                                max-width: 55px;
                                min-height: 55px;
                                max-height: 55px;
                                font-size: 24px;
                                color: rgb(20, 20, 20);
                                font-weight: bold;
                            ''')

    def handle_timeout(self):
        apply_color_animation(
            self.button,
            QtGui.QColor("#7E84A2"),
            QtGui.QColor("#4C7EFF"),
            duration=1000,
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    w = Widget()
    w.show()
    sys.exit(app.exec_())