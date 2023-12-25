# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QComboBox, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1282, 910)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"/******************************************************************************************/\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	color: white;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	background-color: rgb(12, 53, 106);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"/******************************************************************************************/\n"
"\n"
"QGroupBox\n"
"{\n"
"	font-size: 18px;	\n"
"	border: 1px solid #a0a0a0;\n"
"	\n"
"	\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::indicator:checked {\n"
"	image: url(:/icons/icon/icons8-check-48.png);\n"
"	margin:0px;\n"
"padding:0px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"	width: 21px;\n"
"    height: 21px;\n"
"	border:1px solid rgb(11, 50, 99);\n"
"	\n"
"}\n"
"\n"
"/************************************"
                        "******************************************************/\n"
"QLineEdit\n"
"{\n"
"	border:2px solid rgb(6, 76, 130);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"    min-width: 6em;\n"
"	min-height: 35px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
"/******************************************************************************************/\n"
"\n"
"QSpinBox, QDoubleSpinBox  \n"
"{\n"
"	border:1px solid rgb(12, 53, 106);\n"
"    border-radius: 0px;\n"
"    padding: 1px 18px 1px 8px;\n"
"	font-size: 18px;\n"
"	min-height: 30px;\n"
"	min-width: 100px;\n"
"}\n"
"\n"
"\n"
"QSpinBox:disabled ,\n"
"QDoubleSpinBox:disabled \n"
"{\n"
"	border:2px solid rgb(200, 200, 200);\n"
"	color:(210, 210, 210);\n"
"}\n"
"\n"
"\n"
"\n"
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow\n"
"{   \n"
"	image: url(:/icons/icon/icons8-plus-white-48.png);\n"
"	width: 24px;\n"
"	height: 24px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-arrow ,  QDoubleSpinBox::down-arrow\n"
"{   \n"
"	image: url(:/icons/icon/icons8-minus-whi"
                        "te-48.png);\n"
"	width: 24px;\n"
"	height: 24px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"	border:none;\n"
"    min-width:36px;\n"
"    min-height: 36px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: right;\n"
"    top: 0px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"    min-width:36px;\n"
"    min-height: 36px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left;\n"
"    top: 0px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button   {\n"
"	background-color: #0c356a;\n"
"	border-bottom:1px solid #fff;\n"
"	\n"
"	\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled ,\n"
"QSpinBox::down-button:disabled ,\n"
"QDoubleSpinBox::up-button:disabled ,\n"
"QDoubleSpinBox::down-button:disabled    {\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(209, 209, 209);\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus{\n"
"	background: rgb(24"
                        "1, 241, 241);\n"
"	/*selection-background-color: black;*/\n"
"}\n"
"\n"
"\n"
"\n"
"/*********************************************************************************************/\n"
"QComboBox\n"
"{\n"
"	border:1px solid rgb(12, 53, 106);\n"
"    border-radius: 0px;\n"
"    padding: 1px 18px 1px 8px;\n"
"	min-height: 30px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QComboBox:enabled{\n"
"color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QComboBox:disabled\n"
"{\n"
"	border:2px solid rgb(210, 210, 210);\n"
"	color:(210, 210, 210);\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{   \n"
"	image: url(:/icons/icon/icons8-down-white-48.png);\n"
"	width: 24px;\n"
"    height: 24px;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down:button{\n"
"	width: 36px;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	 background-color: rgb(12, 53, 106);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	 \n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled \n"
"{\n"
"	 background-color: rgb(210, 210, 210);\n"
"	 min-wi"
                        "dth: 30px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"	color: #202020;\n"
"	background-color:#ffffff;\n"
"    /*selection-background-color: rgb(6, 76, 130);*/\n"
"	selection-color: rgb(12, 53, 106);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    border: none;\n"
"	height:30px;\n"
"}\n"
"\n"
"/*****************************************************************************************/\n"
"\n"
"QDateEdit\n"
"{\n"
"	border:2px solid rgb(12, 52, 105);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"	min-height: 30px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
"QDateEdit:disabled ,\n"
"QDateEdit:disabled \n"
"{\n"
"	border:2px solid rgb(200, 200, 200);\n"
"}\n"
"\n"
"\n"
"\n"
"QDateEdit::up-arrow\n"
"{   \n"
"	image: url(:/icons/icon/icons8-uptriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"QDateEdit::down-arrow \n"
"{   \n"
"	image: url(:/icons/icon/icons8-downtriangle-48.png);\n"
"	width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
""
                        "\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-button\n"
"{\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(12, 52, 105);\n"
"    width: 34px;\n"
"}\n"
"\n"
"\n"
"QDateEdit::up-button:disabled ,\n"
"QDateEdit::down-button:disabled\n"
"    {\n"
"    subcontrol-origin: border;\n"
"	background-color:rgb(209, 209, 209);\n"
"    width: 30px;\n"
"}\n"
"\n"
"QDateEdit:focus\n"
"{\n"
"	background: rgb(241, 241, 241);\n"
"	/*selection-background-color: black;*/\n"
"}\n"
"/*****************************************************************************************/")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setCursor(QCursor(Qt.ArrowCursor))
        self.header.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"}\n"
"\n"
"")
        self.header.setFrameShape(QFrame.WinPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.header)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(105, 50))
        self.label.setPixmap(QPixmap(u"icons/whitew.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(-5)

        self.horizontalLayout_9.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(371, 300))
        self.label_5.setStyleSheet(u"font-size:24px;\n"
"color: white;\n"
"font: 20pt \"Mongolian Baiti\";\n"
"")
        self.label_5.setMargin(-1)

        self.horizontalLayout_9.addWidget(self.label_5)


        self.horizontalLayout_4.addWidget(self.frame_13, 0, Qt.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.frame_27 = QFrame(self.header)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.logined_username_lbl = QLabel(self.frame_27)
        self.logined_username_lbl.setObjectName(u"logined_username_lbl")
        self.logined_username_lbl.setStyleSheet(u"color:#ffffff;")

        self.horizontalLayout_20.addWidget(self.logined_username_lbl)

        self.login_logout_btn = QPushButton(self.frame_27)
        self.login_logout_btn.setObjectName(u"login_logout_btn")
        self.login_logout_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icon/icons8-user-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_logout_btn.setIcon(icon)
        self.login_logout_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_20.addWidget(self.login_logout_btn)


        self.horizontalLayout_4.addWidget(self.frame_27)

        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(500, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(600, 600))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.minimize_btn = QPushButton(self.frame_12)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background: #a3a3a3;\n"
" }")
        icon1 = QIcon()
        icon1.addFile(u":/general_icons/general_incons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.frame_12)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background: #a3a3a3;\n"
" }")
        icon2 = QIcon()
        icon2.addFile(u":/general_icons/general_incons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.frame_12)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setMouseTracking(True)
        self.close_btn.setTabletTracking(True)
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #F70000;\n"
" }")
        icon3 = QIcon()
        icon3.addFile(u":/general_icons/general_incons/icons8-close-20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)

        self.horizontalLayout_8.addWidget(self.close_btn)


        self.horizontalLayout_3.addWidget(self.frame_12)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.header)

        self.middle = QFrame(self.centralwidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMaximumSize(QSize(16777215, 16777215))
        self.middle.setStyleSheet(u"")
        self.middle.setFrameShape(QFrame.NoFrame)
        self.middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.middle)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.middle)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(104, 0))
        self.frame_43.setMaximumSize(QSize(124, 16777215))
        self.frame_43.setStyleSheet(u"background-color: rgb(12, 53, 106);")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Sunken)
        self.frame_43.setLineWidth(3)
        self.verticalLayout_36 = QVBoxLayout(self.frame_43)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(19, 10, 22, 10)
        self.verticalSpacer_2 = QSpacerItem(10, 36, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_36.addItem(self.verticalSpacer_2)

        self.frame_19 = QFrame(self.frame_43)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(50, 50))
        self.frame_19.setBaseSize(QSize(10, 10))
        self.frame_19.setStyleSheet(u"background-color:rgb(140, 140, 140)")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setLineWidth(4)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_36.addWidget(self.frame_19)

        self.LiveDetectionBT = QPushButton(self.frame_43)
        self.LiveDetectionBT.setObjectName(u"LiveDetectionBT")
        self.LiveDetectionBT.setMaximumSize(QSize(59, 57))
        self.LiveDetectionBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.LiveDetectionBT.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    background-color:#F1F0E8;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../icons/camera_connection.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LiveDetectionBT.setIcon(icon4)
        self.LiveDetectionBT.setIconSize(QSize(51, 51))

        self.verticalLayout_36.addWidget(self.LiveDetectionBT, 0, Qt.AlignHCenter)

        self.ReportConnectionBT = QPushButton(self.frame_43)
        self.ReportConnectionBT.setObjectName(u"ReportConnectionBT")
        self.ReportConnectionBT.setMaximumSize(QSize(60, 60))
        self.ReportConnectionBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.ReportConnectionBT.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"    background-color:#F1F0E8;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../icons/monitor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ReportConnectionBT.setIcon(icon5)
        self.ReportConnectionBT.setIconSize(QSize(51, 51))

        self.verticalLayout_36.addWidget(self.ReportConnectionBT, 0, Qt.AlignHCenter)

        self.HelpConnectionBT = QPushButton(self.frame_43)
        self.HelpConnectionBT.setObjectName(u"HelpConnectionBT")
        self.HelpConnectionBT.setMaximumSize(QSize(60, 60))
        self.HelpConnectionBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.HelpConnectionBT.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"   background-color:#F1F0E8;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../icons/Capture-calib.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpConnectionBT.setIcon(icon6)
        self.HelpConnectionBT.setIconSize(QSize(51, 51))

        self.verticalLayout_36.addWidget(self.HelpConnectionBT, 0, Qt.AlignHCenter)

        self.SettingBT = QPushButton(self.frame_43)
        self.SettingBT.setObjectName(u"SettingBT")
        self.SettingBT.setMaximumSize(QSize(60, 60))
        self.SettingBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.SettingBT.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"   background-color:#F1F0E8;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingBT.setIcon(icon7)
        self.SettingBT.setIconSize(QSize(51, 51))

        self.verticalLayout_36.addWidget(self.SettingBT)

        self.usersBtn = QPushButton(self.frame_43)
        self.usersBtn.setObjectName(u"usersBtn")
        self.usersBtn.setMaximumSize(QSize(60, 60))
        self.usersBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.usersBtn.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"   background-color:#F1F0E8;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        self.usersBtn.setIcon(icon7)
        self.usersBtn.setIconSize(QSize(51, 51))

        self.verticalLayout_36.addWidget(self.usersBtn)

        self.AboutBT = QPushButton(self.frame_43)
        self.AboutBT.setObjectName(u"AboutBT")
        self.AboutBT.setMaximumSize(QSize(60, 60))
        self.AboutBT.setCursor(QCursor(Qt.PointingHandCursor))
        self.AboutBT.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"   background-color:#F1F0E8;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        self.AboutBT.setIcon(icon6)
        self.AboutBT.setIconSize(QSize(51, 51))

        self.verticalLayout_36.addWidget(self.AboutBT)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_4)


        self.horizontalLayout_27.addWidget(self.frame_43)

        self.main_frame = QFrame(self.middle)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(1, 1))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pages_stackwgt = QStackedWidget(self.main_frame)
        self.pages_stackwgt.setObjectName(u"pages_stackwgt")
        self.pages_stackwgt.setStyleSheet(u"#Live_View_Page,\n"
"#Help_Page,\n"
"#Report_Page,\n"
"#Setting_Page\n"
"{\n"
"background-color:#ffffff;\n"
"\n"
"}")
        self.pages_stackwgt.setFrameShape(QFrame.NoFrame)
        self.pages_stackwgt.setFrameShadow(QFrame.Plain)
        self.pages_stackwgt.setLineWidth(3)
        self.Live_View_Page = QWidget()
        self.Live_View_Page.setObjectName(u"Live_View_Page")
        self.horizontalLayout_7 = QHBoxLayout(self.Live_View_Page)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, -1, -1)
        self.frame_6 = QFrame(self.Live_View_Page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(11, 7, 11, 21)
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(8, 0, 0, 0)
        self.frame_62 = QFrame(self.frame_11)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(260, 404))
        self.frame_62.setMaximumSize(QSize(120, 16777215))
        self.frame_62.setStyleSheet(u"QLabel{\n"
"	font-size: 16px;\n"
"	border: no\n"
"}")
        self.frame_62.setFrameShape(QFrame.Panel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_62)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, -1, -1)
        self.groupBox_7 = QGroupBox(self.frame_62)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 200))
        self.groupBox_7.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_7.setStyleSheet(u"QLabel{\n"
"	font-size: 16px;\n"
"	border: no\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 50, -1, -1)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setVerticalSpacing(20)
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)

        self.Laser_Connection_2 = QLabel(self.groupBox_7)
        self.Laser_Connection_2.setObjectName(u"Laser_Connection_2")
        self.Laser_Connection_2.setMinimumSize(QSize(25, 25))
        self.Laser_Connection_2.setMaximumSize(QSize(25, 25))
        self.Laser_Connection_2.setStyleSheet(u"QLabel{\n"
"	\n"
"background-color:rgb(48, 163, 13);\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_5.addWidget(self.Laser_Connection_2, 2, 1, 1, 1)

        self.Laser_Connection_Check = QLabel(self.groupBox_7)
        self.Laser_Connection_Check.setObjectName(u"Laser_Connection_Check")
        self.Laser_Connection_Check.setMinimumSize(QSize(25, 25))
        self.Laser_Connection_Check.setMaximumSize(QSize(25, 25))
        self.Laser_Connection_Check.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(48, 163, 13);\n"
"}")

        self.gridLayout_5.addWidget(self.Laser_Connection_Check, 0, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_30, 4, 0, 1, 1)

        self.Laser_Connection_3 = QLabel(self.groupBox_7)
        self.Laser_Connection_3.setObjectName(u"Laser_Connection_3")
        self.Laser_Connection_3.setMinimumSize(QSize(25, 25))
        self.Laser_Connection_3.setMaximumSize(QSize(25, 25))
        self.Laser_Connection_3.setStyleSheet(u"QLabel{\n"
"	\n"
"background-color:rgb(48, 163, 13);\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_5.addWidget(self.Laser_Connection_3, 3, 1, 1, 1)

        self.Laser_Connection_4 = QLabel(self.groupBox_7)
        self.Laser_Connection_4.setObjectName(u"Laser_Connection_4")
        self.Laser_Connection_4.setMinimumSize(QSize(25, 25))
        self.Laser_Connection_4.setMaximumSize(QSize(25, 25))
        self.Laser_Connection_4.setStyleSheet(u"QLabel{\n"
"	\n"
"background-color:rgb(48, 163, 13);\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_5.addWidget(self.Laser_Connection_4, 4, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 20))
        self.label_29.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_29, 3, 0, 1, 1)

        self.label_60 = QLabel(self.groupBox_7)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_60, 1, 0, 1, 1)

        self.label_26 = QLabel(self.groupBox_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_26, 0, 0, 1, 1)

        self.Laser_Connection = QLabel(self.groupBox_7)
        self.Laser_Connection.setObjectName(u"Laser_Connection")
        self.Laser_Connection.setMinimumSize(QSize(25, 25))
        self.Laser_Connection.setMaximumSize(QSize(25, 25))
        self.Laser_Connection.setStyleSheet(u"QLabel{\n"
"	\n"
"background-color:rgb(48, 163, 13);\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_5.addWidget(self.Laser_Connection, 1, 1, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_5)


        self.verticalLayout_17.addWidget(self.groupBox_7)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_14)

        self.groupBox_9 = QGroupBox(self.frame_62)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 120))
        self.groupBox_9.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_9.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setVerticalSpacing(20)
        self.gridLayout_6.setContentsMargins(-1, 39, -1, -1)
        self.Not_Critical_live_view = QLabel(self.groupBox_9)
        self.Not_Critical_live_view.setObjectName(u"Not_Critical_live_view")
        self.Not_Critical_live_view.setMinimumSize(QSize(20, 20))
        self.Not_Critical_live_view.setMaximumSize(QSize(50, 20))
        self.Not_Critical_live_view.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(48, 163, 13);\n"
