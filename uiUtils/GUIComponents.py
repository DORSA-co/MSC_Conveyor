import re

from PySide6 import QtWidgets, QtCore, QtGui
# import guiBackend
import PySide6.QtWidgets 

from Constants import Constant
from Constants import IconsPath

CODE_NAME_BUTTON_STYLE ={
    'normal': """ QPushButton{
                  min-width:100px;
                  background-color: rgb(150,150,150);
                }


            QPushButton:hover{
            background-color: rgb(50,50,50);
            }
            """,

    'active':
            """ QPushButton{
                  min-width:100px;
                  background-color: rgb(58, 209, 154);
                }


            QPushButton:hover{
            background-color: rgb(58, 209, 154);
            }
            """

}

TABEL_BUTTON_STYLE = """
    QPushButton{ 
        background-color: rgba(255,255,255,0);
        min-height:0px; min-width:0px; 
        width:auto;
        qproperty-iconSize: 24px;
        } 
    """

SIDEBAR_BUTTON_SELECTED_STYLE = """
    QPushButton{
        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #4C7EFF, stop: 0.029 #4C7EFF, stop: 0.03 rgba(120, 146, 223, 40), stop: 1 rgba(120, 146, 223, 40));
        }

"""

SIDEBAR_BUTTON_UNSELECTED_STYLE = """
    None

"""

MULTISTEP_SELECT_STYLE = """
    QPushButton{
        background-color: transparent;
        border:5px solid #4C7EFF;
        border-radius: 32px;
        min-width: 55px;
        max-width: 55px;
        min-height: 55px;
        max-height: 55px;
        font-size: 24px;
        color: rgb(20, 20, 20);
        font-weight: bold;
    }

    QPushButton:hover{
        border:5px solid #83A5FC;
    }
"""

MULTISTEP_UNSELECT_STYLE = """
    QPushButton{
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
    }

    QPushButton:hover{
        border:5px solid #BDBDBF;
    }
"""

REPORT_BUTTON_STYLE = """
QPushButton{
	min-height:30px;
    min-width:30px;
    max-height:30px;
    max-width:30px;
	border-radius:3px;
	color: rgb(255, 255, 255);
	background-color:rgb(54, 193, 142);

}

QPushButton:hover{
	color: rgb(255, 255, 255);
	background-color:rgb(40, 144, 106);
}

"""

TABLE_BUTTON_STYLE = """
QPushButton{
	min-height:30px;
    min-width:100px;
    max-height:30px;
    max-width:100px;
	border-radius:3px;
	color: rgb(255, 255, 255);
	background-color:rgb(54, 193, 142);

}

QPushButton:hover{
	color: rgb(255, 255, 255);
	background-color:rgb(40, 144, 106);
}
"""

CONFIRMBOX_STYLESHEET = """
   QMessageBox{ 
        background-color: #ffffff;

    }
    
    QPushButton{
        border: none;
        font-weight: bold;
        color: #ffffff;
        background-color:rgb(6, 76, 130);
        min-height: 25px;
        border-radius: 5px;
        min-width:100px;
        font-size:12px;
	
        }

    QPushButton:hover{
	    background-color:rgb(22, 38, 76);
    }
"""

COMPARE_COMBOBOXE = """
                    QComboBox
{
	border:2px solid rgb(6, 76, 130);
    border-radius: 1px;
    padding: 3px;
	min-width:0xp;
	min-height: 0px;
    max-height: 18px;
	font-size: 14px;
}

QComboBox:enabled{
color: rgb(50, 50, 50);
}

QComboBox::down-arrow
{   
	image: url(:/assets/icons/icons8-downtriangle-48.png);
	width: 8px;
    height: 8px;
     background-color: rgb(6, 76, 130);
	 min-width: 0px;
     max-height: 17px;

}
        """

