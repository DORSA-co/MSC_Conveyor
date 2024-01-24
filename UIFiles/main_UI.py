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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from GUIComponents import (PhotoViewer, SwitchControl)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1226, 812)
        self.StyleSheet = QWidget(MainWindow)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setEnabled(True)
        self.StyleSheet.setStyleSheet(u"QLabel{\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
"QLineEdit {\n"
"  	border:1px solid #E0E4EC;\n"
"	background-color: #F7F8FA;\n"
"	border-radius: 10px;\n"
"	padding-left: 15px;\n"
"	min-height: 35px;\n"
"	min-width: 70px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
"QSpinBox, QDoubleSpinBox  \n"
"{\n"
"	background-color: transparent;\n"
"	border-bottom: 2px solid #D7D7D9;\n"
"	border-radius: None;\n"
"	font-size: 18px;\n"
"	min-height: 25px;\n"
"	min-width: 70px;\n"
"	qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"QSpinBox:disabled ,\n"
"QDoubleSpinBox:disabled \n"
"{\n"
"	border-bottom: 2px solid #F0F0F2;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow\n"
"{   \n"
"	image: url(:/icons/icons/plu"
                        "s_icon_black.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow ,  QDoubleSpinBox::down-arrow\n"
"{   \n"
"	image: url(:/icons/icons/minus_icon_black.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, QDoubleSpinBox::up-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/plus_icon_gray.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled ,  QDoubleSpinBox::down-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/minus_icon_gray.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"	border:none;\n"
"    min-width:30px;\n"
"    min-height: 29px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: right;\n"
"    top: 0px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"QSpinBox::down-button\n"
"{\n"
"    min-width:30px;\n"
"    min-height: 29px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left;\n"
"    top: 0px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"QSpinBox::up-"
                        "button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button   {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QSpinBox::up-button:disabled ,\n"
"QSpinBox::down-button:disabled ,\n"
"QDoubleSpinBox::up-button:disabled ,\n"
"QDoubleSpinBox::down-button:disabled    {\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus{\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
"QTabWidget {\n"
"    background-color: #F7F8FA;\n"
"}\n"
"\n"
"/* Tab Bar Style */\n"
"QTabBar::tab {\n"
"    background-color: #BDBDBF;\n"
"    color: rgb(20, 20, 20);\n"
"	min-width: 100px;\n"
"    padding: 8px 16px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #D7D7D9;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"/* Tab Content Area */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #E0E4EC;\n"
"    bo"
                        "rder-top: none;\n"
"    background-color: #E0E4EC;\n"
"}\n"
"\n"
"/* Selected Tab Label Style */\n"
"QTabBar::tab:selected {\n"
"    background-color: #E0E4EC;\n"
"    border-bottom: 2px solid #7892DF; /* Change the color of the selected tab indicator */\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
"QTableWidget {\n"
"    background-color: #F7F8FA;\n"
"	gridline-color: #D7D7D9;\n"
"	color: rgb(20, 20, 20);\n"
"	border: 2px solid #F7F8FA;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F7F8FA;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom: 2px solid #BDBDBF;\n"
"	border-right: 1px solid #D7D7D9;\n"
"	font-weight: bold;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"   border-top-left-radius: 4px;\n"
"	border-left: None;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"   border-top-right-radius: 4px;\n"
"	border-right: None;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
""
                        "    background-color: #E0E4EC;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #D7D7D9;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	\n"
"	image: url(:/icons/icons/table_sort_icon.png);\n"
"}\n"
"\n"
"/*QScrollBar:horizontal, QScrollBar:vertical {\n"
"    border: 1px solid #BDBDBF;\n"
"    background: #BDBDBF;\n"
"    height: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal, QScrollBar::handle:vertical {\n"
"    background: #646466;\n"
"}\n"
"*/\n"
"\n"
"/************************************************************/\n"
"\n"
"QComboBox\n"
"{\n"
"	border:1px solid #E0E4EC;\n"
"	background-color: #F7F8FA;\n"
"	border-radius: 10px;\n"
"	padding-left: 15px;\n"
"	min-height: 35px;\n"
"	min-width: 70px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QComboBox:enabled{\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QComboBox:disabled\n"
"{\n"
"	border: 2px solid #F0F0F2;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/ic"
                        "ons/down_icon_gray.png);\n"
"	width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{   \n"
"	image: url(:/icons/icons/down_icon_black.png);\n"
"	width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding; \n"
"    subcontrol-position: bottom right;\n"
"    width: 30px; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px; \n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"    border-left: 5px solid #7892DF;\n"
"	background-color: #D7D7D9;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #F7F8FA;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
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
"	bor"
                        "der: 0px;\n"
"}\n"
"\n"
"#main_stackedWidget{\n"
"	background-color: #E0E4EC;\n"
"}\n"
"\n"
"#camera_tab .QFrame, #algorithm_stackedWidget .QFrame, #user_register_tab .QFrame, #user_profile_tab .QFrame{\n"
"	background-color: #F7F8FA;\n"
"	border:1px solid #D7D7D9;\n"
"}\n"
"\n"
"#camera_settings_frame .QLabel, #register_info_frame .QLabel,\n"
"#profile_change_username_frame .QLabel,\n"
"#profile_change_password_frame .QLabel\n"
"{\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"#connect_camera_switch::indicator{\n"
"	border: None;\n"
"}\n"
"\n"
"#save_camera_settings, #save_algorithm_settings, #register_user\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 22px;\n"
"	min-width: 200;\n"
"	max-width: 200;\n"
"	min-height: 44;\n"
"	max-height: 44;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#save_camera_settings:hover, #save"
                        "_algorithm_settings:hover, #register_user:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));\n"
"}\n"
"\n"
"#save_camera_settings:pressed, #save_algorithm_settings:pressed, #register_user:pressed {\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"#step1_settings_frame .QLabel, #step2_settings_frame .QLabel, #step3_settings_frame .QLabel\n"
"{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#step1_label, #step2_label, #step3_label{\n"
"	font-size: 26px;\n"
"	color: #4C7EFF;\n"
"}\n"
"\n"
"#show_steps_frame{\n"
"	border: None;\n"
"}\n"
"\n"
"#show_steps_frame .QPushButton{\n"
"	background-color: transparent;\n"
"	border:5px solid #7E84A2;\n"
"	border-radius: 32px;\n"
"	min-width: 55px;\n"
"	max-width: 55px;\n"
"	min-height: 55px;\n"
"	max-height: 55px;\n"
"	font-size: 24px;\n"
"	color: rgb(20, 20, 20);\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#show_steps_frame .QPushButton:hover{\n"
"	border:5px solid #BDBDBF"
                        ";\n"
"}\n"
"\n"
"#show_steps_frame .QFrame{\n"
"	border: 2px solid #7E84A2;\n"
"	min-height: 0px;\n"
"	max-height: 0px;\n"
"}\n"
"\n"
"#userspage_user_heading_lbl{\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"	color: #4C7EFF;\n"
"	min-height: 70px;\n"
"}\n"
"\n"
"#profile_change_username_label, #profile_change_password_label{\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"	color: #4C7EFF;\n"
"}\n"
"\n"
"#userpage_editprofile_change_username_btn,\n"
"#userpage_editprofile_change_password_btn\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 15px;\n"
"	min-width: 150;\n"
"	max-width: 150;\n"
"	min-height: 30;\n"
"	max-height: 30;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#userpage_editprofile_change_username_btn:hover,\n"
"#userpage_editprofile_change_password_btn:hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1"
                        ":0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));\n"
"}\n"
"\n"
"#userpage_editprofile_change_username_btn:pressed \n"
"#userpage_editprofile_change_password_btn:pressed\n"
"{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"#userpage_password_eye,\n"
"#userpage_confirm_password_eye,\n"
"#userpage_editprofile_old_password_eye,\n"
"#userpage_editprofile_new_password_eye,\n"
"#userpage_editprofile_confirm_new_password_eye\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:1px solid #E0E4EC;\n"
"	background-color: #F7F8FA;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-left: None;\n"
"	padding-right: 3px;\n"
"}\n"
"\n"
"#userpage_password_inpt,\n"
"#userpage_confirm_password_inpt,\n"
"#userpage_editprofile_old_password_inpt,\n"
"#userpage_editprofile_new_password_inpt,\n"
"#userpage_editprofile_confirm_new_password_inpt\n"
"{\n"
"	border-right: None;\n"
"	border-top-right-r"
                        "adius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"#register_message_scrollArea, \n"
"#change_username_message_scrollArea,\n"
"#change_password_message_scrollArea\n"
"{\n"
"	border: None;\n"
"}\n"
"\n"
"#register_message_frame, \n"
"#change_username_message_frame,\n"
"#change_password_message_frame\n"
"{\n"
"	background-color: #F7F8FA;\n"
"}\n"
"\n"
"#defects_notifications_widget{\n"
"	background-color: #F7F8FA;\n"
"	border:1px solid #D7D7D9;\n"
"}\n"
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
        self.dorsa_label.setPixmap(QPixmap(u":/icons/icons/dorsa_logo.png"))
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
        icon.addFile(u":/icons/icons/live_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_live_view_btn.setIcon(icon)
        self.side_live_view_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.side_live_view_btn)

        self.side_settings_btn = QPushButton(self.side_frame)
        self.side_settings_btn.setObjectName(u"side_settings_btn")
        sizePolicy1.setHeightForWidth(self.side_settings_btn.sizePolicy().hasHeightForWidth())
        self.side_settings_btn.setSizePolicy(sizePolicy1)
        self.side_settings_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/settings_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u":/icons/icons/report_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_report_btn.setIcon(icon2)
        self.side_report_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.side_report_btn)

        self.side_users_btn = QPushButton(self.side_frame)
        self.side_users_btn.setObjectName(u"side_users_btn")
        sizePolicy1.setHeightForWidth(self.side_users_btn.sizePolicy().hasHeightForWidth())
        self.side_users_btn.setSizePolicy(sizePolicy1)
        self.side_users_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/users_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_users_btn.setIcon(icon3)
        self.side_users_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.side_users_btn)

        self.side_about_btn = QPushButton(self.side_frame)
        self.side_about_btn.setObjectName(u"side_about_btn")
        sizePolicy1.setHeightForWidth(self.side_about_btn.sizePolicy().hasHeightForWidth())
        self.side_about_btn.setSizePolicy(sizePolicy1)
        self.side_about_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/about_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon5.addFile(u":/icons/icons/open_menus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon6.addFile(u":/icons/icons/login_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_logout_btn.setIcon(icon6)
        self.login_logout_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.login_logout_btn)

        self.help_btn = QPushButton(self.top_frame)
        self.help_btn.setObjectName(u"help_btn")
        sizePolicy1.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy1)
        self.help_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/help_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btn.setIcon(icon7)
        self.help_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_14.addWidget(self.help_btn)

        self.minimize_btn = QPushButton(self.top_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy1.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy1)
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/minus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon8)
        self.minimize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.top_frame)
        self.maximize_btn.setObjectName(u"maximize_btn")
        sizePolicy1.setHeightForWidth(self.maximize_btn.sizePolicy().hasHeightForWidth())
        self.maximize_btn.setSizePolicy(sizePolicy1)
        self.maximize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon9)
        self.maximize_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon10)
        self.close_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_14.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_stackedWidget = QStackedWidget(self.StyleSheet)
        self.main_stackedWidget.setObjectName(u"main_stackedWidget")
        self.live_view_page = QWidget()
        self.live_view_page.setObjectName(u"live_view_page")
        self.horizontalLayout_2 = QHBoxLayout(self.live_view_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.defect_notifications_frame = QFrame(self.live_view_page)
        self.defect_notifications_frame.setObjectName(u"defect_notifications_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.defect_notifications_frame.sizePolicy().hasHeightForWidth())
        self.defect_notifications_frame.setSizePolicy(sizePolicy3)
        self.defect_notifications_frame.setMinimumSize(QSize(320, 0))
        self.defect_notifications_frame.setMaximumSize(QSize(320, 16777215))
        self.defect_notifications_frame.setFrameShape(QFrame.StyledPanel)
        self.defect_notifications_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.defect_notifications_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.defect_notifications_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame)

        self.defects_notifications_scrollArea = QScrollArea(self.defect_notifications_frame)
        self.defects_notifications_scrollArea.setObjectName(u"defects_notifications_scrollArea")
        self.defects_notifications_scrollArea.setMinimumSize(QSize(0, 0))
        self.defects_notifications_scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.defects_notifications_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.defects_notifications_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.defects_notifications_scrollArea.setWidgetResizable(True)
        self.defects_notifications_widget = QWidget()
        self.defects_notifications_widget.setObjectName(u"defects_notifications_widget")
        self.defects_notifications_widget.setGeometry(QRect(0, 0, 302, 680))
        self.verticalLayout_9 = QVBoxLayout(self.defects_notifications_widget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.defects_notifications_scrollArea.setWidget(self.defects_notifications_widget)

        self.verticalLayout_3.addWidget(self.defects_notifications_scrollArea)

        self.frame_2 = QFrame(self.defect_notifications_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.defect_notifications_frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.main_stackedWidget.addWidget(self.live_view_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.horizontalLayout_3 = QHBoxLayout(self.settings_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.settings_tabs = QTabWidget(self.settings_page)
        self.settings_tabs.setObjectName(u"settings_tabs")
        self.camera_tab = QWidget()
        self.camera_tab.setObjectName(u"camera_tab")
        self.horizontalLayout_7 = QHBoxLayout(self.camera_tab)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.camera_settings_frame = QFrame(self.camera_tab)
        self.camera_settings_frame.setObjectName(u"camera_settings_frame")
        self.camera_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.camera_settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.camera_settings_frame)
        self.verticalLayout_24.setSpacing(12)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(20, 11, 20, 10)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.camera_settings_off_label = QLabel(self.camera_settings_frame)
        self.camera_settings_off_label.setObjectName(u"camera_settings_off_label")
        sizePolicy2.setHeightForWidth(self.camera_settings_off_label.sizePolicy().hasHeightForWidth())
        self.camera_settings_off_label.setSizePolicy(sizePolicy2)
        self.camera_settings_off_label.setFont(font)
        self.camera_settings_off_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.camera_settings_off_label)

        self.connect_camera_switch = SwitchControl(self.camera_settings_frame)
        self.connect_camera_switch.setObjectName(u"connect_camera_switch")
        self.connect_camera_switch.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.connect_camera_switch)

        self.camera_settings_on_label = QLabel(self.camera_settings_frame)
        self.camera_settings_on_label.setObjectName(u"camera_settings_on_label")
        self.camera_settings_on_label.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.camera_settings_on_label.sizePolicy().hasHeightForWidth())
        self.camera_settings_on_label.setSizePolicy(sizePolicy2)
        self.camera_settings_on_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.camera_settings_on_label)


        self.verticalLayout_24.addLayout(self.horizontalLayout_8)

        self.line = QFrame(self.camera_settings_frame)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 2))
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_24.addWidget(self.line)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.camera_settings_camera_label = QLabel(self.camera_settings_frame)
        self.camera_settings_camera_label.setObjectName(u"camera_settings_camera_label")
        self.camera_settings_camera_label.setFont(font)

        self.verticalLayout_21.addWidget(self.camera_settings_camera_label)

        self.comboBox = QComboBox(self.camera_settings_frame)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_21.addWidget(self.comboBox)


        self.verticalLayout_24.addLayout(self.verticalLayout_21)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.camera_settings_serial_label = QLabel(self.camera_settings_frame)
        self.camera_settings_serial_label.setObjectName(u"camera_settings_serial_label")
        self.camera_settings_serial_label.setFont(font)

        self.verticalLayout_23.addWidget(self.camera_settings_serial_label)

        self.devices_sn_combobox = QComboBox(self.camera_settings_frame)
        self.devices_sn_combobox.setObjectName(u"devices_sn_combobox")

        self.verticalLayout_23.addWidget(self.devices_sn_combobox)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.camera_settings_gain_label = QLabel(self.camera_settings_frame)
        self.camera_settings_gain_label.setObjectName(u"camera_settings_gain_label")
        self.camera_settings_gain_label.setFont(font)
        self.camera_settings_gain_label.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.camera_settings_gain_label)

        self.gain_spinbox = QSpinBox(self.camera_settings_frame)
        self.gain_spinbox.setObjectName(u"gain_spinbox")
        self.gain_spinbox.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.gain_spinbox)


        self.verticalLayout_24.addLayout(self.verticalLayout_6)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.camera_settings_width_label = QLabel(self.camera_settings_frame)
        self.camera_settings_width_label.setObjectName(u"camera_settings_width_label")
        self.camera_settings_width_label.setEnabled(True)
        self.camera_settings_width_label.setFont(font)
        self.camera_settings_width_label.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.camera_settings_width_label)

        self.width_spinbox = QSpinBox(self.camera_settings_frame)
        self.width_spinbox.setObjectName(u"width_spinbox")
        self.width_spinbox.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.width_spinbox)


        self.verticalLayout_24.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.camera_settings_height_label = QLabel(self.camera_settings_frame)
        self.camera_settings_height_label.setObjectName(u"camera_settings_height_label")
        self.camera_settings_height_label.setFont(font)
        self.camera_settings_height_label.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.camera_settings_height_label)

        self.height_spinbox = QSpinBox(self.camera_settings_frame)
        self.height_spinbox.setObjectName(u"height_spinbox")
        self.height_spinbox.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.height_spinbox)


        self.verticalLayout_24.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.camera_settings_exposure_label = QLabel(self.camera_settings_frame)
        self.camera_settings_exposure_label.setObjectName(u"camera_settings_exposure_label")
        self.camera_settings_exposure_label.setFont(font)
        self.camera_settings_exposure_label.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.camera_settings_exposure_label)

        self.expo_spinbox = QSpinBox(self.camera_settings_frame)
        self.expo_spinbox.setObjectName(u"expo_spinbox")
        self.expo_spinbox.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.expo_spinbox)


        self.verticalLayout_24.addLayout(self.verticalLayout_12)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.camera_settings_offsetx_label = QLabel(self.camera_settings_frame)
        self.camera_settings_offsetx_label.setObjectName(u"camera_settings_offsetx_label")
        self.camera_settings_offsetx_label.setFont(font)
        self.camera_settings_offsetx_label.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.camera_settings_offsetx_label)

        self.offsetx_spinbox = QSpinBox(self.camera_settings_frame)
        self.offsetx_spinbox.setObjectName(u"offsetx_spinbox")
        self.offsetx_spinbox.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.offsetx_spinbox)


        self.verticalLayout_24.addLayout(self.verticalLayout_14)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.camera_settings_offsety_label = QLabel(self.camera_settings_frame)
        self.camera_settings_offsety_label.setObjectName(u"camera_settings_offsety_label")
        self.camera_settings_offsety_label.setFont(font)
        self.camera_settings_offsety_label.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.camera_settings_offsety_label)

        self.offsety_spinbox = QSpinBox(self.camera_settings_frame)
        self.offsety_spinbox.setObjectName(u"offsety_spinbox")
        self.offsety_spinbox.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.offsety_spinbox)


        self.verticalLayout_24.addLayout(self.verticalLayout_20)

        self.save_camera_settings = QPushButton(self.camera_settings_frame)
        self.save_camera_settings.setObjectName(u"save_camera_settings")
        sizePolicy1.setHeightForWidth(self.save_camera_settings.sizePolicy().hasHeightForWidth())
        self.save_camera_settings.setSizePolicy(sizePolicy1)
        self.save_camera_settings.setFont(font)
        self.save_camera_settings.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.save_camera_settings, 0, Qt.AlignHCenter)

        self.label = QLabel(self.camera_settings_frame)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout_24.addWidget(self.label)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_9)


        self.horizontalLayout_7.addWidget(self.camera_settings_frame)

        self.camera_live_frame = QFrame(self.camera_tab)
        self.camera_live_frame.setObjectName(u"camera_live_frame")
        self.camera_live_frame.setFrameShape(QFrame.StyledPanel)
        self.camera_live_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_live_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_settings_live_view = PhotoViewer(self.camera_live_frame)
        self.camera_settings_live_view.setObjectName(u"camera_settings_live_view")

        self.verticalLayout_8.addWidget(self.camera_settings_live_view)

        self.camera_settings_live_label = QLabel(self.camera_live_frame)
        self.camera_settings_live_label.setObjectName(u"camera_settings_live_label")

        self.verticalLayout_8.addWidget(self.camera_settings_live_label)


        self.horizontalLayout_7.addWidget(self.camera_live_frame)

        self.horizontalLayout_7.setStretch(0, 25)
        self.horizontalLayout_7.setStretch(1, 75)
        self.settings_tabs.addTab(self.camera_tab, "")
        self.algorithm_tab = QWidget()
        self.algorithm_tab.setObjectName(u"algorithm_tab")
        self.verticalLayout_4 = QVBoxLayout(self.algorithm_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.show_steps_frame = QFrame(self.algorithm_tab)
        self.show_steps_frame.setObjectName(u"show_steps_frame")
        self.show_steps_frame.setMinimumSize(QSize(0, 100))
        self.show_steps_frame.setFrameShape(QFrame.StyledPanel)
        self.show_steps_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.show_steps_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.step1_btn = QPushButton(self.show_steps_frame)
        self.step1_btn.setObjectName(u"step1_btn")
        self.step1_btn.setFont(font)
        self.step1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.step1_btn.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.step1_btn)

        self.frame_3 = QFrame(self.show_steps_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 4))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_3)

        self.step2_btn = QPushButton(self.show_steps_frame)
        self.step2_btn.setObjectName(u"step2_btn")
        self.step2_btn.setFont(font)
        self.step2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.step2_btn.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.step2_btn)

        self.frame_4 = QFrame(self.show_steps_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_4)

        self.step3_btn = QPushButton(self.show_steps_frame)
        self.step3_btn.setObjectName(u"step3_btn")
        self.step3_btn.setFont(font)
        self.step3_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.step3_btn)


        self.verticalLayout_4.addWidget(self.show_steps_frame)

        self.algorithm_stackedWidget = QStackedWidget(self.algorithm_tab)
        self.algorithm_stackedWidget.setObjectName(u"algorithm_stackedWidget")
        self.step1 = QWidget()
        self.step1.setObjectName(u"step1")
        self.horizontalLayout_6 = QHBoxLayout(self.step1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.step1_settings_frame = QFrame(self.step1)
        self.step1_settings_frame.setObjectName(u"step1_settings_frame")
        self.step1_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.step1_settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.step1_settings_frame)
        self.verticalLayout_28.setSpacing(50)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(20, 15, 20, -1)
        self.step1_label = QLabel(self.step1_settings_frame)
        self.step1_label.setObjectName(u"step1_label")
        sizePolicy.setHeightForWidth(self.step1_label.sizePolicy().hasHeightForWidth())
        self.step1_label.setSizePolicy(sizePolicy)
        self.step1_label.setStyleSheet(u"border-bottom: 2px solid #D7D7D9;")

        self.verticalLayout_28.addWidget(self.step1_label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.background_th_label = QLabel(self.step1_settings_frame)
        self.background_th_label.setObjectName(u"background_th_label")
        sizePolicy2.setHeightForWidth(self.background_th_label.sizePolicy().hasHeightForWidth())
        self.background_th_label.setSizePolicy(sizePolicy2)
        self.background_th_label.setFont(font)

        self.verticalLayout_5.addWidget(self.background_th_label)

        self.alghoritm_background_thresh = QSpinBox(self.step1_settings_frame)
        self.alghoritm_background_thresh.setObjectName(u"alghoritm_background_thresh")
        self.alghoritm_background_thresh.setEnabled(True)
        self.alghoritm_background_thresh.setStyleSheet(u"")
        self.alghoritm_background_thresh.setAlignment(Qt.AlignCenter)
        self.alghoritm_background_thresh.setMaximum(255)

        self.verticalLayout_5.addWidget(self.alghoritm_background_thresh)


        self.verticalLayout_28.addLayout(self.verticalLayout_5)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.conv_wsize_label = QLabel(self.step1_settings_frame)
        self.conv_wsize_label.setObjectName(u"conv_wsize_label")
        sizePolicy2.setHeightForWidth(self.conv_wsize_label.sizePolicy().hasHeightForWidth())
        self.conv_wsize_label.setSizePolicy(sizePolicy2)
        self.conv_wsize_label.setFont(font)

        self.verticalLayout_13.addWidget(self.conv_wsize_label)

        self.alghoritm_conv_window_size = QSpinBox(self.step1_settings_frame)
        self.alghoritm_conv_window_size.setObjectName(u"alghoritm_conv_window_size")
        self.alghoritm_conv_window_size.setEnabled(True)
        self.alghoritm_conv_window_size.setStyleSheet(u"")
        self.alghoritm_conv_window_size.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.alghoritm_conv_window_size)


        self.verticalLayout_28.addLayout(self.verticalLayout_13)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_3)


        self.horizontalLayout_6.addWidget(self.step1_settings_frame)

        self.step1_image_frame = QFrame(self.step1)
        self.step1_image_frame.setObjectName(u"step1_image_frame")
        self.step1_image_frame.setFrameShape(QFrame.StyledPanel)
        self.step1_image_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.step1_image_frame)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.algorithm_image1 = QLabel(self.step1_image_frame)
        self.algorithm_image1.setObjectName(u"algorithm_image1")

        self.verticalLayout_29.addWidget(self.algorithm_image1)


        self.horizontalLayout_6.addWidget(self.step1_image_frame)

        self.horizontalLayout_6.setStretch(0, 25)
        self.horizontalLayout_6.setStretch(1, 75)
        self.algorithm_stackedWidget.addWidget(self.step1)
        self.step2 = QWidget()
        self.step2.setObjectName(u"step2")
        self.horizontalLayout_9 = QHBoxLayout(self.step2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.step2_settings_frame = QFrame(self.step2)
        self.step2_settings_frame.setObjectName(u"step2_settings_frame")
        self.step2_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.step2_settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.step2_settings_frame)
        self.verticalLayout_33.setSpacing(50)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(20, 15, 20, -1)
        self.step2_label = QLabel(self.step2_settings_frame)
        self.step2_label.setObjectName(u"step2_label")
        sizePolicy.setHeightForWidth(self.step2_label.sizePolicy().hasHeightForWidth())
        self.step2_label.setSizePolicy(sizePolicy)
        self.step2_label.setStyleSheet(u"border-bottom: 2px solid #D7D7D9;")

        self.verticalLayout_33.addWidget(self.step2_label)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(7)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.algorithm_label = QLabel(self.step2_settings_frame)
        self.algorithm_label.setObjectName(u"algorithm_label")

        self.verticalLayout_31.addWidget(self.algorithm_label)

        self.anomaly_alghorithm_combo = QComboBox(self.step2_settings_frame)
        self.anomaly_alghorithm_combo.setObjectName(u"anomaly_alghorithm_combo")
        self.anomaly_alghorithm_combo.setEnabled(True)
        self.anomaly_alghorithm_combo.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.anomaly_alghorithm_combo)


        self.verticalLayout_33.addLayout(self.verticalLayout_31)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(7)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.thresh_error_label = QLabel(self.step2_settings_frame)
        self.thresh_error_label.setObjectName(u"thresh_error_label")

        self.verticalLayout_32.addWidget(self.thresh_error_label)

        self.anomaly_thresh_error = QSpinBox(self.step2_settings_frame)
        self.anomaly_thresh_error.setObjectName(u"anomaly_thresh_error")
        self.anomaly_thresh_error.setEnabled(True)
        self.anomaly_thresh_error.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.anomaly_thresh_error)


        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_4)


        self.horizontalLayout_9.addWidget(self.step2_settings_frame)

        self.step2_image_frame = QFrame(self.step2)
        self.step2_image_frame.setObjectName(u"step2_image_frame")
        self.step2_image_frame.setFrameShape(QFrame.StyledPanel)
        self.step2_image_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.step2_image_frame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.algorithm_image2 = QLabel(self.step2_image_frame)
        self.algorithm_image2.setObjectName(u"algorithm_image2")

        self.verticalLayout_34.addWidget(self.algorithm_image2)


        self.horizontalLayout_9.addWidget(self.step2_image_frame)

        self.horizontalLayout_9.setStretch(0, 25)
        self.horizontalLayout_9.setStretch(1, 75)
        self.algorithm_stackedWidget.addWidget(self.step2)
        self.step3 = QWidget()
        self.step3.setObjectName(u"step3")
        self.horizontalLayout_11 = QHBoxLayout(self.step3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.step3_settings_frame = QFrame(self.step3)
        self.step3_settings_frame.setObjectName(u"step3_settings_frame")
        self.step3_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.step3_settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.step3_settings_frame)
        self.verticalLayout_36.setSpacing(50)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(20, 15, 20, -1)
        self.step3_label = QLabel(self.step3_settings_frame)
        self.step3_label.setObjectName(u"step3_label")
        sizePolicy.setHeightForWidth(self.step3_label.sizePolicy().hasHeightForWidth())
        self.step3_label.setSizePolicy(sizePolicy)
        self.step3_label.setStyleSheet(u"border-bottom: 2px solid #D7D7D9;")

        self.verticalLayout_36.addWidget(self.step3_label)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(7)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_72 = QLabel(self.step3_settings_frame)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_35.addWidget(self.label_72)

        self.defect_extractor_min_width = QSpinBox(self.step3_settings_frame)
        self.defect_extractor_min_width.setObjectName(u"defect_extractor_min_width")
        self.defect_extractor_min_width.setStyleSheet(u"")
        self.defect_extractor_min_width.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.defect_extractor_min_width)


        self.verticalLayout_36.addLayout(self.verticalLayout_35)

        self.verticalSpacer_6 = QSpacerItem(20, 296, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_6)


        self.horizontalLayout_11.addWidget(self.step3_settings_frame)

        self.step3_image_frame = QFrame(self.step3)
        self.step3_image_frame.setObjectName(u"step3_image_frame")
        self.step3_image_frame.setFrameShape(QFrame.StyledPanel)
        self.step3_image_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.step3_image_frame)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.algorithm_image3 = QLabel(self.step3_image_frame)
        self.algorithm_image3.setObjectName(u"algorithm_image3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.algorithm_image3.sizePolicy().hasHeightForWidth())
        self.algorithm_image3.setSizePolicy(sizePolicy4)

        self.verticalLayout_40.addWidget(self.algorithm_image3)


        self.horizontalLayout_11.addWidget(self.step3_image_frame)

        self.horizontalLayout_11.setStretch(0, 25)
        self.horizontalLayout_11.setStretch(1, 75)
        self.algorithm_stackedWidget.addWidget(self.step3)

        self.verticalLayout_4.addWidget(self.algorithm_stackedWidget)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.save_algorithm_settings = QPushButton(self.algorithm_tab)
        self.save_algorithm_settings.setObjectName(u"save_algorithm_settings")
        sizePolicy1.setHeightForWidth(self.save_algorithm_settings.sizePolicy().hasHeightForWidth())
        self.save_algorithm_settings.setSizePolicy(sizePolicy1)
        self.save_algorithm_settings.setMinimumSize(QSize(200, 44))
        self.save_algorithm_settings.setMaximumSize(QSize(200, 44))
        self.save_algorithm_settings.setFont(font)
        self.save_algorithm_settings.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.save_algorithm_settings)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.settings_tabs.addTab(self.algorithm_tab, "")

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
        self.user_tabs.setStyleSheet(u"")
        self.user_register_tab = QWidget()
        self.user_register_tab.setObjectName(u"user_register_tab")
        self.verticalLayout_41 = QVBoxLayout(self.user_register_tab)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.register_info_frame = QFrame(self.user_register_tab)
        self.register_info_frame.setObjectName(u"register_info_frame")
        self.register_info_frame.setFrameShape(QFrame.StyledPanel)
        self.register_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.register_info_frame)
        self.verticalLayout_30.setSpacing(20)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(20, 20, 20, -1)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.register_username_label = QLabel(self.register_info_frame)
        self.register_username_label.setObjectName(u"register_username_label")

        self.verticalLayout_19.addWidget(self.register_username_label)

        self.userpage_username_inpt = QLineEdit(self.register_info_frame)
        self.userpage_username_inpt.setObjectName(u"userpage_username_inpt")

        self.verticalLayout_19.addWidget(self.userpage_username_inpt)


        self.verticalLayout_30.addLayout(self.verticalLayout_19)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.register_password_label = QLabel(self.register_info_frame)
        self.register_password_label.setObjectName(u"register_password_label")

        self.verticalLayout_25.addWidget(self.register_password_label)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.userpage_password_inpt = QLineEdit(self.register_info_frame)
        self.userpage_password_inpt.setObjectName(u"userpage_password_inpt")

        self.horizontalLayout_21.addWidget(self.userpage_password_inpt)

        self.userpage_password_eye = QPushButton(self.register_info_frame)
        self.userpage_password_eye.setObjectName(u"userpage_password_eye")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.userpage_password_eye.sizePolicy().hasHeightForWidth())
        self.userpage_password_eye.setSizePolicy(sizePolicy5)
        self.userpage_password_eye.setCursor(QCursor(Qt.PointingHandCursor))
        self.userpage_password_eye.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/black_eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userpage_password_eye.setIcon(icon11)

        self.horizontalLayout_21.addWidget(self.userpage_password_eye)


        self.verticalLayout_25.addLayout(self.horizontalLayout_21)


        self.verticalLayout_30.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.register_confirm_password_label = QLabel(self.register_info_frame)
        self.register_confirm_password_label.setObjectName(u"register_confirm_password_label")

        self.verticalLayout_26.addWidget(self.register_confirm_password_label)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.userpage_confirm_password_inpt = QLineEdit(self.register_info_frame)
        self.userpage_confirm_password_inpt.setObjectName(u"userpage_confirm_password_inpt")
        self.userpage_confirm_password_inpt.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.userpage_confirm_password_inpt)

        self.userpage_confirm_password_eye = QPushButton(self.register_info_frame)
        self.userpage_confirm_password_eye.setObjectName(u"userpage_confirm_password_eye")
        sizePolicy5.setHeightForWidth(self.userpage_confirm_password_eye.sizePolicy().hasHeightForWidth())
        self.userpage_confirm_password_eye.setSizePolicy(sizePolicy5)
        self.userpage_confirm_password_eye.setCursor(QCursor(Qt.PointingHandCursor))
        self.userpage_confirm_password_eye.setStyleSheet(u"")
        self.userpage_confirm_password_eye.setIcon(icon11)

        self.horizontalLayout_22.addWidget(self.userpage_confirm_password_eye)


        self.verticalLayout_26.addLayout(self.horizontalLayout_22)


        self.verticalLayout_30.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.register_user_role_label = QLabel(self.register_info_frame)
        self.register_user_role_label.setObjectName(u"register_user_role_label")

        self.verticalLayout_27.addWidget(self.register_user_role_label)

        self.userpage_user_role_combobox = QComboBox(self.register_info_frame)
        self.userpage_user_role_combobox.setObjectName(u"userpage_user_role_combobox")

        self.verticalLayout_27.addWidget(self.userpage_user_role_combobox)


        self.verticalLayout_30.addLayout(self.verticalLayout_27)

        self.register_user = QPushButton(self.register_info_frame)
        self.register_user.setObjectName(u"register_user")
        self.register_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_user.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/assets/Assets/icons/icons8-plus-white-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.register_user.setIcon(icon12)

        self.verticalLayout_30.addWidget(self.register_user, 0, Qt.AlignHCenter)

        self.register_message_scrollArea = QScrollArea(self.register_info_frame)
        self.register_message_scrollArea.setObjectName(u"register_message_scrollArea")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.register_message_scrollArea.sizePolicy().hasHeightForWidth())
        self.register_message_scrollArea.setSizePolicy(sizePolicy6)
        self.register_message_scrollArea.setWidgetResizable(True)
        self.register_message_frame = QWidget()
        self.register_message_frame.setObjectName(u"register_message_frame")
        self.register_message_frame.setGeometry(QRect(0, 0, 946, 223))
        sizePolicy3.setHeightForWidth(self.register_message_frame.sizePolicy().hasHeightForWidth())
        self.register_message_frame.setSizePolicy(sizePolicy3)
        self.verticalLayout_55 = QVBoxLayout(self.register_message_frame)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_5)

        self.register_message_scrollArea.setWidget(self.register_message_frame)

        self.verticalLayout_30.addWidget(self.register_message_scrollArea)


        self.verticalLayout_41.addWidget(self.register_info_frame)

        self.user_tabs.addTab(self.user_register_tab, "")
        self.user_profile_tab = QWidget()
        self.user_profile_tab.setObjectName(u"user_profile_tab")
        self.horizontalLayout_20 = QHBoxLayout(self.user_profile_tab)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.profile_change_username_title_frame = QFrame(self.user_profile_tab)
        self.profile_change_username_title_frame.setObjectName(u"profile_change_username_title_frame")
        self.profile_change_username_title_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_change_username_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.profile_change_username_title_frame)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.profile_change_username_label = QLabel(self.profile_change_username_title_frame)
        self.profile_change_username_label.setObjectName(u"profile_change_username_label")
        self.profile_change_username_label.setFont(font)
        self.profile_change_username_label.setStyleSheet(u"")

        self.verticalLayout_53.addWidget(self.profile_change_username_label)


        self.verticalLayout_52.addWidget(self.profile_change_username_title_frame)

        self.profile_change_username_frame = QFrame(self.user_profile_tab)
        self.profile_change_username_frame.setObjectName(u"profile_change_username_frame")
        self.profile_change_username_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_change_username_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.profile_change_username_frame)
        self.verticalLayout_54.setSpacing(20)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(20, 20, 20, -1)
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(6)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.profile_old_username_label = QLabel(self.profile_change_username_frame)
        self.profile_old_username_label.setObjectName(u"profile_old_username_label")
        self.profile_old_username_label.setLayoutDirection(Qt.LeftToRight)
        self.profile_old_username_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_46.addWidget(self.profile_old_username_label)

        self.userpage_editprofile_username_inpt = QLineEdit(self.profile_change_username_frame)
        self.userpage_editprofile_username_inpt.setObjectName(u"userpage_editprofile_username_inpt")
        self.userpage_editprofile_username_inpt.setEnabled(False)

        self.verticalLayout_46.addWidget(self.userpage_editprofile_username_inpt)


        self.verticalLayout_54.addLayout(self.verticalLayout_46)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.profile_username_label = QLabel(self.profile_change_username_frame)
        self.profile_username_label.setObjectName(u"profile_username_label")
        self.profile_username_label.setLayoutDirection(Qt.LeftToRight)
        self.profile_username_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_42.addWidget(self.profile_username_label)

        self.userpage_editprofile_new_username_inpt = QLineEdit(self.profile_change_username_frame)
        self.userpage_editprofile_new_username_inpt.setObjectName(u"userpage_editprofile_new_username_inpt")

        self.verticalLayout_42.addWidget(self.userpage_editprofile_new_username_inpt)


        self.verticalLayout_54.addLayout(self.verticalLayout_42)

        self.userpage_editprofile_change_username_btn = QPushButton(self.profile_change_username_frame)
        self.userpage_editprofile_change_username_btn.setObjectName(u"userpage_editprofile_change_username_btn")
        self.userpage_editprofile_change_username_btn.setMinimumSize(QSize(150, 30))
        self.userpage_editprofile_change_username_btn.setMaximumSize(QSize(150, 30))
        self.userpage_editprofile_change_username_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.userpage_editprofile_change_username_btn.setStyleSheet(u"")

        self.verticalLayout_54.addWidget(self.userpage_editprofile_change_username_btn, 0, Qt.AlignHCenter)

        self.change_username_message_scrollArea = QScrollArea(self.profile_change_username_frame)
        self.change_username_message_scrollArea.setObjectName(u"change_username_message_scrollArea")
        self.change_username_message_scrollArea.setWidgetResizable(True)
        self.change_username_message_frame = QWidget()
        self.change_username_message_frame.setObjectName(u"change_username_message_frame")
        self.change_username_message_frame.setGeometry(QRect(0, 0, 447, 360))
        self.change_username_message_scrollArea.setWidget(self.change_username_message_frame)

        self.verticalLayout_54.addWidget(self.change_username_message_scrollArea)


        self.verticalLayout_52.addWidget(self.profile_change_username_frame)


        self.horizontalLayout_20.addLayout(self.verticalLayout_52)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.profile_change_password_title_frame = QFrame(self.user_profile_tab)
        self.profile_change_password_title_frame.setObjectName(u"profile_change_password_title_frame")
        self.profile_change_password_title_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_change_password_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.profile_change_password_title_frame)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.profile_change_password_label = QLabel(self.profile_change_password_title_frame)
        self.profile_change_password_label.setObjectName(u"profile_change_password_label")
        self.profile_change_password_label.setStyleSheet(u"")

        self.verticalLayout_44.addWidget(self.profile_change_password_label)


        self.verticalLayout_50.addWidget(self.profile_change_password_title_frame)

        self.profile_change_password_frame = QFrame(self.user_profile_tab)
        self.profile_change_password_frame.setObjectName(u"profile_change_password_frame")
        self.profile_change_password_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_change_password_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.profile_change_password_frame)
        self.verticalLayout_51.setSpacing(20)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(20, 20, 20, -1)
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(6)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.profile_password_label = QLabel(self.profile_change_password_frame)
        self.profile_password_label.setObjectName(u"profile_password_label")

        self.verticalLayout_43.addWidget(self.profile_password_label)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.userpage_editprofile_old_password_inpt = QLineEdit(self.profile_change_password_frame)
        self.userpage_editprofile_old_password_inpt.setObjectName(u"userpage_editprofile_old_password_inpt")
        self.userpage_editprofile_old_password_inpt.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.userpage_editprofile_old_password_inpt)

        self.userpage_editprofile_old_password_eye = QPushButton(self.profile_change_password_frame)
        self.userpage_editprofile_old_password_eye.setObjectName(u"userpage_editprofile_old_password_eye")
        sizePolicy5.setHeightForWidth(self.userpage_editprofile_old_password_eye.sizePolicy().hasHeightForWidth())
        self.userpage_editprofile_old_password_eye.setSizePolicy(sizePolicy5)
        self.userpage_editprofile_old_password_eye.setCursor(QCursor(Qt.PointingHandCursor))
        self.userpage_editprofile_old_password_eye.setStyleSheet(u"")
        self.userpage_editprofile_old_password_eye.setIcon(icon11)

        self.horizontalLayout_17.addWidget(self.userpage_editprofile_old_password_eye)


        self.verticalLayout_43.addLayout(self.horizontalLayout_17)


        self.verticalLayout_51.addLayout(self.verticalLayout_43)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(6)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(-1, -1, -1, 0)
        self.profile_new_password_label = QLabel(self.profile_change_password_frame)
        self.profile_new_password_label.setObjectName(u"profile_new_password_label")

        self.verticalLayout_47.addWidget(self.profile_new_password_label)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.userpage_editprofile_new_password_inpt = QLineEdit(self.profile_change_password_frame)
        self.userpage_editprofile_new_password_inpt.setObjectName(u"userpage_editprofile_new_password_inpt")

        self.horizontalLayout_18.addWidget(self.userpage_editprofile_new_password_inpt)

        self.userpage_editprofile_new_password_eye = QPushButton(self.profile_change_password_frame)
        self.userpage_editprofile_new_password_eye.setObjectName(u"userpage_editprofile_new_password_eye")
        sizePolicy5.setHeightForWidth(self.userpage_editprofile_new_password_eye.sizePolicy().hasHeightForWidth())
        self.userpage_editprofile_new_password_eye.setSizePolicy(sizePolicy5)
        self.userpage_editprofile_new_password_eye.setCursor(QCursor(Qt.PointingHandCursor))
        self.userpage_editprofile_new_password_eye.setIcon(icon11)

        self.horizontalLayout_18.addWidget(self.userpage_editprofile_new_password_eye)


        self.verticalLayout_47.addLayout(self.horizontalLayout_18)


        self.verticalLayout_51.addLayout(self.verticalLayout_47)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setSpacing(6)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.profile_confirm_password_label = QLabel(self.profile_change_password_frame)
        self.profile_confirm_password_label.setObjectName(u"profile_confirm_password_label")

        self.verticalLayout_49.addWidget(self.profile_confirm_password_label)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.userpage_editprofile_confirm_new_password_inpt = QLineEdit(self.profile_change_password_frame)
        self.userpage_editprofile_confirm_new_password_inpt.setObjectName(u"userpage_editprofile_confirm_new_password_inpt")

        self.horizontalLayout_19.addWidget(self.userpage_editprofile_confirm_new_password_inpt)

        self.userpage_editprofile_confirm_new_password_eye = QPushButton(self.profile_change_password_frame)
        self.userpage_editprofile_confirm_new_password_eye.setObjectName(u"userpage_editprofile_confirm_new_password_eye")
        sizePolicy5.setHeightForWidth(self.userpage_editprofile_confirm_new_password_eye.sizePolicy().hasHeightForWidth())
        self.userpage_editprofile_confirm_new_password_eye.setSizePolicy(sizePolicy5)
        self.userpage_editprofile_confirm_new_password_eye.setCursor(QCursor(Qt.PointingHandCursor))
        self.userpage_editprofile_confirm_new_password_eye.setIcon(icon11)

        self.horizontalLayout_19.addWidget(self.userpage_editprofile_confirm_new_password_eye)


        self.verticalLayout_49.addLayout(self.horizontalLayout_19)


        self.verticalLayout_51.addLayout(self.verticalLayout_49)

        self.userpage_editprofile_change_password_btn = QPushButton(self.profile_change_password_frame)
        self.userpage_editprofile_change_password_btn.setObjectName(u"userpage_editprofile_change_password_btn")
        self.userpage_editprofile_change_password_btn.setMaximumSize(QSize(120, 30))
        self.userpage_editprofile_change_password_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.userpage_editprofile_change_password_btn.setStyleSheet(u"max-width: 120px;")

        self.verticalLayout_51.addWidget(self.userpage_editprofile_change_password_btn, 0, Qt.AlignHCenter)

        self.change_password_message_scrollArea = QScrollArea(self.profile_change_password_frame)
        self.change_password_message_scrollArea.setObjectName(u"change_password_message_scrollArea")
        self.change_password_message_scrollArea.setWidgetResizable(True)
        self.change_password_message_frame = QWidget()
        self.change_password_message_frame.setObjectName(u"change_password_message_frame")
        self.change_password_message_frame.setGeometry(QRect(0, 0, 447, 272))
        self.change_password_message_scrollArea.setWidget(self.change_password_message_frame)

        self.verticalLayout_51.addWidget(self.change_password_message_scrollArea)


        self.verticalLayout_50.addWidget(self.profile_change_password_frame)


        self.horizontalLayout_20.addLayout(self.verticalLayout_50)

        self.user_tabs.addTab(self.user_profile_tab, "")
        self.all_users_tab = QWidget()
        self.all_users_tab.setObjectName(u"all_users_tab")
        self.verticalLayout_45 = QVBoxLayout(self.all_users_tab)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.userspage_user_heading_lbl = QLabel(self.all_users_tab)
        self.userspage_user_heading_lbl.setObjectName(u"userspage_user_heading_lbl")
        self.userspage_user_heading_lbl.setStyleSheet(u"")

        self.verticalLayout_45.addWidget(self.userspage_user_heading_lbl)

        self.userpage_all_users_table = QTableWidget(self.all_users_tab)
        if (self.userpage_all_users_table.rowCount() < 1):
            self.userpage_all_users_table.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.userpage_all_users_table.setVerticalHeaderItem(0, __qtablewidgetitem)
        self.userpage_all_users_table.setObjectName(u"userpage_all_users_table")
        self.userpage_all_users_table.setStyleSheet(u"")
        self.userpage_all_users_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userpage_all_users_table.setShowGrid(True)
        self.userpage_all_users_table.setGridStyle(Qt.SolidLine)
        self.userpage_all_users_table.setSortingEnabled(True)
        self.userpage_all_users_table.setWordWrap(True)
        self.userpage_all_users_table.horizontalHeader().setMinimumSectionSize(57)
        self.userpage_all_users_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.userpage_all_users_table.horizontalHeader().setStretchLastSection(True)
        self.userpage_all_users_table.verticalHeader().setVisible(False)
        self.userpage_all_users_table.verticalHeader().setCascadingSectionResizes(False)

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
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1226, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        self.main_stackedWidget.setCurrentIndex(0)
        self.settings_tabs.setCurrentIndex(0)
        self.algorithm_stackedWidget.setCurrentIndex(0)
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
        self.camera_settings_off_label.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.connect_camera_switch.setText("")
        self.camera_settings_on_label.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.camera_settings_camera_label.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.camera_settings_serial_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.camera_settings_gain_label.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.camera_settings_width_label.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.camera_settings_height_label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.camera_settings_exposure_label.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.camera_settings_offsetx_label.setText(QCoreApplication.translate("MainWindow", u"Offset X", None))
        self.camera_settings_offsety_label.setText(QCoreApplication.translate("MainWindow", u"Offset Y", None))
        self.save_camera_settings.setText(QCoreApplication.translate("MainWindow", u"Save Prameters", None))
        self.label.setText("")
        self.camera_settings_live_label.setText("")
        self.settings_tabs.setTabText(self.settings_tabs.indexOf(self.camera_tab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.step1_btn.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.step2_btn.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.step3_btn.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.step1_label.setText(QCoreApplication.translate("MainWindow", u"Step 1", None))
        self.background_th_label.setText(QCoreApplication.translate("MainWindow", u"Background Threshould", None))
        self.conv_wsize_label.setText(QCoreApplication.translate("MainWindow", u"Convolotion Window Size", None))
        self.algorithm_image1.setText("")
        self.step2_label.setText(QCoreApplication.translate("MainWindow", u"Step 2", None))
        self.algorithm_label.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.thresh_error_label.setText(QCoreApplication.translate("MainWindow", u"Thresh Error", None))
        self.algorithm_image2.setText("")
        self.step3_label.setText(QCoreApplication.translate("MainWindow", u"Step 3", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Min Width", None))
        self.algorithm_image3.setText("")
        self.save_algorithm_settings.setText(QCoreApplication.translate("MainWindow", u"Save Prameters", None))
        self.settings_tabs.setTabText(self.settings_tabs.indexOf(self.algorithm_tab), QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.register_username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.register_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.userpage_password_eye.setText("")
        self.register_confirm_password_label.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.userpage_confirm_password_eye.setText("")
        self.register_user_role_label.setText(QCoreApplication.translate("MainWindow", u"User Role", None))
        self.register_user.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.user_register_tab), QCoreApplication.translate("MainWindow", u"register user", None))
        self.profile_change_username_label.setText(QCoreApplication.translate("MainWindow", u"Change Username", None))
        self.profile_old_username_label.setText(QCoreApplication.translate("MainWindow", u"Old Username", None))
        self.profile_username_label.setText(QCoreApplication.translate("MainWindow", u"New Username", None))
        self.userpage_editprofile_change_username_btn.setText(QCoreApplication.translate("MainWindow", u"Change Username", None))
        self.profile_change_password_label.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.profile_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.userpage_editprofile_old_password_eye.setText("")
        self.profile_new_password_label.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.userpage_editprofile_new_password_eye.setText("")
        self.profile_confirm_password_label.setText(QCoreApplication.translate("MainWindow", u"Confirm New Password", None))
        self.userpage_editprofile_confirm_new_password_eye.setText("")
        self.userpage_editprofile_change_password_btn.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.user_profile_tab), QCoreApplication.translate("MainWindow", u"Edit Profile", None))
        self.userspage_user_heading_lbl.setText(QCoreApplication.translate("MainWindow", u"Only Admin Can Access", None))
        ___qtablewidgetitem = self.userpage_all_users_table.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.user_tabs.setTabText(self.user_tabs.indexOf(self.all_users_tab), QCoreApplication.translate("MainWindow", u"All Users", None))
    # retranslateUi