"}")

        self.gridLayout_6.addWidget(self.Not_Critical_live_view, 1, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox_9)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_35, 0, 0, 1, 1)

        self.Critical_live_view = QLabel(self.groupBox_9)
        self.Critical_live_view.setObjectName(u"Critical_live_view")
        self.Critical_live_view.setMinimumSize(QSize(20, 20))
        self.Critical_live_view.setMaximumSize(QSize(50, 20))
        self.Critical_live_view.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(48, 163, 13);\n"
"}")

        self.gridLayout_6.addWidget(self.Critical_live_view, 0, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_32, 1, 0, 1, 1)

        self.label_41 = QLabel(self.groupBox_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_41, 2, 0, 1, 1)

        self.Normal_live_view = QLabel(self.groupBox_9)
        self.Normal_live_view.setObjectName(u"Normal_live_view")
        self.Normal_live_view.setMinimumSize(QSize(20, 20))
        self.Normal_live_view.setMaximumSize(QSize(50, 20))
        self.Normal_live_view.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(48, 163, 13);\n"
"}")

        self.gridLayout_6.addWidget(self.Normal_live_view, 2, 1, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_6)


        self.verticalLayout_17.addWidget(self.groupBox_9)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_17)

        self.groupBox_4 = QGroupBox(self.frame_62)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 200))
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.Message_LiveView = QLabel(self.groupBox_4)
        self.Message_LiveView.setObjectName(u"Message_LiveView")
        self.Message_LiveView.setMinimumSize(QSize(300, 0))
        self.Message_LiveView.setMaximumSize(QSize(400, 16777215))
        self.Message_LiveView.setFrameShape(QFrame.Box)
        self.Message_LiveView.setFrameShadow(QFrame.Raised)
        self.Message_LiveView.setScaledContents(True)
        self.Message_LiveView.setAlignment(Qt.AlignCenter)
        self.Message_LiveView.setWordWrap(True)
        self.Message_LiveView.setMargin(4)
        self.Message_LiveView.setIndent(100)

        self.verticalLayout_38.addWidget(self.Message_LiveView)


        self.verticalLayout_17.addWidget(self.groupBox_4)


        self.horizontalLayout_56.addWidget(self.frame_62)

        self.frame_44 = QFrame(self.frame_11)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_44)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.frame_9 = QFrame(self.frame_44)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 99))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.frame_9.setLineWidth(3)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(16, 13, 9, 9)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(177, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_25.addWidget(self.frame_10)

        self.Stop_connection = QPushButton(self.frame_9)
        self.Stop_connection.setObjectName(u"Stop_connection")
        self.Stop_connection.setMaximumSize(QSize(80, 30))
        self.Stop_connection.setBaseSize(QSize(70, 30))
        self.Stop_connection.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"    background-color:#F1F0E8;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../icons/camera_connected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop_connection.setIcon(icon8)
        self.Stop_connection.setIconSize(QSize(50, 50))

        self.horizontalLayout_25.addWidget(self.Stop_connection)

        self.Camera_connection = QPushButton(self.frame_9)
        self.Camera_connection.setObjectName(u"Camera_connection")
        self.Camera_connection.setMaximumSize(QSize(80, 30))
        self.Camera_connection.setBaseSize(QSize(70, 30))
        self.Camera_connection.setCursor(QCursor(Qt.PointingHandCursor))
        self.Camera_connection.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"    background-color:#F1F0E8;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../icons/camera_disconnected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Camera_connection.setIcon(icon9)
        self.Camera_connection.setIconSize(QSize(50, 50))

        self.horizontalLayout_25.addWidget(self.Camera_connection)

        self.live = QPushButton(self.frame_9)
        self.live.setObjectName(u"live")
        self.live.setMaximumSize(QSize(70, 30))
        self.live.setCursor(QCursor(Qt.PointingHandCursor))
        self.live.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"    background-color:#F1F0E8;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"../icons/Live00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.live.setIcon(icon10)
        self.live.setIconSize(QSize(60, 60))

        self.horizontalLayout_25.addWidget(self.live)

        self.Stop = QPushButton(self.frame_9)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setToolTipDuration(-1)
        self.Stop.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"    background-color:#F1F0E8;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"../icons/stop-button2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop.setIcon(icon11)
        self.Stop.setIconSize(QSize(29, 26))

        self.horizontalLayout_25.addWidget(self.Stop)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(160, 100))
        self.label_2.setStyleSheet(u"font-size:30px;\n"
"color: white;\n"
"font: 23pt \"Mongolian Baiti\";")

        self.horizontalLayout_25.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.tabWidget = QTabWidget(self.frame_44)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_37 = QVBoxLayout(self.tab)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.Showlive = QLabel(self.tab)
        self.Showlive.setObjectName(u"Showlive")
        self.Showlive.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Showlive.sizePolicy().hasHeightForWidth())
        self.Showlive.setSizePolicy(sizePolicy1)
        self.Showlive.setMinimumSize(QSize(0, 0))
        self.Showlive.setMaximumSize(QSize(16777215, 16777215))
        self.Showlive.setLayoutDirection(Qt.LeftToRight)
        self.Showlive.setAutoFillBackground(False)
        self.Showlive.setStyleSheet(u"")
        self.Showlive.setFrameShape(QFrame.Panel)
        self.Showlive.setFrameShadow(QFrame.Raised)
        self.Showlive.setLineWidth(1)
        self.Showlive.setTextFormat(Qt.PlainText)
        self.Showlive.setScaledContents(True)
        self.Showlive.setAlignment(Qt.AlignCenter)
        self.Showlive.setWordWrap(False)
        self.Showlive.setOpenExternalLinks(False)

        self.verticalLayout_37.addWidget(self.Showlive)

        self.frame_79 = QFrame(self.tab)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(0, 200))
        self.frame_79.setMaximumSize(QSize(16777215, 16777215))
        self.frame_79.setFrameShape(QFrame.NoFrame)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_79)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_25 = QFrame(self.frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setStyleSheet(u"background-color:#0C356A;\n"
"border-radius:5px;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_20 = QLabel(self.frame_25)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(250, 16777215))
        self.label_20.setStyleSheet(u"font-size:18px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Mongolian Baiti\";")

        self.horizontalLayout_24.addWidget(self.label_20)


        self.verticalLayout_7.addWidget(self.frame_25)

        self.frame_58 = QFrame(self.frame)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"border: 3px solid back")
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_48 = QVBoxLayout(self.frame_58)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Depth = QLabel(self.frame_58)
        self.Depth.setObjectName(u"Depth")
        self.Depth.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.Depth.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Depth, 1, 1, 1, 1)

        self.label_25 = QLabel(self.frame_58)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_33 = QLabel(self.frame_58)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_33, 0, 0, 1, 1)

        self.Width = QLabel(self.frame_58)
        self.Width.setObjectName(u"Width")
        self.Width.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.Width.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Width, 2, 1, 1, 1)

        self.Length = QLabel(self.frame_58)
        self.Length.setObjectName(u"Length")
        self.Length.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.Length.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Length, 0, 1, 1, 1)

        self.label_Width = QLabel(self.frame_58)
        self.label_Width.setObjectName(u"label_Width")
        self.label_Width.setStyleSheet(u"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.label_Width.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_Width, 2, 0, 1, 1)


        self.verticalLayout_48.addLayout(self.gridLayout_3)


        self.verticalLayout_7.addWidget(self.frame_58)


        self.horizontalLayout_26.addWidget(self.frame)

        self.line_2 = QFrame(self.frame_79)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_26.addWidget(self.line_2)

        self.frame_16 = QFrame(self.frame_79)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.verticalLayout_22 = QVBoxLayout(self.frame_16)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_57 = QFrame(self.frame_16)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 50))
        self.frame_57.setStyleSheet(u"background-color:#0C356A;\n"
"font-size:18px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_22 = QLabel(self.frame_57)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(250, 16777215))
        self.label_22.setStyleSheet(u"font: 18pt \"Mongolian Baiti\";")

        self.horizontalLayout_2.addWidget(self.label_22)


        self.verticalLayout_22.addWidget(self.frame_57)

        self.frame_59 = QFrame(self.frame_16)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"border: 3px solid back")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Total_Number_Defect = QLabel(self.frame_59)
        self.Total_Number_Defect.setObjectName(u"Total_Number_Defect")
        self.Total_Number_Defect.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.Total_Number_Defect.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Total_Number_Defect, 0, 1, 1, 1)

        self.Total_Number_Critical_defect = QLabel(self.frame_59)
        self.Total_Number_Critical_defect.setObjectName(u"Total_Number_Critical_defect")
        self.Total_Number_Critical_defect.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.Total_Number_Critical_defect.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Total_Number_Critical_defect, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_59)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 16pt \"Mongolian Baiti\";\n"