TABLE_SPINBOX = """
QSpinBox, QDoubleSpinBox  
{
	border:2px solid rgb(6, 76, 130);
    border-radius: 3px;
    padding: 2px;
    min-width:0xp;
	min-height: 0px;
    max-height: 20px;
	font-size: 12px;
}

QSpinBox:enabled, QDoubleSpinBox:enabled{
color: rgb(50, 50, 50);
}


QSpinBox::up-arrow, QDoubleSpinBox::up-arrow, QSpinBox::down-arrow ,  QDoubleSpinBox::down-arrow
{   
	image: url(noimg);
	width: 0px;
    height: 0px;

}


QSpinBox::up-button,
QSpinBox::down-button,
QDoubleSpinBox::up-button,
QDoubleSpinBox::down-button   {
    subcontrol-origin: border;
	background-color:rgb(6, 76, 130);
    width: 0px;
}


QSpinBox::up-button:disabled ,
QSpinBox::down-button:disabled ,
QDoubleSpinBox::up-button:disabled ,
QDoubleSpinBox::down-button:disabled    {
    subcontrol-origin: border;
	background-color:rgb(209, 209, 209);
    width: 0px;
}

QSpinBox:focus, QDoubleSpinBox:focus{
	background: rgb(241, 241, 241);
	/*selection-background-color: black;*/
}

"""


def take_closest(num, collection):
    return min(collection, key=lambda x: abs(x - num))


def single_timer_runner( t, func):
    """runs a function after a delay time

    Args:
        t (_type_): delay time in ms`
        func (_type_): function event after time finished
    """
    timer = QtCore.QTimer()
    timer.singleShot(t, func)


class Color:
    def __init__(self, color) -> None:
        if self.is_hex_color(color):
            self.hex_color = color
            self.rgb_color = self.hex2rgb(color)

        elif self.is_rgb_color(color):
            self.hex_color = self.rgb2hex(color)
            self.rgb_color = tuple(map(int, color.strip('()').split(', ')))

        else:
            raise "{color} is not a valid Hex or RGB color."

    def is_hex_color(self, color):
        """
        Check if the given color is a valid hexadecimal color code.
        """
        hex_color_pattern = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
        return re.match(hex_color_pattern, color) is not None

    def is_rgb_color(self, color):
        """
        Check if the given color is a valid RGB color in the format (x, y, z).
        """
        rgb_color_pattern = r'^\(\s*(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\s*\)$'
        match = re.match(rgb_color_pattern, color)
        if match:
            r, g, b = map(int, match.groups())
            return all(0 <= val <= 255 for val in [r, g, b])
        return False
        
    def rgb2hex(self, color):
        """
        Convert RGB to Hexadecimal color code.
        """
        if self.is_rgb_color(color):
            r, g, b = map(int, color.strip('()').split(', '))
            return '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)
        else:
            raise ValueError("Invalid RGB color format")

    def hex2rgb(self, color):
        """
        Convert Hexadecimal color code to RGB.
        """
        if self.is_hex_color(color):
            hexcolor = color.lstrip('#')
            if len(hexcolor) == 6:
                r, g, b = tuple(int(hexcolor[i:i+2], 16) for i in (0, 2, 4))
            elif len(hexcolor) == 3:
                r, g, b = tuple(int(hexcolor[i:i+1]*2, 16) for i in (0, 1, 2))
            else:
                raise ValueError("Invalid hex color format")
            return r, g, b
        else:
            raise ValueError("Invalid hex color format")


class AnimatedTextEdit(QtWidgets.QTextEdit):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0.0)

    def fade_in(self, duration=1000, callback=None):
        self.__fade(0.0, 1.0, duration, callback)

    def fade_out(self, duration=1000, callback=None):
        self.__fade(1.0, 0.0, duration,callback)

    def __fade(self, start_opacity, end_opacity, duration, callback=None):
        self.animation = QtCore.QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(duration)
        self.animation.setStartValue(start_opacity)
        self.animation.setEndValue(end_opacity)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.finished.connect(callback)
        self.animation.start()


