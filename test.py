from PySide6.QtWidgets import QMessageBox
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui

CONFIRMBOX_STYLESHEET = """
QMessageBox{ 
    background-color: #E0E4EC;
    font: auto "Roboto";
    font-size: 16px;
}

QMessageBox QLabel#qt_msgbox_label {
    min-width: 400px;
}
"""

OK_BUTTUN_STYLE= """
QPushButton
{
    background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));
    color: rgba(255, 255, 255, 210);
    border-radius: 20px;
    min-width: 100;
    max-width: 100;
    min-height: 40;
    max-height: 40;
    font-size: 14px;
    font-weight: bold;
    icon: url('UIFiles/assets/icons/tick.png')
}

QPushButton:hover
{
    background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));
}

QPushButton:pressed
{
    padding-left: 5px;
    padding-top: 5px;
}
"""

YES_BUTTUN_STYLE= """
QPushButton
{
    background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));
    color: rgba(255, 255, 255, 210);
    border-radius: 20px;
    min-width: 100;
    max-width: 100;
    min-height: 40;
    max-height: 40;
    font-size: 14px;
    font-weight: bold;
    icon: url('UIFiles/assets/icons/tick.png')
}

QPushButton:hover
{
    background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));
}

QPushButton:pressed
{
    padding-left: 5px;
    padding-top: 5px;
}
"""

SAVE_BUTTUN_STYLE= """
QPushButton
{
    background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));
    color: rgba(255, 255, 255, 210);
    border-radius: 20px;
    min-width: 100;
    max-width: 100;
    min-height: 40;
    max-height: 40;
    font-size: 14px;
    font-weight: bold;
    icon: url('UIFiles/assets/icons/save_icon.png')
}

QPushButton:hover
{
    background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));
}

QPushButton:pressed
{
    padding-left: 5px;
    padding-top: 5px;
}
"""

CANCEL_BUTTUN_STYLE= """
QPushButton
{
    border: 2px solid  rgba(46, 76, 153, 255);
    color:  rgba(46, 76, 153, 255);
    border-radius: 18px;
    min-width: 100;
    max-width: 100;
    min-height: 36;
    max-height: 36;
    font-size: 14px;
    font-weight: bold;
    icon: url(UIFiles/assets/icons/cancel_icon.png);
}

QPushButton:hover
{
    border: 2px solid rgba(76, 126, 255, 255);
    color:  rgba(76, 126, 255, 255);
    icon: url(UIFiles/assets/icons/cancel_hover.png);
}

QPushButton:pressed
{
    padding-left: 5px;
    padding-top: 5px;
}
"""

NO_BUTTUN_STYLE= """
QPushButton
{
    border: 2px solid  rgba(46, 76, 153, 255);
    color:  rgba(46, 76, 153, 255);
    border-radius: 18px;
    min-width: 100;
    max-width: 100;
    min-height: 36;
    max-height: 36;
    font-size: 14px;
    font-weight: bold;
    icon: url(UIFiles/assets/icons/cancel_icon.png);
}

QPushButton:hover
{
    border: 2px solid rgba(76, 126, 255, 255);
    color:  rgba(76, 126, 255, 255);
    icon: url(UIFiles/assets/icons/cancel_hover.png);
}

QPushButton:pressed
{
    padding-left: 5px;
    padding-top: 5px;
}
"""

IGNORE_BUTTUN_STYLE= """
QPushButton
{
    border: 2px solid  rgba(46, 76, 153, 255);
    color:  rgba(46, 76, 153, 255);
    border-radius: 18px;
    min-width: 100;
    max-width: 100;
    min-height: 36;
    max-height: 36;
    font-size: 14px;
    font-weight: bold;
    icon: url();
}

QPushButton:hover
{
    border: 2px solid rgba(76, 126, 255, 255);
    color:  rgba(76, 126, 255, 255);
    icon: url();
}

QPushButton:pressed
{
    padding-left: 5px;
    padding-top: 5px;
}
"""

class MessageBox():
    def __init__(self, title, text, buttons, icon, parent=None):

        self.STANDARD_BUTTONS = {
            'yes': QtWidgets.QMessageBox.Yes,
            'no': QtWidgets.QMessageBox.No,
            'cancel': QtWidgets.QMessageBox.Cancel,
            'save': QtWidgets.QMessageBox.Save,
            'ok': QtWidgets.QMessageBox.Ok,
            'ignore': QtWidgets.QMessageBox.Ignore,
        }

        self.STANDARD_BUTTONS_STYLES = {
            'yes': YES_BUTTUN_STYLE,
            'no': NO_BUTTUN_STYLE,
            'cancel': CANCEL_BUTTUN_STYLE,
            'save': SAVE_BUTTUN_STYLE,
            'ignore': IGNORE_BUTTUN_STYLE,
            'ok': OK_BUTTUN_STYLE
        }

        self.buttons = buttons

        self.msg = QtWidgets.QMessageBox(parent=parent)
        self.msg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.msg.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.msg.setStyleSheet(CONFIRMBOX_STYLESHEET)
        self.msg.setMinimumSize(400, 200)

        self.icon = QtGui.QPixmap(icon)
        self.msg.setIconPixmap(self.icon)

        # self.msg.setText("{0} <br> {0}".format(title, text))

        html_text = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        /* Title style */
        .title {{
            color: rgb(20, 20, 20); /* Title color */
            font-size: 22px; /* Title font size */
            font-weight: bold;
        }}
        /* Text style */
        .text {{
            color: rgb(20, 20, 20);
            font-size: 16px; /* Text font size */
        }}
        </style>
        </head>
        <body>
        <p class="title">{0}</p>
        <p class="text">{1}</p>
        </body>
        </html>
        """
        self.msg.setTextFormat(QtCore.Qt.RichText)
        self.msg.setText(html_text.format(title, text))

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

        for btn_name in buttons:
            style = self.STANDARD_BUTTONS_STYLES[btn_name]
            btn = self.msg.button(self.STANDARD_BUTTONS[btn_name])
            btn.setStyleSheet(style)

    def render(self) -> str:
        retval = self.msg.exec_()
        for btn_name in self.buttons:
            if self.STANDARD_BUTTONS[btn_name] == retval:
                return btn_name

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    # Create and show the custom message box
    message_box = MessageBox(title='Test', text='Test message', buttons=['ok', 'cancel', 'yes', 'no', 'save', 'ignore'], icon='UIFiles/assets/icons/info_icon.png')
    message_box.render()