"border: no")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_59)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 16pt \"Mongolian Baiti\";\n"
"border: no")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)


        self.horizontalLayout_15.addLayout(self.gridLayout)


        self.verticalLayout_22.addWidget(self.frame_59)


        self.horizontalLayout_26.addWidget(self.frame_16)


        self.verticalLayout_37.addWidget(self.frame_79)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_39 = QVBoxLayout(self.tab_2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.live_thickness_image = QLabel(self.tab_2)
        self.live_thickness_image.setObjectName(u"live_thickness_image")

        self.verticalLayout_39.addWidget(self.live_thickness_image)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_15.addWidget(self.tabWidget)


        self.horizontalLayout_56.addWidget(self.frame_44)


        self.verticalLayout_9.addWidget(self.frame_11)


        self.horizontalLayout_7.addWidget(self.frame_6)

        self.pages_stackwgt.addWidget(self.Live_View_Page)
        self.defect_tab = QWidget()
        self.defect_tab.setObjectName(u"defect_tab")
        self.horizontalLayout = QHBoxLayout(self.defect_tab)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.frame_29 = QFrame(self.defect_tab)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.frame_29)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(1, 1, 1, 21)
        self.frame_81 = QFrame(self.frame_29)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 100))
        self.frame_81.setMaximumSize(QSize(16777215, 16777215))
        self.frame_81.setTabletTracking(False)
        self.frame_81.setAutoFillBackground(False)
        self.frame_81.setFrameShape(QFrame.Panel)
        self.frame_81.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(10, 3, 10, 10)
        self.frame_32 = QFrame(self.frame_81)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy1.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy1)
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setMaximumSize(QSize(16777215, 16777215))
        self.frame_32.setStyleSheet(u"font-size:17px;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_32)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 2, -1)
        self.frame_3 = QFrame(self.frame_32)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.frame_31 = QFrame(self.frame_3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 80))
        self.frame_31.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"   border-radius:5px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(90, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)

        self.label_21 = QLabel(self.frame_31)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(300, 100))
        self.label_21.setStyleSheet(u"font-size:30px;\n"
"color: white;\n"
"font: 24pt \"Mongolian Baiti\";")

        self.horizontalLayout_17.addWidget(self.label_21)

        self.horizontalSpacer_14 = QSpacerItem(300, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)


        self.verticalLayout_4.addWidget(self.frame_31)

        self.scrollArea_2 = QScrollArea(self.frame_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1143, 647))
        self.horizontalLayout_57 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.groupBox_20 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_20.setObjectName(u"groupBox_20")
        sizePolicy1.setHeightForWidth(self.groupBox_20.sizePolicy().hasHeightForWidth())
        self.groupBox_20.setSizePolicy(sizePolicy1)
        self.groupBox_20.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_20.setBaseSize(QSize(446, 0))
        self.groupBox_20.setStyleSheet(u"font: 22pt \"Mongolian Baiti\";\n"
"border:3px solid back")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_6 = QSpacerItem(20, 53, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_21.addItem(self.verticalSpacer_6)

        self.groupBox_14 = QGroupBox(self.groupBox_20)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(361, 196))
        self.groupBox_14.setMaximumSize(QSize(1287, 590))
        self.groupBox_14.setStyleSheet(u"font: 16pt \"Mongolian Baiti\";\n"
"border:3px solid back")
        self.horizontalLayout_37 = QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.groupBox_16 = QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMaximumSize(QSize(16777215, 126))
        self.groupBox_16.setStyleSheet(u"font: 14pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_88 = QFrame(self.groupBox_16)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(0, 0))
        self.frame_88.setMaximumSize(QSize(16777215, 39))
        self.frame_88.setStyleSheet(u"border: no")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_55 = QLabel(self.frame_88)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font-size:20px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_78.addWidget(self.label_55)

        self.lenght_not_critical = QSpinBox(self.frame_88)
        self.lenght_not_critical.setObjectName(u"lenght_not_critical")
        self.lenght_not_critical.setMinimumSize(QSize(128, 34))
        self.lenght_not_critical.setMaximumSize(QSize(56, 16777215))
        self.lenght_not_critical.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"font-size:14px;\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;")
        self.lenght_not_critical.setMaximum(1000)

        self.horizontalLayout_78.addWidget(self.lenght_not_critical)


        self.verticalLayout_27.addWidget(self.frame_88)

        self.frame_18 = QFrame(self.groupBox_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 30))
        self.frame_18.setStyleSheet(u"border: no")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_19 = QLabel(self.frame_18)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font-size:18px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_32.addWidget(self.label_19)

        self.lenght_not_critical_Max = QSpinBox(self.frame_18)
        self.lenght_not_critical_Max.setObjectName(u"lenght_not_critical_Max")
        self.lenght_not_critical_Max.setMinimumSize(QSize(128, 34))
        self.lenght_not_critical_Max.setMaximumSize(QSize(56, 16777215))
        self.lenght_not_critical_Max.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"font-size:14px;\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;")
        self.lenght_not_critical_Max.setMaximum(1000)

        self.horizontalLayout_32.addWidget(self.lenght_not_critical_Max)


        self.verticalLayout_27.addWidget(self.frame_18)


        self.horizontalLayout_37.addWidget(self.groupBox_16)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_17)

        self.groupBox_15 = QGroupBox(self.groupBox_14)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMinimumSize(QSize(0, 81))
        self.groupBox_15.setMaximumSize(QSize(16777215, 126))
        self.groupBox_15.setBaseSize(QSize(1, 0))
        self.groupBox_15.setStyleSheet(u"font: 14pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_87 = QFrame(self.groupBox_15)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMaximumSize(QSize(16777215, 34))
        self.frame_87.setStyleSheet(u"font-size:18px;\n"
"font: 12pt \"Mongolian Baiti\";\n"
"border: no\n"
"")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_54 = QLabel(self.frame_87)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font-size:18px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_77.addWidget(self.label_54)

        self.Depth_not_Critical = QSpinBox(self.frame_87)
        self.Depth_not_Critical.setObjectName(u"Depth_not_Critical")
        self.Depth_not_Critical.setMinimumSize(QSize(126, 32))
        self.Depth_not_Critical.setMaximumSize(QSize(56, 16777215))
        self.Depth_not_Critical.setStyleSheet(u"")
        self.Depth_not_Critical.setMaximum(1000)

        self.horizontalLayout_77.addWidget(self.Depth_not_Critical)


        self.verticalLayout_6.addWidget(self.frame_87)

        self.frame_17 = QFrame(self.groupBox_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 34))
        self.frame_17.setStyleSheet(u"font-size:18px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"border: no")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font-size:18px;\n"
"font: 12pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_34.addWidget(self.label_13)

        self.Depth_not_Critical_Max = QSpinBox(self.frame_17)
        self.Depth_not_Critical_Max.setObjectName(u"Depth_not_Critical_Max")
        self.Depth_not_Critical_Max.setMinimumSize(QSize(128, 34))
        self.Depth_not_Critical_Max.setMaximumSize(QSize(55, 16777215))
        self.Depth_not_Critical_Max.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"font-size:14px;\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;")
        self.Depth_not_Critical_Max.setMaximum(1000)

        self.horizontalLayout_34.addWidget(self.Depth_not_Critical_Max)


        self.verticalLayout_6.addWidget(self.frame_17)


        self.horizontalLayout_37.addWidget(self.groupBox_15)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_18)

        self.groupBox_6 = QGroupBox(self.groupBox_14)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 86))
        self.groupBox_6.setMaximumSize(QSize(16777215, 125))
        self.groupBox_6.setStyleSheet(u"font: 14pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_86 = QFrame(self.groupBox_6)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(0, 0))
        self.frame_86.setMaximumSize(QSize(16777215, 32))
        self.frame_86.setBaseSize(QSize(0, 0))
        self.frame_86.setStyleSheet(u"border: no")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_53 = QLabel(self.frame_86)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font-size:18px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_76.addWidget(self.label_53)

        self.Width_not_critical = QSpinBox(self.frame_86)
        self.Width_not_critical.setObjectName(u"Width_not_critical")
        self.Width_not_critical.setMinimumSize(QSize(126, 32))
        self.Width_not_critical.setMaximumSize(QSize(56, 16777215))
        self.Width_not_critical.setStyleSheet(u"")
        self.Width_not_critical.setMaximum(1000)

        self.horizontalLayout_76.addWidget(self.Width_not_critical)


        self.verticalLayout_2.addWidget(self.frame_86)

        self.frame_15 = QFrame(self.groupBox_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 31))
        self.frame_15.setStyleSheet(u"border: no")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-size:18px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"")

        self.horizontalLayout_31.addWidget(self.label_9)

        self.Width_not_critical_Max = QSpinBox(self.frame_15)
        self.Width_not_critical_Max.setObjectName(u"Width_not_critical_Max")
        self.Width_not_critical_Max.setMinimumSize(QSize(126, 32))
        self.Width_not_critical_Max.setMaximumSize(QSize(56, 16777215))
        self.Width_not_critical_Max.setStyleSheet(u"")
        self.Width_not_critical_Max.setMaximum(1000)

        self.horizontalLayout_31.addWidget(self.Width_not_critical_Max)


        self.verticalLayout_2.addWidget(self.frame_15)


        self.horizontalLayout_37.addWidget(self.groupBox_6)


        self.verticalLayout_21.addWidget(self.groupBox_14)

        self.verticalSpacer_10 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_21.addItem(self.verticalSpacer_10)

        self.groupBox_12 = QGroupBox(self.groupBox_20)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(312, 59))
        self.groupBox_12.setMaximumSize(QSize(1286, 206))
        self.groupBox_12.setStyleSheet(u"font: 16pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.horizontalLayout_75 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.groupBox_18 = QGroupBox(self.groupBox_12)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setMinimumSize(QSize(0, 61))
        self.groupBox_18.setMaximumSize(QSize(16777215, 105))
        self.groupBox_18.setStyleSheet(u"font: 14pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_30 = QFrame(self.groupBox_18)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 0))
        self.frame_30.setMaximumSize(QSize(16777215, 43))
        self.frame_30.setStyleSheet(u"border:no")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_50 = QLabel(self.frame_30)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font-size:18px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_73.addWidget(self.label_50)

        self.Lenght_Critical = QSpinBox(self.frame_30)
        self.Lenght_Critical.setObjectName(u"Lenght_Critical")
        self.Lenght_Critical.setMinimumSize(QSize(128, 34))
        self.Lenght_Critical.setMaximumSize(QSize(56, 16777215))
        self.Lenght_Critical.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"font-size:14px;\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;")
        self.Lenght_Critical.setMaximum(1000)

        self.horizontalLayout_73.addWidget(self.Lenght_Critical)


        self.verticalLayout_20.addWidget(self.frame_30)


        self.horizontalLayout_75.addWidget(self.groupBox_18)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_19)

        self.groupBox_17 = QGroupBox(self.groupBox_12)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMinimumSize(QSize(0, 89))
        self.groupBox_17.setMaximumSize(QSize(16777215, 105))
        self.groupBox_17.setStyleSheet(u"font: 14pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_83 = QFrame(self.groupBox_17)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMaximumSize(QSize(16777215, 39))
        self.frame_83.setStyleSheet(u"border:no")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_52 = QLabel(self.frame_83)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font-size:18px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_74.addWidget(self.label_52)

        self.Depth_Critical = QSpinBox(self.frame_83)
        self.Depth_Critical.setObjectName(u"Depth_Critical")
        self.Depth_Critical.setMinimumSize(QSize(126, 32))
        self.Depth_Critical.setMaximumSize(QSize(56, 16777215))
        self.Depth_Critical.setStyleSheet(u"")
        self.Depth_Critical.setMaximum(1000)

        self.horizontalLayout_74.addWidget(self.Depth_Critical)


        self.verticalLayout_23.addWidget(self.frame_83)


        self.horizontalLayout_75.addWidget(self.groupBox_17)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_20)

        self.groupBox_13 = QGroupBox(self.groupBox_12)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(0, 89))
        self.groupBox_13.setMaximumSize(QSize(16777215, 105))
        self.groupBox_13.setStyleSheet(u"font: 14pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_21 = QFrame(self.groupBox_13)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setMaximumSize(QSize(16777215, 41))
        self.frame_21.setBaseSize(QSize(0, 0))
        self.frame_21.setStyleSheet(u"border:no")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_51 = QLabel(self.frame_21)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font-size:18px;\n"
"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_72.addWidget(self.label_51)

        self.Width_critical = QSpinBox(self.frame_21)
        self.Width_critical.setObjectName(u"Width_critical")
        self.Width_critical.setMinimumSize(QSize(126, 32))
        self.Width_critical.setMaximumSize(QSize(56, 24))
        self.Width_critical.setStyleSheet(u"")
        self.Width_critical.setMaximum(1000)

        self.horizontalLayout_72.addWidget(self.Width_critical)


        self.verticalLayout_25.addWidget(self.frame_21)


        self.horizontalLayout_75.addWidget(self.groupBox_13)


        self.verticalLayout_21.addWidget(self.groupBox_12)

        self.frame_14 = QFrame(self.groupBox_20)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 99))
        self.frame_14.setMaximumSize(QSize(16777215, 87))
        self.frame_14.setStyleSheet(u"border:no")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_85 = QFrame(self.frame_14)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setGeometry(QRect(470, 30, 192, 64))
        self.frame_85.setMaximumSize(QSize(196, 64))
        self.frame_85.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"  border-radius:5px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_85)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.Save_Calibration = QPushButton(self.frame_85)
        self.Save_Calibration.setObjectName(u"Save_Calibration")
        self.Save_Calibration.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"    background-color:#0C356A;\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"../icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save_Calibration.setIcon(icon12)

        self.verticalLayout_31.addWidget(self.Save_Calibration)


        self.verticalLayout_21.addWidget(self.frame_14)


        self.horizontalLayout_57.addWidget(self.groupBox_20)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_2)


        self.verticalLayout_10.addWidget(self.frame_3)


        self.horizontalLayout_28.addWidget(self.frame_32)


        self.verticalLayout_24.addWidget(self.frame_81)

        self.frame_8 = QFrame(self.frame_29)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_8)

        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(100, 16777215))
        self.label_24.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";")

        self.horizontalLayout_23.addWidget(self.label_24)

        self.Message_Calibration = QLabel(self.frame_8)
        self.Message_Calibration.setObjectName(u"Message_Calibration")
        self.Message_Calibration.setMinimumSize(QSize(300, 0))
        self.Message_Calibration.setMaximumSize(QSize(400, 16777215))
        self.Message_Calibration.setFrameShape(QFrame.Box)
        self.Message_Calibration.setFrameShadow(QFrame.Raised)
        self.Message_Calibration.setAlignment(Qt.AlignCenter)
        self.Message_Calibration.setMargin(4)

        self.horizontalLayout_23.addWidget(self.Message_Calibration)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_9)


        self.verticalLayout_24.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_29)

        self.pages_stackwgt.addWidget(self.defect_tab)
        self.Report_page = QWidget()
        self.Report_page.setObjectName(u"Report_page")
        self.horizontalLayout_6 = QHBoxLayout(self.Report_page)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, -1)
        self.filters_frame = QFrame(self.Report_page)
        self.filters_frame.setObjectName(u"filters_frame")
        self.filters_frame.setMaximumSize(QSize(400, 16777215))
        self.filters_frame.setStyleSheet(u"#filters_scroll_area,\n"
"#filters_frame{\n"
"	background-color: #fafafa;\n"
"}")
        self.filters_frame.setFrameShape(QFrame.Panel)
        self.filters_frame.setFrameShadow(QFrame.Raised)
        self.filters_frame.setLineWidth(3)
        self.verticalLayout_28 = QVBoxLayout(self.filters_frame)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, -1, 11, -1)
        self.label_40 = QLabel(self.filters_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 50))
        self.label_40.setStyleSheet(u"font-size:20px;\n"
"font-weight:bold;")

        self.verticalLayout_28.addWidget(self.label_40)

        self.scrollArea_3 = QScrollArea(self.filters_frame)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 500))
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.filters_scroll_area = QWidget()
        self.filters_scroll_area.setObjectName(u"filters_scroll_area")
        self.filters_scroll_area.setGeometry(QRect(0, 0, 281, 573))
        self.verticalLayout_5 = QVBoxLayout(self.filters_scroll_area)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, -1, -1, -1)
        self.groupBox_10 = QGroupBox(self.filters_scroll_area)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(0, 130))
        self.groupBox_10.setMaximumSize(QSize(16777215, 250))
        self.groupBox_10.setStyleSheet(u"")
        self.groupBox_10.setCheckable(True)
        self.groupBox_10.setChecked(False)
        self.horizontalLayout_61 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(-1, 30, -1, -1)
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_43 = QLabel(self.groupBox_10)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"border:no")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_43)

        self.lineEdit_Min_Date = QDateEdit(self.groupBox_10)
        self.lineEdit_Min_Date.setObjectName(u"lineEdit_Min_Date")
        self.lineEdit_Min_Date.setStyleSheet(u"")
        self.lineEdit_Min_Date.setDate(QDate(2023, 1, 1))

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Min_Date)

        self.label_45 = QLabel(self.groupBox_10)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"border:no")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_45)

        self.lineEdit_Max_Date = QDateEdit(self.groupBox_10)
        self.lineEdit_Max_Date.setObjectName(u"lineEdit_Max_Date")
        self.lineEdit_Max_Date.setStyleSheet(u"")
        self.lineEdit_Max_Date.setMaximumDate(QDate(9999, 11, 30))
        self.lineEdit_Max_Date.setMaximumTime(QTime(23, 59, 59))
        self.lineEdit_Max_Date.setDate(QDate(2023, 1, 1))

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Max_Date)


        self.horizontalLayout_61.addLayout(self.formLayout_4)


        self.verticalLayout_5.addWidget(self.groupBox_10)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.groupBox_2 = QGroupBox(self.filters_scroll_area)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 150))
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)


        self.verticalLayout_11.addLayout(self.formLayout)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.groupBox_3 = QGroupBox(self.filters_scroll_area)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 120))
        self.groupBox_3.setMaximumSize(QSize(16777215, 150))
        self.groupBox_3.setStyleSheet(u"")
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 30, -1, -1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_Min_Depth = QSpinBox(self.groupBox_3)
        self.lineEdit_Min_Depth.setObjectName(u"lineEdit_Min_Depth")
        self.lineEdit_Min_Depth.setMaximum(50)

        self.gridLayout_4.addWidget(self.lineEdit_Min_Depth, 0, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font-size:16px;")

        self.gridLayout_4.addWidget(self.label_44, 0, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"border:no")

        self.gridLayout_4.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_34 = QLabel(self.groupBox_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"border:no")

        self.gridLayout_4.addWidget(self.label_34, 1, 0, 1, 1)

        self.lineEdit_Max_Depth = QSpinBox(self.groupBox_3)
        self.lineEdit_Max_Depth.setObjectName(u"lineEdit_Max_Depth")
        self.lineEdit_Max_Depth.setMaximum(50)

        self.gridLayout_4.addWidget(self.lineEdit_Max_Depth, 1, 1, 1, 1)

        self.label_46 = QLabel(self.groupBox_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font-size:16px;")

        self.gridLayout_4.addWidget(self.label_46, 1, 2, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_4)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.groupBox = QGroupBox(self.filters_scroll_area)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(400, 150))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.horizontalLayout_38 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 30, -1, -1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_Max_Length = QSpinBox(self.groupBox)
        self.lineEdit_Max_Length.setObjectName(u"lineEdit_Max_Length")
        self.lineEdit_Max_Length.setMaximum(20000)

        self.gridLayout_2.addWidget(self.lineEdit_Max_Length, 1, 1, 1, 1)

        self.lineEdit_Min_Length = QSpinBox(self.groupBox)
        self.lineEdit_Min_Length.setObjectName(u"lineEdit_Min_Length")
        self.lineEdit_Min_Length.setMaximum(20000)

        self.gridLayout_2.addWidget(self.lineEdit_Min_Length, 0, 1, 1, 1)

        self.label_37 = QLabel(self.groupBox)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"border:no")

        self.gridLayout_2.addWidget(self.label_37, 1, 0, 1, 1)

        self.label_36 = QLabel(self.groupBox)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"border:no")

        self.gridLayout_2.addWidget(self.label_36, 0, 0, 1, 1)

        self.label_47 = QLabel(self.groupBox)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font-size:16px;")

        self.gridLayout_2.addWidget(self.label_47, 0, 2, 1, 1)

        self.label_48 = QLabel(self.groupBox)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font-size:16px;")

        self.gridLayout_2.addWidget(self.label_48, 1, 2, 1, 1)


        self.horizontalLayout_38.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.scrollArea_3.setWidget(self.filters_scroll_area)

        self.verticalLayout_28.addWidget(self.scrollArea_3)


        self.horizontalLayout_6.addWidget(self.filters_frame)

        self.line = QFrame(self.Report_page)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(5, 10))
        self.line.setStyleSheet(u"color:rgb(12, 53, 106);\n"
"background-color:rgb(12, 53, 106);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line)

        self.frame_39 = QFrame(self.Report_page)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(16777215, 16777215))
        self.frame_39.setStyleSheet(u"background-color:#ffffff;")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Plain)
        self.verticalLayout_32 = QVBoxLayout(self.frame_39)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(11, 1, 1, 21)
        self.frame_82 = QFrame(self.frame_39)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(0, 0))
        self.frame_82.setMaximumSize(QSize(16777215, 16777215))
        self.frame_82.setFrameShape(QFrame.Panel)
        self.frame_82.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(10, 3, 10, 10)
        self.frame_42 = QFrame(self.frame_82)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_42)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 2, -1)
        self.frame_40 = QFrame(self.frame_42)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 80))
        self.frame_40.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Plain)
        self.frame_40.setLineWidth(3)
        self.verticalLayout_34 = QVBoxLayout(self.frame_40)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_28 = QLabel(self.frame_41)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(150, 100))
        self.label_28.setStyleSheet(u"font-size:30px;\n"
"color: white;\n"
"font: 26pt \"Mongolian Baiti\";")

        self.horizontalLayout_22.addWidget(self.label_28)


        self.verticalLayout_34.addWidget(self.frame_41)


        self.verticalLayout_35.addWidget(self.frame_40)

        self.tableWidget = QTableWidget(self.frame_42)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_35.addWidget(self.tableWidget)

        self.frame_69 = QFrame(self.frame_42)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 50))
        self.frame_69.setMaximumSize(QSize(16777215, 100))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)

        self.verticalLayout_35.addWidget(self.frame_69)


        self.horizontalLayout_29.addWidget(self.frame_42)


        self.verticalLayout_32.addWidget(self.frame_82)

        self.frame_38 = QFrame(self.frame_39)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 40))
        self.frame_38.setMaximumSize(QSize(16777215, 120))
        self.frame_38.setBaseSize(QSize(100, 0))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_12)

        self.label_6 = QLabel(self.frame_38)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";")

        self.horizontalLayout_42.addWidget(self.label_6)

        self.Message_Report = QLabel(self.frame_38)
        self.Message_Report.setObjectName(u"Message_Report")
        self.Message_Report.setMinimumSize(QSize(300, 0))
        self.Message_Report.setMaximumSize(QSize(400, 16777215))
        self.Message_Report.setFrameShape(QFrame.Box)
        self.Message_Report.setFrameShadow(QFrame.Raised)
        self.Message_Report.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.Message_Report)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_13)


        self.verticalLayout_32.addWidget(self.frame_38)


        self.horizontalLayout_6.addWidget(self.frame_39)

        self.pages_stackwgt.addWidget(self.Report_page)
        self.Setting_Page = QWidget()
        self.Setting_Page.setObjectName(u"Setting_Page")
        self.horizontalLayout_14 = QHBoxLayout(self.Setting_Page)
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, -1, -1)
        self.settings_tabs = QTabWidget(self.Setting_Page)
        self.settings_tabs.setObjectName(u"settings_tabs")
        self.camera_tab = QWidget()
        self.camera_tab.setObjectName(u"camera_tab")
        self.horizontalLayout_49 = QHBoxLayout(self.camera_tab)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.camera_setting_frame = QFrame(self.camera_tab)
        self.camera_setting_frame.setObjectName(u"camera_setting_frame")
        self.camera_setting_frame.setMaximumSize(QSize(350, 16777215))
        self.camera_setting_frame.setStyleSheet(u"QLabel{\n"
"	font: 16px;\n"
"	border: no\n"
"}\n"
"\n"
"#camera_setting_frame{\n"
"\n"
"	border: 2px solid #445069;\n"
"\n"
"}\n"
"\n"
"QSpinBox{\n"
"	min-width: 150px;\n"
"\n"
"}")
        self.camera_setting_frame.setFrameShape(QFrame.StyledPanel)
        self.camera_setting_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.camera_setting_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 17, -1, -1)
        self.Camera_connection_Camera_setting = QPushButton(self.camera_setting_frame)
        self.Camera_connection_Camera_setting.setObjectName(u"Camera_connection_Camera_setting")
        self.Camera_connection_Camera_setting.setMaximumSize(QSize(80, 30))
        self.Camera_connection_Camera_setting.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"    background-color:#F1F0E8;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"    background-color:rgb(12, 53, 106);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:rgb(9, 39, 76);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icon/camera_disconnected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Camera_connection_Camera_setting.setIcon(icon13)
        self.Camera_connection_Camera_setting.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.Camera_connection_Camera_setting)

        self.Stop_connection_Camera_setting = QPushButton(self.camera_setting_frame)
        self.Stop_connection_Camera_setting.setObjectName(u"Stop_connection_Camera_setting")
        self.Stop_connection_Camera_setting.setMaximumSize(QSize(80, 30))
        self.Stop_connection_Camera_setting.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"    background-color:#F1F0E8;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"    background-color:rgb(12, 53, 106);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        self.Stop_connection_Camera_setting.setIcon(icon9)
        self.Stop_connection_Camera_setting.setIconSize(QSize(50, 50))

        self.horizontalLayout_18.addWidget(self.Stop_connection_Camera_setting)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_22)


        self.verticalLayout_33.addLayout(self.horizontalLayout_18)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(20)
        self.label_18 = QLabel(self.camera_setting_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_18, 8, 0, 1, 1)

        self.offsetx_spinbox = QSpinBox(self.camera_setting_frame)
        self.offsetx_spinbox.setObjectName(u"offsetx_spinbox")
        self.offsetx_spinbox.setMaximumSize(QSize(90, 33))
        self.offsetx_spinbox.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.offsetx_spinbox, 7, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.cameras_combobox = QComboBox(self.camera_setting_frame)
        self.cameras_combobox.setObjectName(u"cameras_combobox")
        self.cameras_combobox.setStyleSheet(u"min-width:150px;")

        self.gridLayout_7.addWidget(self.cameras_combobox, 0, 1, 1, 1)

        self.label_14 = QLabel(self.camera_setting_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_14, 4, 0, 1, 1)

        self.label_11 = QLabel(self.camera_setting_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_21, 1, 2, 1, 1)

        self.offsety_spinbox = QSpinBox(self.camera_setting_frame)
        self.offsety_spinbox.setObjectName(u"offsety_spinbox")
        self.offsety_spinbox.setMaximumSize(QSize(90, 33))
        self.offsety_spinbox.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.offsety_spinbox, 8, 1, 1, 1)

        self.label_17 = QLabel(self.camera_setting_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_17, 7, 0, 1, 1)

        self.devices_sn_combobox = QComboBox(self.camera_setting_frame)
        self.devices_sn_combobox.setObjectName(u"devices_sn_combobox")

        self.gridLayout_7.addWidget(self.devices_sn_combobox, 1, 1, 1, 1)

        self.width_spinbox = QSpinBox(self.camera_setting_frame)
        self.width_spinbox.setObjectName(u"width_spinbox")
        self.width_spinbox.setMaximumSize(QSize(90, 33))
        self.width_spinbox.setStyleSheet(u"")
        self.width_spinbox.setMaximum(10000)

        self.gridLayout_7.addWidget(self.width_spinbox, 4, 1, 1, 1)

        self.label_42 = QLabel(self.camera_setting_frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_16 = QLabel(self.camera_setting_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_16, 6, 0, 1, 1)

        self.expo_spinbox = QSpinBox(self.camera_setting_frame)
        self.expo_spinbox.setObjectName(u"expo_spinbox")
        self.expo_spinbox.setMaximumSize(QSize(90, 30))
        self.expo_spinbox.setStyleSheet(u"")
        self.expo_spinbox.setMaximum(10000000)

        self.gridLayout_7.addWidget(self.expo_spinbox, 6, 1, 1, 1)

        self.height_spinbox = QSpinBox(self.camera_setting_frame)
        self.height_spinbox.setObjectName(u"height_spinbox")
        self.height_spinbox.setMaximumSize(QSize(90, 33))
        self.height_spinbox.setStyleSheet(u"")
        self.height_spinbox.setMaximum(100000)

        self.gridLayout_7.addWidget(self.height_spinbox, 5, 1, 1, 1)

        self.label_12 = QLabel(self.camera_setting_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_12, 5, 0, 1, 1)

        self.label_15 = QLabel(self.camera_setting_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_15, 3, 0, 1, 1)

        self.gain_spinbox = QSpinBox(self.camera_setting_frame)
        self.gain_spinbox.setObjectName(u"gain_spinbox")
        self.gain_spinbox.setMaximumSize(QSize(90, 33))
        self.gain_spinbox.setStyleSheet(u"")
        self.gain_spinbox.setMaximum(600)

        self.gridLayout_7.addWidget(self.gain_spinbox, 3, 1, 1, 1)


        self.verticalLayout_33.addLayout(self.gridLayout_7)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 50, -1, -1)
        self.Save_Camera_Parameters = QPushButton(self.camera_setting_frame)
        self.Save_Camera_Parameters.setObjectName(u"Save_Camera_Parameters")
        self.Save_Camera_Parameters.setMaximumSize(QSize(200, 16777215))
        self.Save_Camera_Parameters.setCursor(QCursor(Qt.PointingHandCursor))
        self.Save_Camera_Parameters.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    background-color:#0C356A;\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"	background-color: rgb(12, 53, 106);\n"