class Message(AnimatedTextEdit):
    def __init__(self, parent, title:str, text:str, color:tuple, icon_path:str):
        super().__init__(text, parent)
        self.setEnabled(False)
        parent.layout().insertWidget(0, self)

        self.style = (
            """QTextEdit
            {{
                color: rgb(20, 20, 20);
                border: None;
                border-bottom: 2px solid rgba({0}, {1}, {2}, 255);
                background-color: rgba({0}, {1}, {2}, 50);
                padding-left: 55px;
                padding-top: 6px;
                padding-bottom: 3x;
                background-image: url({3});
                background-position: left center;
                background-repeat: no-repeat;
                min-height: 55px;
                max-height: 55px;
            }}

            QTextEdit:disabled
            {{
                color: rgb(20, 20, 20)
            }}"""

)

        self.style = self.style.replace('\n', '').replace('\t', '')

        self.set_style(color, icon_path)

        self.html_text = (
                """<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600; color:{};">{}</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{}</p></body></html>"""
            )
        
        self.set_message(title, text, color)

    def set_message(self, title:str, text:str, color:tuple):
        color_obj = Color(color)
        self.setHtml(self.html_text.format(color_obj.hex_color, title, text))

    def set_style(self, color, icon_path):
        color_obj = Color(color)
        self.setStyleSheet(
            self.style.format(color_obj.rgb_color[0], color_obj.rgb_color[1], color_obj.rgb_color[2], icon_path)
        )

    def show_message(self):
        self.fade_in(duration=Constant.MessagesAnimation.FADE_IN_DURATION)

        single_timer_runner(Constant.MessagesAnimation.MESSAGE_DURARTION, 
                                          lambda: self.fade_out(duration=Constant.MessagesAnimation.FADE_OUT_DURATION, callback=self.deleteLater)
        )


class SuccessMessage(Message):
    def __init__(self, parent, text=""):
        title = "SUCCESS"
        color = Constant.MessageColors.SUCCESS
        icon_path = IconsPath.IconsPath.SUCCESS_PATH
        super().__init__(parent, title, text, color, icon_path)


class WarningMessage(Message):
    def __init__(self, parent, text=""):
        title = "WARNING"
        color = Constant.MessageColors.WARNING
        icon_path = IconsPath.IconsPath.WARNING_PATH
        super().__init__(parent, title, text, color, icon_path)


class ErrorMessage(Message):
    def __init__(self, parent, text=""):
        title = "ERROR"
        color = Constant.MessageColors.ERROR
        icon_path = IconsPath.IconsPath.ERROR_PATH
        super().__init__(parent, title, text, color, icon_path)


class InfoMessage(Message):
    def __init__(self, parent, text=""):
        title = "INFO"
        color = Constant.MessageColors.INFO
        icon_path = IconsPath.IconsPath.INFO_PATH
        super().__init__(parent, title, text, color, icon_path)


class SwitchCircle(QtWidgets.QWidget):
    def __init__(self, parent, move_range: tuple, color, animation_curve, animation_duration):
        super().__init__(parent=parent)
        self.color = color
        self.move_range = move_range
        self.animation = QtCore.QPropertyAnimation(self, b"pos")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(animation_duration)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QColor(self.color))
        painter.drawEllipse(0, 0, 22, 22)
        painter.end()

    def set_color(self, value):
        self.color = value
        self.update()

    def mousePressEvent(self, event):
        self.animation.stop()
        self.oldX = event.globalX()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        delta = event.globalX() - self.oldX
        self.new_x = delta + self.x()
        if self.new_x < self.move_range[0]:
            self.new_x += (self.move_range[0] - self.new_x)
        if self.new_x > self.move_range[1]:
            self.new_x -= (self.new_x - self.move_range[1])
        self.move(self.new_x, self.y())
        self.oldX = event.globalX()
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        try:
            go_to = take_closest(self.new_x, self.move_range)
            if go_to == self.move_range[0]:
                self.animation.setStartValue(self.pos())
                self.animation.setEndValue(QtCore.QPoint(go_to, self.y()))
                self.animation.start()
                self.parent().setChecked(False)
            elif go_to == self.move_range[1]:
                self.animation.setStartValue(self.pos())
                self.animation.setEndValue(QtCore.QPoint(go_to, self.y()))
                self.animation.start()
                self.parent().setChecked(True)
        except AttributeError:
            pass
        return super().mouseReleaseEvent(event)


