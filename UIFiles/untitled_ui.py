# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1253, 715)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_6 = QFrame(self.centralwidget)
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
        icon = QIcon()
        icon.addFile(u"../icons/camera_connected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop_connection.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u"../icons/camera_disconnected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Camera_connection.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u"../icons/Live00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.live.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u"../icons/stop-button2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop.setIcon(icon3)
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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_4)


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
        self.Length = QLabel(self.frame_58)
        self.Length.setObjectName(u"Length")
        self.Length.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.Length.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Length, 0, 1, 1, 1)

        self.Width = QLabel(self.frame_58)
        self.Width.setObjectName(u"Width")
        self.Width.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.Width.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Width, 2, 1, 1, 1)

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

        self.Depth = QLabel(self.frame_58)
        self.Depth.setObjectName(u"Depth")
        self.Depth.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";\n"
"border: no")
        self.Depth.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.Depth, 1, 1, 1, 1)

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


        self.verticalLayout.addWidget(self.frame_6)

        self.notifications_buttons_frame = QFrame(self.centralwidget)
        self.notifications_buttons_frame.setObjectName(u"notifications_buttons_frame")
        self.notifications_buttons_frame.setStyleSheet(u"#filter_btn:hover{\n"
"	icon:url(:/icons/icons/filter_hover.png);\n"
"}\n"
"\n"
"#clear_filter_btn:hover{\n"
"	icon:url(:/icons/icons/clear_filter_hover.png);\n"
"}\n"
"\n"
"#delete_notifs_btn:hover{\n"
"	icon:url(:/icons/icons/delete_hover.png);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.notifications_buttons_frame)
        self.horizontalLayout_6.setSpacing(14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 25, -1, -1)
        self.filter_btn = QPushButton(self.notifications_buttons_frame)
        self.filter_btn.setObjectName(u"filter_btn")
        self.filter_btn.setMinimumSize(QSize(50, 50))
        self.filter_btn.setMaximumSize(QSize(50, 50))
        self.filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.filter_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter_btn.setIcon(icon4)
        self.filter_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.filter_btn)

        self.clear_filter_btn = QPushButton(self.notifications_buttons_frame)
        self.clear_filter_btn.setObjectName(u"clear_filter_btn")
        self.clear_filter_btn.setEnabled(True)
        self.clear_filter_btn.setMinimumSize(QSize(50, 50))
        self.clear_filter_btn.setMaximumSize(QSize(50, 50))
        self.clear_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/clear_filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_filter_btn.setIcon(icon5)
        self.clear_filter_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.clear_filter_btn)

        self.delete_notifs_btn = QPushButton(self.notifications_buttons_frame)
        self.delete_notifs_btn.setObjectName(u"delete_notifs_btn")
        self.delete_notifs_btn.setMinimumSize(QSize(50, 50))
        self.delete_notifs_btn.setMaximumSize(QSize(50, 50))
        self.delete_notifs_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_notifs_btn.setIcon(icon6)
        self.delete_notifs_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.delete_notifs_btn)


        self.verticalLayout.addWidget(self.notifications_buttons_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.Length.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.Width.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Depth of Defect:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Length of Defect:", None))
        self.Depth.setText(QCoreApplication.translate("MainWindow", u"0 mm", None))
        self.label_Width.setText(QCoreApplication.translate("MainWindow", u"Width of Defect:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Properties of Total Defect", None))
        self.Total_Number_Defect.setText(QCoreApplication.translate("MainWindow", u"    0", None))
        self.Total_Number_Critical_defect.setText(QCoreApplication.translate("MainWindow", u"    0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Number of Critical Defect:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Number of Defect:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.live_thickness_image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.filter_btn.setText("")
        self.clear_filter_btn.setText("")
        self.delete_notifs_btn.setText("")
    # retranslateUi