"	padding: 15px 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.Save_Camera_Parameters.setIcon(icon12)
        self.Save_Camera_Parameters.setIconSize(QSize(26, 26))

        self.horizontalLayout_13.addWidget(self.Save_Camera_Parameters)


        self.verticalLayout_33.addLayout(self.horizontalLayout_13)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)


        self.horizontalLayout_49.addWidget(self.camera_setting_frame)

        self.frame_61 = QFrame(self.camera_tab)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_61)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_7 = QFrame(self.frame_61)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 75))
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setBaseSize(QSize(0, 100))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.frame_7.setLineWidth(3)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(250, 100))
        self.label_8.setStyleSheet(u"font-size:30px;\n"
"color: white;\n"
"font: 26pt \"Mongolian Baiti\";")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_16)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.Showlive_Setting = QLabel(self.frame_61)
        self.Showlive_Setting.setObjectName(u"Showlive_Setting")

        self.verticalLayout_8.addWidget(self.Showlive_Setting)

        self.frame_20 = QFrame(self.frame_61)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 44))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_10)

        self.label_27 = QLabel(self.frame_20)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(100, 16777215))
        self.label_27.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";")

        self.horizontalLayout_33.addWidget(self.label_27)

        self.Message_Camera = QLabel(self.frame_20)
        self.Message_Camera.setObjectName(u"Message_Camera")
        self.Message_Camera.setMinimumSize(QSize(300, 0))
        self.Message_Camera.setMaximumSize(QSize(360, 16777215))
        self.Message_Camera.setFrameShape(QFrame.Box)
        self.Message_Camera.setFrameShadow(QFrame.Raised)
        self.Message_Camera.setAlignment(Qt.AlignCenter)
        self.Message_Camera.setMargin(4)

        self.horizontalLayout_33.addWidget(self.Message_Camera)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_11)


        self.verticalLayout_8.addWidget(self.frame_20)


        self.horizontalLayout_49.addWidget(self.frame_61)

        self.settings_tabs.addTab(self.camera_tab, "")
        self.algorithm_tab = QWidget()
        self.algorithm_tab.setObjectName(u"algorithm_tab")
        self.verticalLayout_13 = QVBoxLayout(self.algorithm_tab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea = QScrollArea(self.algorithm_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1114, 733))
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_step1 = QFrame(self.scrollAreaWidgetContents)
        self.frame_step1.setObjectName(u"frame_step1")
        self.frame_step1.setMaximumSize(QSize(16777215, 400))
        self.frame_step1.setStyleSheet(u"#algo_setting_step1_frame,\n"
"#frame_step1\n"
"{\n"
"border: 2 solid rgba(12, 53, 106, 100);\n"
"background-color:#ffffff;\n"
"\n"
"}\n"
"")
        self.frame_step1.setFrameShape(QFrame.StyledPanel)
        self.frame_step1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_step1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.algo_setting_step1_frame = QFrame(self.frame_step1)
        self.algo_setting_step1_frame.setObjectName(u"algo_setting_step1_frame")
        self.algo_setting_step1_frame.setStyleSheet(u"")
        self.algo_setting_step1_frame.setFrameShape(QFrame.StyledPanel)
        self.algo_setting_step1_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.algo_setting_step1_frame)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_63 = QLabel(self.algo_setting_step1_frame)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 50))
        self.label_63.setStyleSheet(u"font-size: 26px;\n"
"font-weight: bold;\n"
"color:rgb(12, 53, 106);")

        self.verticalLayout_29.addWidget(self.label_63)

        self.frame_34 = QFrame(self.algo_setting_step1_frame)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_34)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_61 = QLabel(self.frame_34)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_8.addWidget(self.label_61, 1, 0, 1, 1)

        self.alghoritm_background_thresh = QSpinBox(self.frame_34)
        self.alghoritm_background_thresh.setObjectName(u"alghoritm_background_thresh")

        self.gridLayout_8.addWidget(self.alghoritm_background_thresh, 0, 1, 1, 1)

        self.alghoritm_conv_window_size = QSpinBox(self.frame_34)
        self.alghoritm_conv_window_size.setObjectName(u"alghoritm_conv_window_size")

        self.gridLayout_8.addWidget(self.alghoritm_conv_window_size, 1, 1, 1, 1)

        self.label_49 = QLabel(self.frame_34)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_8.addWidget(self.label_49, 0, 0, 1, 1)


        self.verticalLayout_29.addWidget(self.frame_34)


        self.horizontalLayout_19.addWidget(self.algo_setting_step1_frame)

        self.frame_36 = QFrame(self.frame_step1)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_36)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.algorithm_image1 = QLabel(self.frame_36)
        self.algorithm_image1.setObjectName(u"algorithm_image1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.algorithm_image1.sizePolicy().hasHeightForWidth())
        self.algorithm_image1.setSizePolicy(sizePolicy2)

        self.verticalLayout_19.addWidget(self.algorithm_image1)


        self.horizontalLayout_19.addWidget(self.frame_36)


        self.verticalLayout_40.addWidget(self.frame_step1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.scrollArea)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Save_algorithm_setting = QPushButton(self.algorithm_tab)
        self.Save_algorithm_setting.setObjectName(u"Save_algorithm_setting")
        self.Save_algorithm_setting.setMaximumSize(QSize(200, 16777215))
        self.Save_algorithm_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.Save_algorithm_setting.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    background-color:#0C356A;\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"	background-color: rgb(12, 53, 106);\n"
"	padding: 15px 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.Save_algorithm_setting.setIcon(icon12)
        self.Save_algorithm_setting.setIconSize(QSize(26, 26))

        self.horizontalLayout_12.addWidget(self.Save_algorithm_setting)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.settings_tabs.addTab(self.algorithm_tab, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.horizontalLayout_16 = QHBoxLayout(self.tab_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.groupBox_21 = QGroupBox(self.tab_11)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setStyleSheet(u"font: 18pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalSpacer_11 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_30.addItem(self.verticalSpacer_11)

        self.frame_23 = QFrame(self.groupBox_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 40))
        self.frame_23.setMaximumSize(QSize(16777215, 39))
        self.frame_23.setStyleSheet(u"border: 2px solid back")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_38 = QLabel(self.frame_23)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(244, 16777215))
        self.label_38.setStyleSheet(u"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_36.addWidget(self.label_38)

        self.Show_Tear_Depth_Label = QLabel(self.frame_23)
        self.Show_Tear_Depth_Label.setObjectName(u"Show_Tear_Depth_Label")
        self.Show_Tear_Depth_Label.setMaximumSize(QSize(100, 16777215))
        self.Show_Tear_Depth_Label.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;\n"
"font-size:18px;")

        self.horizontalLayout_36.addWidget(self.Show_Tear_Depth_Label)


        self.verticalLayout_30.addWidget(self.frame_23)

        self.verticalSpacer_20 = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_30.addItem(self.verticalSpacer_20)

        self.frame_24 = QFrame(self.groupBox_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 59))
        self.frame_24.setMaximumSize(QSize(16777215, 67))
        self.frame_24.setStyleSheet(u"border:no\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.frame_93 = QFrame(self.frame_24)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(0, 36))
        self.frame_93.setMaximumSize(QSize(179, 66))
        self.frame_93.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"border-radius:5px;\n"
"}\n"
"")
        self.frame_93.setFrameShape(QFrame.Box)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.frame_93.setLineWidth(3)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.Show_Tear_Depth_Button = QPushButton(self.frame_93)
        self.Show_Tear_Depth_Button.setObjectName(u"Show_Tear_Depth_Button")
        self.Show_Tear_Depth_Button.setMaximumSize(QSize(120, 16777215))
        self.Show_Tear_Depth_Button.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    background-color:#0C356A;\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"")

        self.horizontalLayout_84.addWidget(self.Show_Tear_Depth_Button)


        self.horizontalLayout_85.addWidget(self.frame_93)


        self.verticalLayout_30.addWidget(self.frame_24)


        self.horizontalLayout_16.addWidget(self.groupBox_21)

        self.groupBox_19 = QGroupBox(self.tab_11)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setStyleSheet(u"font: 18pt \"Mongolian Baiti\";\n"
"border: 3px solid back")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_26.addItem(self.verticalSpacer_12)

        self.frame_84 = QFrame(self.groupBox_19)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(0, 40))
        self.frame_84.setMaximumSize(QSize(16777215, 40))
        self.frame_84.setStyleSheet(u"border: 2px solid back")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_56 = QLabel(self.frame_84)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_79.addWidget(self.label_56)

        self.SpinBox_GRADIENT_SIZE = QSpinBox(self.frame_84)
        self.SpinBox_GRADIENT_SIZE.setObjectName(u"SpinBox_GRADIENT_SIZE")
        self.SpinBox_GRADIENT_SIZE.setMaximumSize(QSize(60, 29))
        self.SpinBox_GRADIENT_SIZE.setStyleSheet(u"")
        self.SpinBox_GRADIENT_SIZE.setMaximum(100000)
        self.SpinBox_GRADIENT_SIZE.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_79.addWidget(self.SpinBox_GRADIENT_SIZE)


        self.verticalLayout_26.addWidget(self.frame_84)

        self.frame_89 = QFrame(self.groupBox_19)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMaximumSize(QSize(16777215, 40))
        self.frame_89.setStyleSheet(u"border: 2px solid back")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_57 = QLabel(self.frame_89)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_80.addWidget(self.label_57)

        self.SpinBox_Critical_Depth = QSpinBox(self.frame_89)
        self.SpinBox_Critical_Depth.setObjectName(u"SpinBox_Critical_Depth")
        self.SpinBox_Critical_Depth.setMaximumSize(QSize(60, 33))
        self.SpinBox_Critical_Depth.setStyleSheet(u"")
        self.SpinBox_Critical_Depth.setMaximum(10000)
        self.SpinBox_Critical_Depth.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_80.addWidget(self.SpinBox_Critical_Depth)


        self.verticalLayout_26.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.groupBox_19)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(16777215, 40))
        self.frame_90.setStyleSheet(u"border: 2px solid back")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_58 = QLabel(self.frame_90)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_81.addWidget(self.label_58)

        self.SpinBox_TEAR_DEPTH = QSpinBox(self.frame_90)
        self.SpinBox_TEAR_DEPTH.setObjectName(u"SpinBox_TEAR_DEPTH")
        self.SpinBox_TEAR_DEPTH.setMaximumSize(QSize(60, 33))
        self.SpinBox_TEAR_DEPTH.setStyleSheet(u"")
        self.SpinBox_TEAR_DEPTH.setMaximum(2000)
        self.SpinBox_TEAR_DEPTH.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_81.addWidget(self.SpinBox_TEAR_DEPTH)


        self.verticalLayout_26.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.groupBox_19)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMaximumSize(QSize(16777215, 40))
        self.frame_91.setStyleSheet(u"border: 2px solid back")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_59 = QLabel(self.frame_91)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_82.addWidget(self.label_59)

        self.SpinBox_MAX_ERROR = QSpinBox(self.frame_91)
        self.SpinBox_MAX_ERROR.setObjectName(u"SpinBox_MAX_ERROR")
        self.SpinBox_MAX_ERROR.setMinimumSize(QSize(128, 34))
        self.SpinBox_MAX_ERROR.setMaximumSize(QSize(60, 33))
        self.SpinBox_MAX_ERROR.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;\n"