class SwitchControl(QtWidgets.QCheckBox):
    def __init__(self, parent=None, bg_color="#BF0000", circle_color="#E0E4EC", active_color="#00BF40",
                 animation_curve=QtCore.QEasingCurve.OutBounce, animation_duration=500, checked: bool = False,
                 change_cursor=True):
        if parent is None:
            super().__init__()
        else:
            super().__init__(parent=parent)
        self.setFixedSize(60, 28)
        if change_cursor:
            self.setCursor(QtCore.Qt.PointingHandCursor)
        self.bg_color = bg_color
        self.circle_color = circle_color
        self.animation_curve = animation_curve
        self.animation_duration = animation_duration
        self.__circle = SwitchCircle(self, (3, self.width() - 26), self.circle_color, self.animation_curve,
                                     self.animation_duration)
        self.__circle_position = 3
        self.active_color = active_color
        self.auto = False
        self.pos_on_press = None
        self.setChecked(checked)
        self.animation = QtCore.QPropertyAnimation(self.__circle, b"pos")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(animation_duration)

    def get_bg_color(self):
        return self.bg_color
    
    def setChecked(self, state):
        if state:
            self.__circle.move(self.width() - 26, 3)
            super().setChecked(True)
        elif not state:
            self.__circle.move(3, 3)
            super().setChecked(False)

    @QtCore.Slot(str)
    def set_bg_color(self, value):
        self.bg_color = value
        self.update()

    backgroundColor = QtCore.Property(str, get_bg_color, set_bg_color)

    def get_circle_color(self):
        return self.circle_color

    @QtCore.Slot(str)
    def set_circle_color(self, value):
        self.circle_color = value
        self.__circle.set_color(self.circle_color)
        self.update()

    circleBackgroundColor = QtCore.Property(str, get_circle_color, set_circle_color)

    def get_animation_duration(self):
        return self.animation_duration

    @QtCore.Slot(int)
    def set_animation_duration(self, value):
        self.animation_duration = value
        self.animation.setDuration(value)

    animationDuration = QtCore.Property(int, get_animation_duration, set_animation_duration)

    def get_active_color(self):
        return self.active_color

    @QtCore.Slot(str)
    def set_active_color(self, value):
        self.active_color = value
        self.update()

    activeColor = QtCore.Property(str, get_active_color, set_active_color)

    def start_animation(self, checked):
        self.animation.stop()
        self.animation.setStartValue(self.__circle.pos())
        if checked:
            self.animation.setEndValue(QtCore.QPoint(self.width() - 26, self.__circle.y()))
            self.setChecked(True)
        if not checked:
            self.animation.setEndValue(QtCore.QPoint(3, self.__circle.y()))
            self.setChecked(False)
        self.animation.start()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.NoPen)
        if not self.isChecked():
            painter.setBrush(QtGui.QColor(self.bg_color))
            painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)
        elif self.isChecked():
            painter.setBrush(QtGui.QColor(self.active_color))
            painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)

    def mousePressEvent(self, event):
        self.auto = True
        self.pos_on_press = event.globalPos()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.globalPos() != self.pos_on_press:
            self.auto = False
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.auto:
            self.auto = False
            self.start_animation(not self.isChecked())


class editButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(editButton, self).__init__(*a, **kw)
        self._icon_normal = QtGui.QIcon(IconsPath.IconsPath.EDIT_ICON)
        self._icon_over = QtGui.QIcon(IconsPath.IconsPath.EDIT_ICON_HOVER)
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)
        self.setCursor(QtCore.Qt.PointingHandCursor)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(editButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(editButton, self).enterEvent(event)


class deleteButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(deleteButton, self).__init__(*a, **kw)
        self._icon_normal = QtGui.QIcon(IconsPath.IconsPath.DELETE_ICON)
        self._icon_over = QtGui.QIcon(IconsPath.IconsPath.DELETE_ICON_HOVER)
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)
        self.setCursor(QtCore.Qt.PointingHandCursor)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(deleteButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(deleteButton, self).enterEvent(event)


class reportButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(reportButton, self).__init__(*a, **kw)
        self._icon = QtGui.QIcon(':/assets/icons/icons8-eye-white-50.png')
        self.setText("")
        self.setStyleSheet(REPORT_BUTTON_STYLE)
        self.setIcon(self._icon)


class tableButton(QtWidgets.QPushButton):

    def __init__(self, text='', *a, **kw):
        super(tableButton, self).__init__(*a, **kw)
        self.setStyleSheet(TABLE_BUTTON_STYLE)
        self.setText(text)


class tabelCheckbox(QtWidgets.QCheckBox):

    def __init__(self, *a, **kw):
        super(tabelCheckbox, self).__init__(*a, **kw)
        

    def set_size(self, w, h):
        self.setStyleSheet(f"""QCheckBox::indicator 
                                {{
                               width :{w}px;
                               height :{h}px;
                               }}""")

        #self.setMaximumWidth(h+5)
        #self.setMaximumWidth(w+5)


class compareComboBox(QtWidgets.QComboBox):

    def __init__(self, *a, **kw):
        super(compareComboBox, self).__init__(*a, **kw)

        self.insertItems(0, ['none', '>','>=', '<', '<=', '=='])
        self.setStyleSheet(COMPARE_COMBOBOXE)


class Input(QtWidgets.QLineEdit):

    def __init__(self, *a, **kw):
        super(Input, self).__init__(*a, **kw)

        

    def set_size(self, w, h):
        self.setStyleSheet(f"""QLineEdit 
                                {{
                               width :{w}px;
                               height :{h}px;

                               min-width :{w}px;
                               min-height :{h}px;

                               max-width :{w}px;
                               max-height :{h}px;
                               }}""")


class doubleSpinBoxTable(QtWidgets.QDoubleSpinBox):

    def __init__(self, *a, **kw):
        super(doubleSpinBoxTable, self).__init__(*a, **kw)
        self.setStyleSheet(TABLE_SPINBOX)
        

class LabelTable(QtWidgets.QLabel):
    clicked = QtCore.Signal()
    def __init__(self, *a, **kw):
        super(LabelTable, self).__init__(*a, **kw)
        self.setScaledContents(True)

    def mousePressEvent(self, event:QtCore.QEvent):        
        if event.type() == QtCore.QEvent.MouseButtonPress:
                self.clicked.emit()
  

    
    def set_size(self, h,w):
        guiBackend.set_max_size(self, h, w)
        guiBackend.set_min_size(self, h, w)


class inputTable(QtWidgets.QLineEdit):
    def __init__(self, *a, **kw):
        super(inputTable, self).__init__(*a, **kw)


class confirmMessageBox:
    def __init__(self, title, text, buttons, min_height=300, min_width=400, parent=None ):
        self.STANDARD_BUTTONS = {
            'yes': QtWidgets.QMessageBox.Yes,
            'no': QtWidgets.QMessageBox.No,
            'cancel': QtWidgets.QMessageBox.Cancel,
            'save': QtWidgets.QMessageBox.Save,
            'ok': QtWidgets.QMessageBox.Ok,
            'ignore': QtWidgets.QMessageBox.Ignore,
            

        }

        self.icon = QtGui.QIcon(':/assets/icons/icons8-question-blue-50.png')
        self.buttons = buttons

        text = text + " " * 100 + "\n"

        self.msg = QtWidgets.QMessageBox( text=text, parent=parent)
        self.msg.setWindowTitle(title)
        self.msg.setStyleSheet(CONFIRMBOX_STYLESHEET)
        self.msg.setWindowIcon(self.icon)
        #self.msg.setMinimumHeight(min_height)
        #self.msg.setStyleSheet("QLabel{ min-width:" + str(min_width) + " px; }" )
        #self.msg.setMinimumWidth(min_width)

        
        #---------------------------------------------------
        selected_buttons_obj = []
        for btn_name in buttons:
            btn = self.STANDARD_BUTTONS[btn_name]
            if isinstance(selected_buttons_obj, list):
                selected_buttons_obj = btn
            else:
                selected_buttons_obj = selected_buttons_obj | btn
        self.msg.setStandardButtons(selected_buttons_obj)
        #---------------------------------------------------

    def render(self) -> str:
        retval = self.msg.exec_()
        for btn_name in self.buttons:
            if self.STANDARD_BUTTONS[btn_name] == retval:
                return btn_name


class timerBuilder:

    def __init__(self, t, event_func) -> None:
        self.event_func = event_func
        self.t = t
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect( self.event_func)


    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect( self.event_func)
        self.timer.start(self.t)
    

    def stop(self, ):
        self.timer.stop()
        self.timer.deleteLater()


class singleAnimation:

    def __init__(self, obj ,atribute, time, key1, key2) -> None:
        
        self.key1 = key1
        self.key2 = key2
        self.time = time
        self.toggle_flag = True
        self.animation = QtCore.QPropertyAnimation(obj, atribute)
        self.animation.setDuration(time)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
    
    def reset(self,):
        self.animation.setDuration(1)
        self.animation.setStartValue(self.key1)
        self.animation.setEndValue(self.key1)
        self.animation.start()
        self.animation.setDuration(self.time)
        
    
    def forward( self ):
        self.toggle_flag = False
        self.animation.setStartValue(self.key1)
        self.animation.setEndValue(self.key2)
        self.animation.start()
        
    
    def backward(self):
        self.toggle_flag = True
        self.animation.setStartValue(self.key2)
        self.animation.setEndValue(self.key1)
        self.animation.start()
        


    def single_forward(self):
        if self.toggle_flag:
            self.forward()
            
        
    
    def single_backward(self,):
        if not self.toggle_flag:
            self.backward()
    
    
    def toggle(self,):
        if self.toggle_flag:
            self.forward()
        else:
            self.backward()


class gifPlayer:

    def __init__(self, label: QtWidgets.QLabel, gif_path: str) -> None:
        self.movie = QtGui.QMovie(gif_path)
        self.label = label
        self.label.setMovie(self.movie)

        self.max_w = self.label.maximumWidth()
        self.max_h = self.label.maximumHeight()
    
    def set_maxsize(self, max_h, max_w):
        if max_w is not None:
            self.max_w = max_w
        
        if max_h is not None:
            self.max_h = max_h


	# Start Animation
    def start_animation(self):
        self.movie.start()

    def show_and_start_animation(self,):
        self.label.setMaximumHeight(self.max_h)
        self.label.setMaximumWidth(self.max_w)

        self.start_animation()

	# Stop Animation(According to need)
    def stop_animation(self):
        pass
        #self.movie.startTimer()

    def hide_and_stop_animation(self,):
        self.label.setMaximumHeight(0)
        self.label.setMaximumWidth(0)

        self.stop_animation()


def selectDirectoryDialog():
    path = QtWidgets.QFileDialog.getExistingDirectory()
    return path


def selectSaveFile(file_name:str = 'All', file_extention:str='.*'):
    """opens a dialog file to select a file to save

    Args:
        file_name (str): an ideal name of file like 'Excel' 
        file_extention (str): file extention like '.xlsx'

    Returns:
        _type_: selected path
    """
    filter = f'{file_name} (*{file_extention})'
    path = QtWidgets.QFileDialog.getSaveFileName(filter=filter)
    return path


def selectFileDialog(file_name:str = 'All', file_extention:str='.*'):
    """opens a dialog file to select a file to save

    Args:
        file_name (str): an ideal name of file like 'Excel' 
        file_extention (str): file extention like '.xlsx'

    Returns:
        _type_: selected path
    """
    filter = f'{file_name} (*{file_extention})'
    path = QtWidgets.QFileDialog.getOpenFileName(filter=filter)
    return path


class overlayMassage(QtWidgets.QWidget):
    def __init__(self, 
                 text,
                 fill_overlay_color:tuple=(30, 30, 30, 200),
                 popup_bg:tuple=(0,0,0,0),
                 popup_card_size = (120,300),
                 font_size = 48,
                 text_color:tuple = (220,220,220), 
                 parent=None):
        
        super(overlayMassage, self).__init__()

        self.text = text
        self.popup_bg = QtGui.QColor(*popup_bg)
        self.overlay_color = fill_overlay_color
        self.fill_overlay_color = QtGui.QColor(*fill_overlay_color)
        self.popup_fillColor = QtGui.QColor(*popup_bg)
        self.popup_card_size = popup_card_size
        self.font_size = font_size
        self.text_color = text_color

        # make the window frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




    def paintEvent(self, event):
        # This method is, in practice, drawing the contents of
        # your window.

        # get current window size
        s = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
        qp.setBrush(self.fill_overlay_color)
        qp.drawRect(0, 0, s.width(), s.height())

        # drawpopup
        qp.setBrush(self.popup_bg)
        qp.setPen(self.popup_bg)
        popup_width = self.popup_card_size[0]
        popup_height = self.popup_card_size[1]
        ow = int(s.width()/2-popup_width/2)
        oh = int(s.height()/2-popup_height/2)
        qp.drawRoundedRect(ow, oh, popup_width, popup_height, 5, 5)

        font = QtGui.QFont()
        font.setPixelSize(self.font_size)
        font.setBold(True)
        qp.setFont(font)
        qp.setPen(QtGui.QColor(*self.text_color))
        tolw, tolh = 80, -5
        qp.drawText(ow + int(popup_width/2) - tolw, oh + int(popup_height/2) - tolh, self.text)

        qp.end()


    def show(self,):
        self.showMaximized()


