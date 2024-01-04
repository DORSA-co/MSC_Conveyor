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
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1294, 767)
        self.StyleSheet = QWidget(MainWindow)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"QTabWidget{\n"
"    font-weight: bold;\n"
"	border: None;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #C4C4C3;\n"
"    background-color: Transparent;\n"
"    margin-top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; \n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 120px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #7f9db9;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
""
                        "#side_frame{\n"
"	background-color: #17203A;\n"
"}\n"
"\n"
"#side_frame QPushButton{\n"
"	border: 0px;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#top_frame{\n"
"	background-color: #F7F8FA;\n"
"}\n"
"\n"
"#top_frame QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"#main_stackedWidget{\n"
"	background-color: #E0E4EC;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.StyleSheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_frame = QFrame(self.StyleSheet)
        self.side_frame.setObjectName(u"side_frame")
        self.side_frame.setMinimumSize(QSize(198, 0))
        self.side_frame.setMaximumSize(QSize(198, 16777215))
        self.side_frame.setFrameShape(QFrame.StyledPanel)
        self.side_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dorsa_label = QLabel(self.side_frame)
        self.dorsa_label.setObjectName(u"dorsa_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dorsa_label.sizePolicy().hasHeightForWidth())
        self.dorsa_label.setSizePolicy(sizePolicy)
        self.dorsa_label.setMinimumSize(QSize(196, 88))
        self.dorsa_label.setMaximumSize(QSize(196, 88))
        self.dorsa_label.setPixmap(QPixmap(u":/general_icons/icons/general_icons/dorsa_logo.png"))
        self.dorsa_label.setScaledContents(True)
        self.dorsa_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.dorsa_label)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.side_live_view_btn = QPushButton(self.side_frame)
        self.side_live_view_btn.setObjectName(u"side_live_view_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_live_view_btn.sizePolicy().hasHeightForWidth())
        self.side_live_view_btn.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.side_live_view_btn.setFont(font)
        self.side_live_view_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_live_view_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/general_icons/icons/general_icons/live_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_live_view_btn.setIcon(icon)
        self.side_live_view_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.side_live_view_btn)

        self.side_settings_btn = QPushButton(self.side_frame)
        self.side_settings_btn.setObjectName(u"side_settings_btn")
        sizePolicy1.setHeightForWidth(self.side_settings_btn.sizePolicy().hasHeightForWidth())
        self.side_settings_btn.setSizePolicy(sizePolicy1)
        self.side_settings_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/general_icons/icons/general_icons/settings_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_settings_btn.setIcon(icon1)
        self.side_settings_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.side_settings_btn)

        self.side_report_btn = QPushButton(self.side_frame)
        self.side_report_btn.setObjectName(u"side_report_btn")
        sizePolicy1.setHeightForWidth(self.side_report_btn.sizePolicy().hasHeightForWidth())
        self.side_report_btn.setSizePolicy(sizePolicy1)
        self.side_report_btn.setMinimumSize(QSize(0, 0))
        self.side_report_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/general_icons/icons/general_icons/report_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_report_btn.setIcon(icon2)
        self.side_report_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.side_report_btn)

        self.side_users_btn = QPushButton(self.side_frame)
        self.side_users_btn.setObjectName(u"side_users_btn")
        sizePolicy1.setHeightForWidth(self.side_users_btn.sizePolicy().hasHeightForWidth())
        self.side_users_btn.setSizePolicy(sizePolicy1)
        self.side_users_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/general_icons/icons/general_icons/users_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_users_btn.setIcon(icon3)
        self.side_users_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.side_users_btn)

        self.side_about_btn = QPushButton(self.side_frame)
        self.side_about_btn.setObjectName(u"side_about_btn")
        sizePolicy1.setHeightForWidth(self.side_about_btn.sizePolicy().hasHeightForWidth())
        self.side_about_btn.setSizePolicy(sizePolicy1)
        self.side_about_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/general_icons/icons/general_icons/about_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_about_btn.setIcon(icon4)
        self.side_about_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.side_about_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_2.setStretch(0, 11)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 10)
        self.verticalLayout_2.setStretch(3, 10)
        self.verticalLayout_2.setStretch(4, 10)
        self.verticalLayout_2.setStretch(5, 10)
        self.verticalLayout_2.setStretch(6, 10)
        self.verticalLayout_2.setStretch(7, 38)

        self.horizontalLayout.addWidget(self.side_frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.StyleSheet)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy2)
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.menu_btn = QPushButton(self.top_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy1.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy1)
        self.menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/general_icons/icons/general_icons/open_menus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon5)
        self.menu_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_14.addWidget(self.menu_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.logined_username_lbl = QLabel(self.top_frame)
        self.logined_username_lbl.setObjectName(u"logined_username_lbl")

        self.horizontalLayout_14.addWidget(self.logined_username_lbl)

        self.login_logout_btn = QPushButton(self.top_frame)
        self.login_logout_btn.setObjectName(u"login_logout_btn")
        sizePolicy1.setHeightForWidth(self.login_logout_btn.sizePolicy().hasHeightForWidth())
        self.login_logout_btn.setSizePolicy(sizePolicy1)
        self.login_logout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/general_icons/icons/general_icons/login_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_logout_btn.setIcon(icon6)
        self.login_logout_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.login_logout_btn)

        self.help_btn = QPushButton(self.top_frame)
        self.help_btn.setObjectName(u"help_btn")
        sizePolicy1.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy1)
        self.help_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/general_icons/icons/general_icons/help_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btn.setIcon(icon7)
        self.help_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_14.addWidget(self.help_btn)

        self.minimize_btn = QPushButton(self.top_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy1.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy1)
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/general_icons/icons/general_icons/minimize_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon8)
        self.minimize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.top_frame)
        self.maximize_btn.setObjectName(u"maximize_btn")
        sizePolicy1.setHeightForWidth(self.maximize_btn.sizePolicy().hasHeightForWidth())
        self.maximize_btn.setSizePolicy(sizePolicy1)
        self.maximize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/general_icons/icons/general_icons/maximize_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon9)
        self.maximize_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_14.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/general_icons/icons/general_icons/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon10)
        self.close_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_14.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_stackedWidget = QStackedWidget(self.StyleSheet)
        self.main_stackedWidget.setObjectName(u"main_stackedWidget")
        self.live_view_page = QWidget()
        self.live_view_page.setObjectName(u"live_view_page")
        self.verticalLayout_3 = QVBoxLayout(self.live_view_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.live_view_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(11, 7, 11, 21)
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
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
        icon11 = QIcon()
        icon11.addFile(u"../icons/camera_connected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop_connection.setIcon(icon11)
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
        icon12 = QIcon()
        icon12.addFile(u"../icons/camera_disconnected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Camera_connection.setIcon(icon12)
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
        icon13 = QIcon()
        icon13.addFile(u"../icons/Live00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.live.setIcon(icon13)
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
        icon14 = QIcon()
        icon14.addFile(u"../icons/stop-button2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Stop.setIcon(icon14)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Showlive.sizePolicy().hasHeightForWidth())
        self.Showlive.setSizePolicy(sizePolicy4)
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


        self.verticalLayout_3.addWidget(self.frame_6)

        self.main_stackedWidget.addWidget(self.live_view_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.horizontalLayout_3 = QHBoxLayout(self.settings_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.settings_tabs = QTabWidget(self.settings_page)
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
        icon15 = QIcon()
        icon15.addFile(u":/icons/icon/camera_disconnected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Camera_connection_Camera_setting.setIcon(icon15)
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
        self.Stop_connection_Camera_setting.setIcon(icon12)
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
        icon16 = QIcon()
        icon16.addFile(u"../icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save_Camera_Parameters.setIcon(icon16)
        self.Save_Camera_Parameters.setIconSize(QSize(26, 26))

        self.horizontalLayout_13.addWidget(self.Save_Camera_Parameters)


        self.verticalLayout_33.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_3)


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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1054, 569))
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
        self.alghoritm_background_thresh.setMaximum(255)

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
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.algorithm_image1.sizePolicy().hasHeightForWidth())
        self.algorithm_image1.setSizePolicy(sizePolicy5)

        self.verticalLayout_19.addWidget(self.algorithm_image1)


        self.horizontalLayout_19.addWidget(self.frame_36)


        self.verticalLayout_40.addWidget(self.frame_step1)

        self.frame_step2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_step2.setObjectName(u"frame_step2")
        self.frame_step2.setMaximumSize(QSize(16777215, 400))
        self.frame_step2.setStyleSheet(u"#algo_setting_step2_frame,\n"
"#frame_step2\n"
"{\n"
"border: 2 solid rgba(12, 53, 106, 100);\n"
"background-color:#ffffff;\n"
"\n"
"}\n"
"")
        self.frame_step2.setFrameShape(QFrame.StyledPanel)
        self.frame_step2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_step2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.algo_setting_step2_frame = QFrame(self.frame_step2)
        self.algo_setting_step2_frame.setObjectName(u"algo_setting_step2_frame")
        self.algo_setting_step2_frame.setStyleSheet(u"")
        self.algo_setting_step2_frame.setFrameShape(QFrame.StyledPanel)
        self.algo_setting_step2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.algo_setting_step2_frame)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_67 = QLabel(self.algo_setting_step2_frame)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(16777215, 50))
        self.label_67.setStyleSheet(u"font-size: 26px;\n"
"font-weight: bold;\n"
"color:rgb(12, 53, 106);")

        self.verticalLayout_50.addWidget(self.label_67)

        self.frame_35 = QFrame(self.algo_setting_step2_frame)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_35)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, -1, -1, 11)
        self.anomaly_alghorithm_combo = QComboBox(self.frame_35)
        self.anomaly_alghorithm_combo.setObjectName(u"anomaly_alghorithm_combo")

        self.gridLayout_10.addWidget(self.anomaly_alghorithm_combo, 0, 1, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_70 = QLabel(self.frame_35)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_11.addWidget(self.label_70, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.anomaly_thresh_error = QSpinBox(self.frame_35)
        self.anomaly_thresh_error.setObjectName(u"anomaly_thresh_error")

        self.gridLayout_10.addWidget(self.anomaly_thresh_error, 1, 1, 1, 1)

        self.label_69 = QLabel(self.frame_35)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_10.addWidget(self.label_69, 1, 0, 1, 1)


        self.verticalLayout_50.addWidget(self.frame_35)


        self.horizontalLayout_21.addWidget(self.algo_setting_step2_frame)

        self.frame_37 = QFrame(self.frame_step2)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_37)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.algorithm_image2 = QLabel(self.frame_37)
        self.algorithm_image2.setObjectName(u"algorithm_image2")
        sizePolicy5.setHeightForWidth(self.algorithm_image2.sizePolicy().hasHeightForWidth())
        self.algorithm_image2.setSizePolicy(sizePolicy5)

        self.verticalLayout_51.addWidget(self.algorithm_image2)


        self.horizontalLayout_21.addWidget(self.frame_37)


        self.verticalLayout_40.addWidget(self.frame_step2)

        self.frame_step3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_step3.setObjectName(u"frame_step3")
        self.frame_step3.setMaximumSize(QSize(16777215, 400))
        self.frame_step3.setStyleSheet(u"#algo_setting_step3_frame,\n"
"#frame_step3\n"
"{\n"
"border: 2 solid rgba(12, 53, 106, 100);\n"
"background-color:#ffffff;\n"
"\n"
"}\n"
"")
        self.frame_step3.setFrameShape(QFrame.StyledPanel)
        self.frame_step3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_step3)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.algo_setting_step3_frame = QFrame(self.frame_step3)
        self.algo_setting_step3_frame.setObjectName(u"algo_setting_step3_frame")
        self.algo_setting_step3_frame.setStyleSheet(u"")
        self.algo_setting_step3_frame.setFrameShape(QFrame.StyledPanel)
        self.algo_setting_step3_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.algo_setting_step3_frame)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_68 = QLabel(self.algo_setting_step3_frame)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(16777215, 50))
        self.label_68.setStyleSheet(u"font-size: 26px;\n"
"font-weight: bold;\n"
"color:rgb(12, 53, 106);")

        self.verticalLayout_52.addWidget(self.label_68)

        self.frame_38 = QFrame(self.algo_setting_step3_frame)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_38)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, -1, -1, 11)
        self.defect_extractor_min_width = QSpinBox(self.frame_38)
        self.defect_extractor_min_width.setObjectName(u"defect_extractor_min_width")

        self.gridLayout_12.addWidget(self.defect_extractor_min_width, 0, 1, 1, 1)

        self.label_72 = QLabel(self.frame_38)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_12.addWidget(self.label_72, 0, 0, 1, 1)


        self.verticalLayout_52.addWidget(self.frame_38)


        self.horizontalLayout_22.addWidget(self.algo_setting_step3_frame)

        self.frame_39 = QFrame(self.frame_step3)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_39)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.algorithm_image3 = QLabel(self.frame_39)
        self.algorithm_image3.setObjectName(u"algorithm_image3")
        sizePolicy5.setHeightForWidth(self.algorithm_image3.sizePolicy().hasHeightForWidth())
        self.algorithm_image3.setSizePolicy(sizePolicy5)

        self.verticalLayout_53.addWidget(self.algorithm_image3)


        self.horizontalLayout_22.addWidget(self.frame_39)


        self.verticalLayout_40.addWidget(self.frame_step3)

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
        self.Save_algorithm_setting.setIcon(icon16)
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
        self.Save_Algorithm_Parameters.setIcon(icon16)
        self.Save_Algorithm_Parameters.setIconSize(QSize(26, 26))

        self.horizontalLayout_83.addWidget(self.Save_Algorithm_Parameters)


        self.horizontalLayout_35.addWidget(self.frame_92)


        self.verticalLayout_26.addWidget(self.frame_22)


        self.horizontalLayout_16.addWidget(self.groupBox_19)

        self.settings_tabs.addTab(self.tab_11, "")

        self.horizontalLayout_3.addWidget(self.settings_tabs)

        self.main_stackedWidget.addWidget(self.settings_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.main_stackedWidget.addWidget(self.report_page)
        self.users_page = QWidget()
        self.users_page.setObjectName(u"users_page")
        self.horizontalLayout_4 = QHBoxLayout(self.users_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.user_tabs = QTabWidget(self.users_page)
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
        icon17 = QIcon()
        icon17.addFile(u":/assets/Assets/icons/icons8-plus-white-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userspage_add_user_btn.setIcon(icon17)

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
        self.userpage_editprofile_update_btn.setMaximumSize(QSize(122, 16777215))
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
        self.userpage_editprofile_change_password_btn.setMaximumSize(QSize(122, 16777215))
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

        self.horizontalLayout_4.addWidget(self.user_tabs)

        self.main_stackedWidget.addWidget(self.users_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.main_stackedWidget.addWidget(self.about_page)

        self.verticalLayout.addWidget(self.main_stackedWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.StyleSheet)

        self.retranslateUi(MainWindow)

        self.main_stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.settings_tabs.setCurrentIndex(1)
        self.user_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dorsa_label.setText("")
        self.side_live_view_btn.setText(QCoreApplication.translate("MainWindow", u" Live View  ", None))
        self.side_settings_btn.setText(QCoreApplication.translate("MainWindow", u" Settings    ", None))
        self.side_report_btn.setText(QCoreApplication.translate("MainWindow", u" Report     ", None))
        self.side_users_btn.setText(QCoreApplication.translate("MainWindow", u" Users        ", None))
        self.side_about_btn.setText(QCoreApplication.translate("MainWindow", u" About Us ", None))
        self.menu_btn.setText("")
        self.logined_username_lbl.setText("")
        self.login_logout_btn.setText("")
        self.help_btn.setText("")
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
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
        self.algorithm_image1.setText("")
        self.algorithm_image1.setProperty("abas", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Step 2", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Thresh Error", None))
        self.algorithm_image2.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Step 3", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Min Width", None))
        self.algorithm_image3.setText("")
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
    # retranslateUi