"font-size:18px;")
        self.SpinBox_MAX_ERROR.setMaximum(10000000)
        self.SpinBox_MAX_ERROR.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_82.addWidget(self.SpinBox_MAX_ERROR)


        self.verticalLayout_26.addWidget(self.frame_91)

        self.frame_26 = QFrame(self.groupBox_19)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 40))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_23 = QLabel(self.frame_26)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_86.addWidget(self.label_23)

        self.pix_length = QLineEdit(self.frame_26)
        self.pix_length.setObjectName(u"pix_length")
        self.pix_length.setMaximumSize(QSize(60, 16777215))
        self.pix_length.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;\n"
"font-size:18px;")

        self.horizontalLayout_86.addWidget(self.pix_length)


        self.verticalLayout_26.addWidget(self.frame_26)

        self.frame_94 = QFrame(self.groupBox_19)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMaximumSize(QSize(16777215, 40))
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_39 = QLabel(self.frame_94)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_87.addWidget(self.label_39)

        self.pix_width = QLineEdit(self.frame_94)
        self.pix_width.setObjectName(u"pix_width")
        self.pix_width.setMaximumSize(QSize(60, 16777215))
        self.pix_width.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;\n"
"font-size:18px;")

        self.horizontalLayout_87.addWidget(self.pix_width)


        self.verticalLayout_26.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.groupBox_19)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMaximumSize(QSize(16777215, 40))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_137 = QLabel(self.frame_95)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setStyleSheet(u"font: 13pt \"Mongolian Baiti\";\n"
"border: no")

        self.horizontalLayout_88.addWidget(self.label_137)

        self.gradient_number = QLineEdit(self.frame_95)
        self.gradient_number.setObjectName(u"gradient_number")
        self.gradient_number.setMaximumSize(QSize(60, 16777215))
        self.gradient_number.setStyleSheet(u"background-color :rgb(219, 219, 219);\n"
"border-style: solid;\n"
"border-width: 1;\n"
"border-radius: 3;\n"
"font-size:18px;")

        self.horizontalLayout_88.addWidget(self.gradient_number)


        self.verticalLayout_26.addWidget(self.frame_95)

        self.frame_22 = QFrame(self.groupBox_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"border:no\n"
"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_92 = QFrame(self.frame_22)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(0, 36))
        self.frame_92.setMaximumSize(QSize(150, 59))
        self.frame_92.setStyleSheet(u"QFrame{\n"
"	background: #0C356A;\n"
"border-radius:5px;\n"
"}\n"
"")
        self.frame_92.setFrameShape(QFrame.Box)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.frame_92.setLineWidth(3)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.Save_Algorithm_Parameters = QPushButton(self.frame_92)
        self.Save_Algorithm_Parameters.setObjectName(u"Save_Algorithm_Parameters")
        self.Save_Algorithm_Parameters.setMaximumSize(QSize(120, 16777215))
        self.Save_Algorithm_Parameters.setCursor(QCursor(Qt.PointingHandCursor))
        self.Save_Algorithm_Parameters.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    background-color:#0C356A;\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.Save_Algorithm_Parameters.setIcon(icon12)
        self.Save_Algorithm_Parameters.setIconSize(QSize(26, 26))

        self.horizontalLayout_83.addWidget(self.Save_Algorithm_Parameters)


        self.horizontalLayout_35.addWidget(self.frame_92)


        self.verticalLayout_26.addWidget(self.frame_22)


        self.horizontalLayout_16.addWidget(self.groupBox_19)

        self.settings_tabs.addTab(self.tab_11, "")

        self.horizontalLayout_14.addWidget(self.settings_tabs)

        self.frame_4 = QFrame(self.Setting_Page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(500, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_4)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(-1, 4, -1, -1)

        self.horizontalLayout_14.addWidget(self.frame_4)

        self.pages_stackwgt.addWidget(self.Setting_Page)
        self.Users_page = QWidget()
        self.Users_page.setObjectName(u"Users_page")
        self.verticalLayout_47 = QVBoxLayout(self.Users_page)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.user_tabs = QTabWidget(self.Users_page)
        self.user_tabs.setObjectName(u"user_tabs")
        self.user_tabs.setStyleSheet(u"#all_users_tab,\n"
"#user_profile_tab,\n"
"#user_register_tab\n"
"{\n"
"	\n"
"	background-color: #ffffff;\n"
"\n"
"}")
        self.user_register_tab = QWidget()
        self.user_register_tab.setObjectName(u"user_register_tab")
        self.verticalLayout_41 = QVBoxLayout(self.user_register_tab)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.gridFrame_2 = QFrame(self.user_register_tab)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setStyleSheet(u"QLabel{\n"
"	font-size: 16px;\n"
"	color: rgb(52, 52, 52);\n"
"	padding-right: 20px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QLineEdit\n"
"{\n"
"	max-width: 300px;\n"
"\n"
"}")
        self.gridLayout_9 = QGridLayout(self.gridFrame_2)
        self.gridLayout_9.setSpacing(3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.userpage_user_role_combobox = QComboBox(self.gridFrame_2)
        self.userpage_user_role_combobox.addItem("")
        self.userpage_user_role_combobox.setObjectName(u"userpage_user_role_combobox")

        self.gridLayout_9.addWidget(self.userpage_user_role_combobox, 6, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_15, 5, 0, 1, 1)

        self.userpage_password_inpt = QLineEdit(self.gridFrame_2)
        self.userpage_password_inpt.setObjectName(u"userpage_password_inpt")

        self.gridLayout_9.addWidget(self.userpage_password_inpt, 2, 1, 1, 1)

        self.userpage_username_inpt = QLineEdit(self.gridFrame_2)
        self.userpage_username_inpt.setObjectName(u"userpage_username_inpt")

        self.gridLayout_9.addWidget(self.userpage_username_inpt, 0, 1, 1, 1)

        self.label_62 = QLabel(self.gridFrame_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_62, 6, 0, 1, 1)

        self.label_64 = QLabel(self.gridFrame_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_64, 0, 0, 1, 1)

        self.userpage_confirm_password_inpt = QLineEdit(self.gridFrame_2)
        self.userpage_confirm_password_inpt.setObjectName(u"userpage_confirm_password_inpt")
        self.userpage_confirm_password_inpt.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.userpage_confirm_password_inpt, 4, 1, 1, 1)

        self.label_65 = QLabel(self.gridFrame_2)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_65, 2, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_23, 0, 2, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_13, 3, 0, 1, 1)

        self.label_66 = QLabel(self.gridFrame_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_66, 4, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_16, 7, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_18, 1, 0, 1, 1)

        self.userspage_add_user_btn = QPushButton(self.gridFrame_2)
        self.userspage_add_user_btn.setObjectName(u"userspage_add_user_btn")
        self.userspage_add_user_btn.setStyleSheet(u"max-width: 120px;")
        icon14 = QIcon()
        icon14.addFile(u":/assets/Assets/icons/icons8-plus-white-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userspage_add_user_btn.setIcon(icon14)

        self.gridLayout_9.addWidget(self.userspage_add_user_btn, 8, 1, 1, 1)


        self.verticalLayout_41.addWidget(self.gridFrame_2)

        self.verticalSpacer_21 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_41.addItem(self.verticalSpacer_21)

        self.userspage_register_error_lbl = QLabel(self.user_register_tab)
        self.userspage_register_error_lbl.setObjectName(u"userspage_register_error_lbl")
        self.userspage_register_error_lbl.setMinimumSize(QSize(310, 35))
        self.userspage_register_error_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color: rgb(255, 95, 84);\n"
"padding:5px;\n"
"\n"
"min-width: 300px;\n"
"max-width: 16777px;\n"
"")

        self.verticalLayout_41.addWidget(self.userspage_register_error_lbl)

        self.userspage_register_success_frame = QFrame(self.user_register_tab)
        self.userspage_register_success_frame.setObjectName(u"userspage_register_success_frame")
        self.userspage_register_success_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(58, 209, 154);\n"
"}")
        self.userspage_register_success_frame.setFrameShape(QFrame.StyledPanel)
        self.userspage_register_success_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.userspage_register_success_frame)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_88 = QLabel(self.userspage_register_success_frame)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMaximumSize(QSize(50, 50))
        self.label_88.setPixmap(QPixmap(u":/assets/icons/icons8-check-150.png"))
        self.label_88.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.label_88)

        self.userspage_register_success_lbl = QLabel(self.userspage_register_success_frame)
        self.userspage_register_success_lbl.setObjectName(u"userspage_register_success_lbl")
        self.userspage_register_success_lbl.setMinimumSize(QSize(0, 50))
        self.userspage_register_success_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"\n"
"")
        self.userspage_register_success_lbl.setScaledContents(False)

        self.horizontalLayout_39.addWidget(self.userspage_register_success_lbl)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_70)


        self.verticalLayout_41.addWidget(self.userspage_register_success_frame)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_19)

        self.user_tabs.addTab(self.user_register_tab, "")
        self.user_profile_tab = QWidget()
        self.user_profile_tab.setObjectName(u"user_profile_tab")
        self.verticalLayout_42 = QVBoxLayout(self.user_profile_tab)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.userpage_editprofile_edit_profile_groupbox = QGroupBox(self.user_profile_tab)
        self.userpage_editprofile_edit_profile_groupbox.setObjectName(u"userpage_editprofile_edit_profile_groupbox")
        self.userpage_editprofile_edit_profile_groupbox.setStyleSheet(u"QLabel{\n"
"	font-size: 16px;\n"
"	color: rgb(52, 52, 52);\n"
"	padding-right: 20px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QLineEdit\n"
"{\n"
"	max-width: 300px;\n"
"\n"
"}")
        self.horizontalLayout_40 = QHBoxLayout(self.userpage_editprofile_edit_profile_groupbox)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(50, 50, -1, -1)
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(25)
        self.userpage_editprofile_username_inpt = QLineEdit(self.userpage_editprofile_edit_profile_groupbox)
        self.userpage_editprofile_username_inpt.setObjectName(u"userpage_editprofile_username_inpt")

        self.gridLayout_18.addWidget(self.userpage_editprofile_username_inpt, 0, 1, 1, 1)

        self.label_79 = QLabel(self.userpage_editprofile_edit_profile_groupbox)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_79, 0, 0, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_39, 0, 2, 1, 1)


        self.verticalLayout_43.addLayout(self.gridLayout_18)

        self.editprofile_error_lbl = QLabel(self.userpage_editprofile_edit_profile_groupbox)
        self.editprofile_error_lbl.setObjectName(u"editprofile_error_lbl")
        self.editprofile_error_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color: rgb(255, 95, 84);\n"
"padding:5px;\n"
"\n"
"min-width: 100px;\n"
"max-width: 16777px;\n"
"max-height: 30px;\n"
"")

        self.verticalLayout_43.addWidget(self.editprofile_error_lbl)

        self.horizontalFrame_7 = QFrame(self.userpage_editprofile_edit_profile_groupbox)
        self.horizontalFrame_7.setObjectName(u"horizontalFrame_7")
        self.horizontalFrame_7.setStyleSheet(u"QPushButton {\n"
"max-width: 120px;\n"
"}")
        self.horizontalLayout_41 = QHBoxLayout(self.horizontalFrame_7)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(-1, 30, -1, -1)
        self.userpage_editprofile_update_btn = QPushButton(self.horizontalFrame_7)
        self.userpage_editprofile_update_btn.setObjectName(u"userpage_editprofile_update_btn")
        self.userpage_editprofile_update_btn.setMinimumSize(QSize(150, 0))
        self.userpage_editprofile_update_btn.setMaximumSize(QSize(130, 16777215))
        self.userpage_editprofile_update_btn.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.userpage_editprofile_update_btn)

        self.userpage_editprofile_cancel_btn = QPushButton(self.horizontalFrame_7)
        self.userpage_editprofile_cancel_btn.setObjectName(u"userpage_editprofile_cancel_btn")

        self.horizontalLayout_41.addWidget(self.userpage_editprofile_cancel_btn)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_69)


        self.verticalLayout_43.addWidget(self.horizontalFrame_7)


        self.horizontalLayout_40.addLayout(self.verticalLayout_43)


        self.verticalLayout_42.addWidget(self.userpage_editprofile_edit_profile_groupbox)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_42.addItem(self.verticalSpacer_35)

        self.userpage_editprofile_change_pass_groupbox = QGroupBox(self.user_profile_tab)
        self.userpage_editprofile_change_pass_groupbox.setObjectName(u"userpage_editprofile_change_pass_groupbox")
        self.userpage_editprofile_change_pass_groupbox.setStyleSheet(u"QLabel{\n"
"	font-size: 16px;\n"
"	color: rgb(52, 52, 52);\n"
"	padding-right: 20px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QLineEdit\n"
"{\n"
"	max-width: 300px;\n"
"\n"
"}")
        self.horizontalLayout_43 = QHBoxLayout(self.userpage_editprofile_change_pass_groupbox)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(50, 50, -1, -1)
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(30)
        self.label_80 = QLabel(self.userpage_editprofile_change_pass_groupbox)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_80, 0, 0, 1, 1)

        self.label_81 = QLabel(self.userpage_editprofile_change_pass_groupbox)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_81, 1, 0, 1, 1)

        self.userpage_editprofile_confirm_new_password_inpt = QLineEdit(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_confirm_new_password_inpt.setObjectName(u"userpage_editprofile_confirm_new_password_inpt")

        self.gridLayout_22.addWidget(self.userpage_editprofile_confirm_new_password_inpt, 2, 1, 1, 1)

        self.userpage_editprofile_old_password_inpt = QLineEdit(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_old_password_inpt.setObjectName(u"userpage_editprofile_old_password_inpt")

        self.gridLayout_22.addWidget(self.userpage_editprofile_old_password_inpt, 0, 1, 1, 1)

        self.label_86 = QLabel(self.userpage_editprofile_change_pass_groupbox)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_22.addWidget(self.label_86, 2, 0, 1, 1)

        self.userpage_editprofile_new_password_inpt = QLineEdit(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_new_password_inpt.setObjectName(u"userpage_editprofile_new_password_inpt")

        self.gridLayout_22.addWidget(self.userpage_editprofile_new_password_inpt, 1, 1, 1, 1)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_73, 0, 2, 1, 1)


        self.verticalLayout_44.addLayout(self.gridLayout_22)

        self.changepass_error_lbl = QLabel(self.userpage_editprofile_change_pass_groupbox)
        self.changepass_error_lbl.setObjectName(u"changepass_error_lbl")
        self.changepass_error_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"background-color: rgb(255, 95, 84);\n"
"padding:5px;\n"
"\n"
"min-width: 300px;\n"
"max-width: 16777px;\n"
"max-height: 30px;\n"
"")

        self.verticalLayout_44.addWidget(self.changepass_error_lbl)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 30, -1, -1)
        self.userpage_editprofile_change_password_btn = QPushButton(self.userpage_editprofile_change_pass_groupbox)
        self.userpage_editprofile_change_password_btn.setObjectName(u"userpage_editprofile_change_password_btn")
        self.userpage_editprofile_change_password_btn.setMaximumSize(QSize(130, 16777215))
        self.userpage_editprofile_change_password_btn.setStyleSheet(u"max-width: 120px;")

        self.horizontalLayout_44.addWidget(self.userpage_editprofile_change_password_btn)

        self.horizontalSpacer_97 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_97)


        self.verticalLayout_44.addLayout(self.horizontalLayout_44)


        self.horizontalLayout_43.addLayout(self.verticalLayout_44)


        self.verticalLayout_42.addWidget(self.userpage_editprofile_change_pass_groupbox)

        self.userspage_editprofile_success_frame = QFrame(self.user_profile_tab)
        self.userspage_editprofile_success_frame.setObjectName(u"userspage_editprofile_success_frame")
        self.userspage_editprofile_success_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(58, 209, 154);\n"
"}")
        self.userspage_editprofile_success_frame.setFrameShape(QFrame.StyledPanel)
        self.userspage_editprofile_success_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.userspage_editprofile_success_frame)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_89 = QLabel(self.userspage_editprofile_success_frame)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMaximumSize(QSize(50, 50))
        self.label_89.setPixmap(QPixmap(u":/assets/icons/icons8-check-150.png"))
        self.label_89.setScaledContents(True)

        self.horizontalLayout_45.addWidget(self.label_89)

        self.userspage_editprofile_success_lbl = QLabel(self.userspage_editprofile_success_frame)
        self.userspage_editprofile_success_lbl.setObjectName(u"userspage_editprofile_success_lbl")
        self.userspage_editprofile_success_lbl.setMinimumSize(QSize(0, 50))
        self.userspage_editprofile_success_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: #ffffff;\n"
"\n"
"")
        self.userspage_editprofile_success_lbl.setScaledContents(False)

        self.horizontalLayout_45.addWidget(self.userspage_editprofile_success_lbl)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_71)


        self.verticalLayout_42.addWidget(self.userspage_editprofile_success_frame)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_36)

        self.user_tabs.addTab(self.user_profile_tab, "")
        self.all_users_tab = QWidget()
        self.all_users_tab.setObjectName(u"all_users_tab")
        self.verticalLayout_45 = QVBoxLayout(self.all_users_tab)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.userspage_user_heading_lbl = QLabel(self.all_users_tab)
        self.userspage_user_heading_lbl.setObjectName(u"userspage_user_heading_lbl")
        self.userspage_user_heading_lbl.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;\n"
"color: rgb(6, 76, 130);\n"
"min-height: 80px;\n"
"max-height: 80px;")

        self.verticalLayout_45.addWidget(self.userspage_user_heading_lbl)

        self.userpage_all_users_table = QTableWidget(self.all_users_tab)
        if (self.userpage_all_users_table.columnCount() < 5):
            self.userpage_all_users_table.setColumnCount(5)
        if (self.userpage_all_users_table.rowCount() < 3):
            self.userpage_all_users_table.setRowCount(3)
        self.userpage_all_users_table.setObjectName(u"userpage_all_users_table")
        self.userpage_all_users_table.setAutoFillBackground(False)
        self.userpage_all_users_table.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"    background-color:rgb(12, 53, 106);\n"
"	color: #ffffff;\n"
"    padding: 4px;\n"
"    font-size: 10pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #fffff8;\n"
"}\n"
"\n"
"")
        self.userpage_all_users_table.setFrameShape(QFrame.StyledPanel)
        self.userpage_all_users_table.setFrameShadow(QFrame.Raised)
        self.userpage_all_users_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.userpage_all_users_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userpage_all_users_table.setDefaultDropAction(Qt.IgnoreAction)
        self.userpage_all_users_table.setAlternatingRowColors(False)
        self.userpage_all_users_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.userpage_all_users_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.userpage_all_users_table.setTextElideMode(Qt.ElideMiddle)
        self.userpage_all_users_table.setSortingEnabled(False)
        self.userpage_all_users_table.setCornerButtonEnabled(True)
        self.userpage_all_users_table.setRowCount(3)
        self.userpage_all_users_table.setColumnCount(5)
        self.userpage_all_users_table.horizontalHeader().setVisible(False)
        self.userpage_all_users_table.horizontalHeader().setDefaultSectionSize(150)
        self.userpage_all_users_table.verticalHeader().setVisible(False)

        self.verticalLayout_45.addWidget(self.userpage_all_users_table)

        self.user_tabs.addTab(self.all_users_tab, "")

        self.verticalLayout_47.addWidget(self.user_tabs)

        self.pages_stackwgt.addWidget(self.Users_page)
        self.About_Page = QWidget()
        self.About_Page.setObjectName(u"About_Page")
        self.verticalLayout_49 = QVBoxLayout(self.About_Page)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_7 = QLabel(self.About_Page)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_49.addWidget(self.label_7)

        self.pages_stackwgt.addWidget(self.About_Page)

        self.verticalLayout_3.addWidget(self.pages_stackwgt)


        self.horizontalLayout_27.addWidget(self.main_frame)


        self.verticalLayout.addWidget(self.middle)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_stackwgt.setCurrentIndex(5)
        self.tabWidget.setCurrentIndex(1)
        self.settings_tabs.setCurrentIndex(1)
        self.user_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Online Belt Inspection System", None))
        self.logined_username_lbl.setText(QCoreApplication.translate("MainWindow", u"No User Logged in", None))
        self.login_logout_btn.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Down", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
#if QT_CONFIG(tooltip)
        self.LiveDetectionBT.setToolTip(QCoreApplication.translate("MainWindow", u"Live View", None))
#endif // QT_CONFIG(tooltip)
        self.LiveDetectionBT.setText("")
#if QT_CONFIG(tooltip)
        self.ReportConnectionBT.setToolTip(QCoreApplication.translate("MainWindow", u"Report", None))
#endif // QT_CONFIG(tooltip)
        self.ReportConnectionBT.setText("")
#if QT_CONFIG(tooltip)
        self.HelpConnectionBT.setToolTip(QCoreApplication.translate("MainWindow", u"Defect Parameters", None))
#endif // QT_CONFIG(tooltip)
        self.HelpConnectionBT.setText("")
#if QT_CONFIG(tooltip)
        self.SettingBT.setToolTip(QCoreApplication.translate("MainWindow", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.SettingBT.setText("")
#if QT_CONFIG(tooltip)
        self.usersBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.usersBtn.setText("")
#if QT_CONFIG(tooltip)
        self.AboutBT.setToolTip(QCoreApplication.translate("MainWindow", u"Defect Parameters", None))
#endif // QT_CONFIG(tooltip)
        self.AboutBT.setText("")
#if QT_CONFIG(tooltip)
        self.pages_stackwgt.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"System Status", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PLC Connection", None))
        self.Laser_Connection_2.setText("")
        self.Laser_Connection_Check.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Line Operating", None))
        self.Laser_Connection_3.setText("")
        self.Laser_Connection_4.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"System Operating", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Laser Detection", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Camera Connection", None))
        self.Laser_Connection.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Show Alarm", None))
        self.Not_Critical_live_view.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Critical Defect", None))
        self.Critical_live_view.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Not Critical Defect", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Normal Situation", None))
        self.Normal_live_view.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
        self.Message_LiveView.setText("")
#if QT_CONFIG(tooltip)
        self.Stop_connection.setToolTip(QCoreApplication.translate("MainWindow", u"Disconnect to Camera", None))
#endif // QT_CONFIG(tooltip)
        self.Stop_connection.setText("")
#if QT_CONFIG(tooltip)
        self.Camera_connection.setToolTip(QCoreApplication.translate("MainWindow", u"Connect to Camera", None))
#endif // QT_CONFIG(tooltip)
        self.Camera_connection.setText("")
#if QT_CONFIG(tooltip)
        self.live.setToolTip(QCoreApplication.translate("MainWindow", u"Show Live", None))
#endif // QT_CONFIG(tooltip)
        self.live.setText("")
#if QT_CONFIG(tooltip)
        self.Stop.setToolTip(QCoreApplication.translate("MainWindow", u"Stop Live", None))
#endif // QT_CONFIG(tooltip)
        self.Stop.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Live View", None))
        self.Showlive.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Properties of Last Defect", None))
        self.Depth.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Depth of Defect:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Length of Defect:", None))
        self.Width.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.Length.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.label_Width.setText(QCoreApplication.translate("MainWindow", u"Width of Defect:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Properties of Total Defect", None))
        self.Total_Number_Defect.setText(QCoreApplication.translate("MainWindow", u"    0", None))
        self.Total_Number_Critical_defect.setText(QCoreApplication.translate("MainWindow", u"    0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Number of Critical Defect:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Number of Defect:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.live_thickness_image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Defect Paremeters", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Define Parameteres of Defect", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Not Critical Defect", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Length of Defect", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Min Length ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Max Length", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Depth of Defect", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Min Depth ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Max Depth ", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Width of Defect", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Min Width", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Max Width ", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Critical Defect ", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Length of Defect", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Min Length", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Depth of defect", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Min Depth ", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Width of Defect", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Min Width ", None))
        self.Save_Calibration.setText(QCoreApplication.translate("MainWindow", u"Save Defect Parameters", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.Message_Calibration.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Search for Defect", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Search by Date of Defect", None))
#if QT_CONFIG(whatsthis)
        self.label_43.setWhatsThis(QCoreApplication.translate("MainWindow", u"border:no", None))
#endif // QT_CONFIG(whatsthis)
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.lineEdit_Min_Date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.lineEdit_Max_Date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Search by Type of Defect", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Critical", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Not Critical", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Search by Depth of Defect", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Search byLength of Defect", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Length of Defect", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Depth of Defect", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Width of Defect", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date of Defect", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Type of Defect", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Image of  Defect", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Remove Defect", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.Message_Report.setText("")
        self.Camera_connection_Camera_setting.setText("")
        self.Stop_connection_Camera_setting.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Offset Y", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Offset X", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
#if QT_CONFIG(tooltip)
        self.Save_Camera_Parameters.setToolTip(QCoreApplication.translate("MainWindow", u"Save Parameters", None))
#endif // QT_CONFIG(tooltip)
        self.Save_Camera_Parameters.setText(QCoreApplication.translate("MainWindow", u"Save Prameters", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Camera Live", None))
        self.Showlive_Setting.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.Message_Camera.setText("")
        self.settings_tabs.setTabText(self.settings_tabs.indexOf(self.camera_tab), QCoreApplication.translate("MainWindow", u"Camera Setting", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Step 1", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Convolotion Window Size", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Background Threshould", None))
        self.algorithm_image1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.Save_algorithm_setting.setToolTip(QCoreApplication.translate("MainWindow", u"Save Parameters", None))
#endif // QT_CONFIG(tooltip)
        self.Save_algorithm_setting.setText(QCoreApplication.translate("MainWindow", u"Save Prameters", None))
        self.settings_tabs.setTabText(self.settings_tabs.indexOf(self.algorithm_tab), QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Show Tear Depth", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TEAR_DEPTH", None))
        self.Show_Tear_Depth_Label.setText("")
#if QT_CONFIG(tooltip)
        self.Show_Tear_Depth_Button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Show_Tear_Depth_Button.setText(QCoreApplication.translate("MainWindow", u"Show Tear Depth", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Algorithm Parameters", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"GRADIENT_SIZE", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Critical_Depth", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"TEAR_DEPTH", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"MAX_ERROR", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Pix_length", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Pix_Width", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"GRADIENT_NUMBER", None))
#if QT_CONFIG(tooltip)
        self.Save_Algorithm_Parameters.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Save_Algorithm_Parameters.setText(QCoreApplication.translate("MainWindow", u"Save Prameters", None))
        self.settings_tabs.setTabText(self.settings_tabs.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.userpage_user_role_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"admin", None))

        self.label_62.setText(QCoreApplication.translate("MainWindow", u"User Role:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Pasword Confirm:", None))
        self.userspage_add_user_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.userspage_register_error_lbl.setText(QCoreApplication.translate("MainWindow", u"Username exist", None))
        self.label_88.setText("")
        self.userspage_register_success_lbl.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.user_register_tab), QCoreApplication.translate("MainWindow", u"register user", None))
        self.userpage_editprofile_edit_profile_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Edit Profile", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.editprofile_error_lbl.setText(QCoreApplication.translate("MainWindow", u"Username exist", None))
        self.userpage_editprofile_update_btn.setText(QCoreApplication.translate("MainWindow", u"Update Profile", None))
        self.userpage_editprofile_cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.userpage_editprofile_change_pass_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Confirm New Password", None))
        self.changepass_error_lbl.setText(QCoreApplication.translate("MainWindow", u"Username exist", None))
        self.userpage_editprofile_change_password_btn.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_89.setText("")
        self.userspage_editprofile_success_lbl.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.user_profile_tab), QCoreApplication.translate("MainWindow", u"Edit Profile", None))
        self.userspage_user_heading_lbl.setText(QCoreApplication.translate("MainWindow", u"Only Admin Can Access", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.all_users_tab), QCoreApplication.translate("MainWindow", u"All Users", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

