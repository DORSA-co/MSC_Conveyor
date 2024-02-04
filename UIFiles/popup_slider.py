# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_slider.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import assets_rc

class Ui_slider(object):
    def setupUi(self, slider):
        if not slider.objectName():
            slider.setObjectName(u"slider")
        slider.resize(544, 812)
        self.verticalLayout = QVBoxLayout(slider)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(slider)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(400, 0))
        self.main_frame.setMaximumSize(QSize(800, 16777215))
        self.main_frame.setStyleSheet(u"QSpinBox, QDoubleSpinBox , QDateEdit\n"
"{\n"
"	background-color: transparent;\n"
"	border-bottom: 2px solid #D7D7D9;\n"
"	border-radius: None;\n"
"	font-size: 18px;\n"
"	min-height: 25px;\n"
"	min-width: 70px;\n"
"	qproperty-alignment: AlignCenter;\n"
"	color: #808080;\n"
"}\n"
"\n"
"QSpinBox:disabled ,\n"
"QDoubleSpinBox:disabled ,\n"
"QDateEdit:disabled\n"
"{\n"
"	border-bottom: 2px solid #DCDCDC;\n"
"	color: #DCDCDC;\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow,\n"
"QDateEdit::up-arrow\n"
"{   \n"
"	image: url(:/icons/icons/plus_icon_black.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow ,  QDoubleSpinBox::down-arrow,\n"
"QDateEdit::down-arrow\n"
"{   \n"
"	image: url(:/icons/icons/minus_icon_black.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, QDoubleSpinBox::up-arrow:disabled,\n"
"QDateEdit::up-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/plus_icon_gray.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"Q"
                        "SpinBox::down-arrow:disabled ,  QDoubleSpinBox::down-arrow:disabled,\n"
"QDateEdit::down-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/minus_icon_gray.png);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDateEdit::up-button\n"
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
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button,\n"
"QDateEdit::down-button\n"
"{\n"
"	border:none;\n"
"    min-width:30px;\n"
"    min-height: 29px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left;\n"
"    top: 0px;\n"
"    right: 0px;\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button,\n"
"QDoubleSpinBox::down-button,\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-button\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QSpinBox::up-button:disabled ,\n"
""
                        "QSpinBox::down-button:disabled ,\n"
"QDoubleSpinBox::up-button:disabled ,\n"
"QDoubleSpinBox::down-button:disabled,\n"
"QDateEdit::up-button:disabled,\n"
"QDateEdit::down-button:disabled\n"
"{\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus,\n"
"QDateEdit:focus\n"
"{\n"
"	border-bottom: 2px solid #7892DF;\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
"QCheckBox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Unchecked State */\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #E0E4EC;\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* Checked State */\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #7892DF;\n"
"    background-color: #7892DF;\n"
"    image: url(:/icons/icons/tick.png)  /* Path to your check mark icon */\n"
"}\n"
"\n"
"/* Hover State */\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid rgba(194, 197, 204, 255)"
                        ";\n"
"}\n"
"\n"
"/* Disabled State */\n"
"QCheckBox::indicator:disabled {\n"
"    border: 2px solid #E0E4EC;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"\n"
"/************************************************************/\n"
"\n"
"#frame{\n"
"	background-color: #F7F8FA;\n"
"}\n"
"\n"
"#system_status_page .QFrame{\n"
"	border:1px solid #E0E4EC;\n"
"	border-radius: 20px;\n"
"	min-height: 100px;\n"
"	max-height: 100px;\n"
"	padding-right: 30px;\n"
"}\n"
"\n"
"#camera_status_title, \n"
"#plc_status_title,\n"
"#laser_status_title,\n"
"#database_status_title{\n"
"	color: #808080;\n"
"}\n"
"\n"
"#filters_frame{\n"
"	border: None;\n"
"}\n"
"\n"
"#filters_frame .QLabel{\n"
"	color: #808080;\n"
"}\n"
"\n"
"#filters_frame .QFrame{\n"
"	border:1px solid #E0E4EC;\n"
"	border-radius: 20px;\n"
"	min-height: 120px;\n"
"	max-height: 120px;\n"
"}\n"
"\n"
"#date_icon,\n"
"#width_icon,\n"
"#height_icon,\n"
"#depth_icon\n"
"{\n"
"	border: 0px solid transparent;	\n"
"}\n"
"\n"
"#filters_apply_btn\n"
"{\n"
"	background-color: q"
                        "lineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));\n"
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
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.close = QPushButton(self.main_frame)
        self.close.setObjectName(u"close")
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet(u"border:none;\n"
"background-color:transparent;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon)

        self.horizontalLayout.addWidget(self.close)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.system_status_page = QWidget()
        self.system_status_page.setObjectName(u"system_status_page")
        self.verticalLayout_3 = QVBoxLayout(self.system_status_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.camera_staus_frame = QFrame(self.system_status_page)
        self.camera_staus_frame.setObjectName(u"camera_staus_frame")
        self.camera_staus_frame.setFrameShape(QFrame.StyledPanel)
        self.camera_staus_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.camera_staus_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.camera_status_icon = QLabel(self.camera_staus_frame)
        self.camera_status_icon.setObjectName(u"camera_status_icon")
        self.camera_status_icon.setMinimumSize(QSize(50, 0))
        self.camera_status_icon.setPixmap(QPixmap(u":/icons/icons/camera.png"))
        self.camera_status_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.camera_status_icon)

        self.camera_status_title = QLabel(self.camera_staus_frame)
        self.camera_status_title.setObjectName(u"camera_status_title")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.camera_status_title.setFont(font)
        self.camera_status_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.camera_status_title)

        self.camera_status = QLabel(self.camera_staus_frame)
        self.camera_status.setObjectName(u"camera_status")
        self.camera_status.setPixmap(QPixmap(u":/icons/icons/error_icon.png"))
        self.camera_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.camera_status)


        self.verticalLayout_3.addWidget(self.camera_staus_frame)

        self.plc_staus_frame = QFrame(self.system_status_page)
        self.plc_staus_frame.setObjectName(u"plc_staus_frame")
        self.plc_staus_frame.setFrameShape(QFrame.StyledPanel)
        self.plc_staus_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.plc_staus_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.plc_staus_icon = QLabel(self.plc_staus_frame)
        self.plc_staus_icon.setObjectName(u"plc_staus_icon")
        self.plc_staus_icon.setPixmap(QPixmap(u":/icons/icons/plc.png"))
        self.plc_staus_icon.setScaledContents(False)
        self.plc_staus_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.plc_staus_icon)

        self.plc_status_title = QLabel(self.plc_staus_frame)
        self.plc_status_title.setObjectName(u"plc_status_title")
        self.plc_status_title.setFont(font)
        self.plc_status_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.plc_status_title)

        self.plc_staus = QLabel(self.plc_staus_frame)
        self.plc_staus.setObjectName(u"plc_staus")
        self.plc_staus.setPixmap(QPixmap(u":/icons/icons/success_icon.png"))
        self.plc_staus.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.plc_staus)


        self.verticalLayout_3.addWidget(self.plc_staus_frame)

        self.laser_status_frame = QFrame(self.system_status_page)
        self.laser_status_frame.setObjectName(u"laser_status_frame")
        self.laser_status_frame.setFrameShape(QFrame.StyledPanel)
        self.laser_status_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.laser_status_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.laser_status_icon = QLabel(self.laser_status_frame)
        self.laser_status_icon.setObjectName(u"laser_status_icon")
        self.laser_status_icon.setPixmap(QPixmap(u":/icons/icons/laser.png"))
        self.laser_status_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.laser_status_icon)

        self.laser_status_title = QLabel(self.laser_status_frame)
        self.laser_status_title.setObjectName(u"laser_status_title")
        self.laser_status_title.setFont(font)
        self.laser_status_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.laser_status_title)

        self.laser_status = QLabel(self.laser_status_frame)
        self.laser_status.setObjectName(u"laser_status")
        self.laser_status.setPixmap(QPixmap(u":/icons/icons/error_icon.png"))
        self.laser_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.laser_status)


        self.verticalLayout_3.addWidget(self.laser_status_frame)

        self.database_staus_frame = QFrame(self.system_status_page)
        self.database_staus_frame.setObjectName(u"database_staus_frame")
        self.database_staus_frame.setFrameShape(QFrame.StyledPanel)
        self.database_staus_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.database_staus_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.database_staus_icon = QLabel(self.database_staus_frame)
        self.database_staus_icon.setObjectName(u"database_staus_icon")
        self.database_staus_icon.setPixmap(QPixmap(u":/icons/icons/database.png"))
        self.database_staus_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.database_staus_icon)

        self.database_status_title = QLabel(self.database_staus_frame)
        self.database_status_title.setObjectName(u"database_status_title")
        self.database_status_title.setFont(font)
        self.database_status_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.database_status_title)

        self.database_staus = QLabel(self.database_staus_frame)
        self.database_staus.setObjectName(u"database_staus")
        self.database_staus.setPixmap(QPixmap(u":/icons/icons/success_icon.png"))
        self.database_staus.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.database_staus)


        self.verticalLayout_3.addWidget(self.database_staus_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pages.addWidget(self.system_status_page)
        self.notification_filter_page = QWidget()
        self.notification_filter_page.setObjectName(u"notification_filter_page")
        self.verticalLayout_4 = QVBoxLayout(self.notification_filter_page)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.filter_by_label = QLabel(self.notification_filter_page)
        self.filter_by_label.setObjectName(u"filter_by_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_by_label.sizePolicy().hasHeightForWidth())
        self.filter_by_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.filter_by_label.setFont(font1)

        self.verticalLayout_4.addWidget(self.filter_by_label)

        self.filters_frame = QFrame(self.notification_filter_page)
        self.filters_frame.setObjectName(u"filters_frame")
        self.filters_frame.setFrameShape(QFrame.StyledPanel)
        self.filters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.filters_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.date_frame = QFrame(self.filters_frame)
        self.date_frame.setObjectName(u"date_frame")
        self.date_frame.setEnabled(True)
        self.date_frame.setStyleSheet(u"")
        self.date_frame.setFrameShape(QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.date_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.filter_date_checkBox = QCheckBox(self.date_frame)
        self.filter_date_checkBox.setObjectName(u"filter_date_checkBox")
        self.filter_date_checkBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filter_date_checkBox.sizePolicy().hasHeightForWidth())
        self.filter_date_checkBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.filter_date_checkBox)

        self.date_icon = QPushButton(self.date_frame)
        self.date_icon.setObjectName(u"date_icon")
        self.date_icon.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.date_icon.sizePolicy().hasHeightForWidth())
        self.date_icon.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/date_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icons/date_gray.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.date_icon.setIcon(icon1)
        self.date_icon.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.date_icon)

        self.date_label = QLabel(self.date_frame)
        self.date_label.setObjectName(u"date_label")
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setFont(font)

        self.horizontalLayout_9.addWidget(self.date_label)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(12, -1, 12, -1)
        self.start_date_input = QDateEdit(self.date_frame)
        self.start_date_input.setObjectName(u"start_date_input")
        self.start_date_input.setEnabled(True)
        self.start_date_input.setTimeSpec(Qt.OffsetFromUTC)

        self.horizontalLayout_10.addWidget(self.start_date_input)

        self.date_to_label = QLabel(self.date_frame)
        self.date_to_label.setObjectName(u"date_to_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.date_to_label.sizePolicy().hasHeightForWidth())
        self.date_to_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.date_to_label)

        self.end_date_input = QDateEdit(self.date_frame)
        self.end_date_input.setObjectName(u"end_date_input")
        self.end_date_input.setEnabled(True)

        self.horizontalLayout_10.addWidget(self.end_date_input)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)


        self.verticalLayout_9.addWidget(self.date_frame)

        self.width_frame = QFrame(self.filters_frame)
        self.width_frame.setObjectName(u"width_frame")
        self.width_frame.setFrameShape(QFrame.StyledPanel)
        self.width_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.width_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.filter_width_checkBox = QCheckBox(self.width_frame)
        self.filter_width_checkBox.setObjectName(u"filter_width_checkBox")
        sizePolicy1.setHeightForWidth(self.filter_width_checkBox.sizePolicy().hasHeightForWidth())
        self.filter_width_checkBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.filter_width_checkBox)

        self.width_icon = QPushButton(self.width_frame)
        self.width_icon.setObjectName(u"width_icon")
        self.width_icon.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.width_icon.sizePolicy().hasHeightForWidth())
        self.width_icon.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/width_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons/width_gray.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.width_icon.setIcon(icon2)
        self.width_icon.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.width_icon)

        self.width_label = QLabel(self.width_frame)
        self.width_label.setObjectName(u"width_label")
        sizePolicy.setHeightForWidth(self.width_label.sizePolicy().hasHeightForWidth())
        self.width_label.setSizePolicy(sizePolicy)
        self.width_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.width_label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(12, -1, 12, -1)
        self.low_width_input = QDoubleSpinBox(self.width_frame)
        self.low_width_input.setObjectName(u"low_width_input")
        self.low_width_input.setEnabled(True)
        self.low_width_input.setAlignment(Qt.AlignCenter)
        self.low_width_input.setMaximum(140.000000000000000)

        self.horizontalLayout_11.addWidget(self.low_width_input)

        self.width_to_label = QLabel(self.width_frame)
        self.width_to_label.setObjectName(u"width_to_label")
        sizePolicy2.setHeightForWidth(self.width_to_label.sizePolicy().hasHeightForWidth())
        self.width_to_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.width_to_label)

        self.high_width_input = QDoubleSpinBox(self.width_frame)
        self.high_width_input.setObjectName(u"high_width_input")
        self.high_width_input.setAlignment(Qt.AlignCenter)
        self.high_width_input.setMaximum(140.000000000000000)
        self.high_width_input.setValue(140.000000000000000)

        self.horizontalLayout_11.addWidget(self.high_width_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.verticalLayout_9.addWidget(self.width_frame)

        self.height_frame = QFrame(self.filters_frame)
        self.height_frame.setObjectName(u"height_frame")
        self.height_frame.setFrameShape(QFrame.StyledPanel)
        self.height_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.height_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.filter_lenght_checkBox = QCheckBox(self.height_frame)
        self.filter_lenght_checkBox.setObjectName(u"filter_lenght_checkBox")
        sizePolicy1.setHeightForWidth(self.filter_lenght_checkBox.sizePolicy().hasHeightForWidth())
        self.filter_lenght_checkBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.filter_lenght_checkBox)

        self.height_icon = QPushButton(self.height_frame)
        self.height_icon.setObjectName(u"height_icon")
        self.height_icon.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.height_icon.sizePolicy().hasHeightForWidth())
        self.height_icon.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/length_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/length_gray.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.height_icon.setIcon(icon3)
        self.height_icon.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.height_icon)

        self.height_label = QLabel(self.height_frame)
        self.height_label.setObjectName(u"height_label")
        sizePolicy.setHeightForWidth(self.height_label.sizePolicy().hasHeightForWidth())
        self.height_label.setSizePolicy(sizePolicy)
        self.height_label.setFont(font)

        self.horizontalLayout_7.addWidget(self.height_label)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(12, -1, 12, -1)
        self.low_lenght_input = QDoubleSpinBox(self.height_frame)
        self.low_lenght_input.setObjectName(u"low_lenght_input")
        self.low_lenght_input.setAlignment(Qt.AlignCenter)
        self.low_lenght_input.setMaximum(200.000000000000000)

        self.horizontalLayout_12.addWidget(self.low_lenght_input)

        self.lenght_to_label = QLabel(self.height_frame)
        self.lenght_to_label.setObjectName(u"lenght_to_label")
        sizePolicy2.setHeightForWidth(self.lenght_to_label.sizePolicy().hasHeightForWidth())
        self.lenght_to_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.lenght_to_label)

        self.high_lenght_input = QDoubleSpinBox(self.height_frame)
        self.high_lenght_input.setObjectName(u"high_lenght_input")
        self.high_lenght_input.setAlignment(Qt.AlignCenter)
        self.high_lenght_input.setMaximum(200.000000000000000)
        self.high_lenght_input.setValue(100.000000000000000)

        self.horizontalLayout_12.addWidget(self.high_lenght_input)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_9.addWidget(self.height_frame)

        self.depth_frame = QFrame(self.filters_frame)
        self.depth_frame.setObjectName(u"depth_frame")
        self.depth_frame.setFrameShape(QFrame.StyledPanel)
        self.depth_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.depth_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.filter_depth_checkBox = QCheckBox(self.depth_frame)
        self.filter_depth_checkBox.setObjectName(u"filter_depth_checkBox")
        sizePolicy1.setHeightForWidth(self.filter_depth_checkBox.sizePolicy().hasHeightForWidth())
        self.filter_depth_checkBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.filter_depth_checkBox)

        self.depth_icon = QPushButton(self.depth_frame)
        self.depth_icon.setObjectName(u"depth_icon")
        self.depth_icon.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.depth_icon.sizePolicy().hasHeightForWidth())
        self.depth_icon.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/depth_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icons/depth_gray.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.depth_icon.setIcon(icon4)
        self.depth_icon.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.depth_icon)

        self.depth_label = QLabel(self.depth_frame)
        self.depth_label.setObjectName(u"depth_label")
        sizePolicy.setHeightForWidth(self.depth_label.sizePolicy().hasHeightForWidth())
        self.depth_label.setSizePolicy(sizePolicy)
        self.depth_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.depth_label)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(12, -1, 12, -1)
        self.low_depth_input = QDoubleSpinBox(self.depth_frame)
        self.low_depth_input.setObjectName(u"low_depth_input")
        self.low_depth_input.setAlignment(Qt.AlignCenter)
        self.low_depth_input.setMinimum(-30.000000000000000)
        self.low_depth_input.setMaximum(30.000000000000000)
        self.low_depth_input.setValue(-30.000000000000000)

        self.horizontalLayout_13.addWidget(self.low_depth_input)

        self.depth_to_label = QLabel(self.depth_frame)
        self.depth_to_label.setObjectName(u"depth_to_label")
        sizePolicy2.setHeightForWidth(self.depth_to_label.sizePolicy().hasHeightForWidth())
        self.depth_to_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.depth_to_label)

        self.high_depth_input = QDoubleSpinBox(self.depth_frame)
        self.high_depth_input.setObjectName(u"high_depth_input")
        self.high_depth_input.setAlignment(Qt.AlignCenter)
        self.high_depth_input.setMinimum(-30.000000000000000)
        self.high_depth_input.setMaximum(30.000000000000000)
        self.high_depth_input.setValue(30.000000000000000)

        self.horizontalLayout_13.addWidget(self.high_depth_input)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9.addWidget(self.depth_frame)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(26, 10, 13, 10)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)

        self.filters_apply_btn = QPushButton(self.filters_frame)
        self.filters_apply_btn.setObjectName(u"filters_apply_btn")
        self.filters_apply_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.filters_apply_btn.setStyleSheet(u"#filters_apply_btn\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 20px;\n"
"	min-width: 134;\n"
"	max-width: 134;\n"
"	min-height:40;\n"
"	max-height: 40;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#filters_apply_btn:disabled\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(189, 189, 191, 255), stop:1 rgba(189, 189, 191, 255));\n"
"	color: rgba(120, 120, 120, 255);\n"
"}\n"
"\n"
"#filters_apply_btn:hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));\n"
"}\n"
"\n"
"#filters_apply_btn:pressed\n"
"{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"")

        self.horizontalLayout_25.addWidget(self.filters_apply_btn)

        self.notif_clear_filter_btn = QPushButton(self.filters_frame)
        self.notif_clear_filter_btn.setObjectName(u"notif_clear_filter_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.notif_clear_filter_btn.sizePolicy().hasHeightForWidth())
        self.notif_clear_filter_btn.setSizePolicy(sizePolicy3)
        self.notif_clear_filter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.notif_clear_filter_btn.setStyleSheet(u"#notif_clear_filter_btn\n"
"{\n"
"	border: 2px solid  rgba(46, 76, 153, 255);\n"
"	color:  rgba(46, 76, 153, 255);\n"
"	border-radius: 18px;\n"
"	min-width: 130;\n"
"	max-width: 130;\n"
"	min-height: 36;\n"
"	max-height: 36;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	qproperty-icon: url(:/icons/icons/clear_filter_blue.png);\n"
"}\n"
"\n"
"#notif_clear_filter_btn:disabled\n"
"{\n"
"	border: 2px solid rgba(189, 189, 191, 255);\n"
"	color: rgba(120, 120, 120, 255);\n"
"}\n"
"\n"
"#notif_clear_filter_btn:hover\n"
"{\n"
"	border: 2px solid rgba(76, 126, 255, 255);\n"
"	color:  rgba(76, 126, 255, 255);\n"
"	qproperty-icon: url(:/icons/icons/clear_filter_blue_hover.png);\n"
"}\n"
"\n"
"#notif_clear_filter_btn:pressed\n"
"{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/clear_filter_blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notif_clear_filter_btn.setIcon(icon5)
        self.notif_clear_filter_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_25.addWidget(self.notif_clear_filter_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.verticalLayout_4.addWidget(self.filters_frame)

        self.pages.addWidget(self.notification_filter_page)

        self.verticalLayout_2.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)


        self.retranslateUi(slider)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(slider)
    # setupUi

    def retranslateUi(self, slider):
        slider.setWindowTitle(QCoreApplication.translate("slider", u"Form", None))
        self.close.setText("")
        self.camera_status_icon.setText("")
        self.camera_status_title.setText(QCoreApplication.translate("slider", u"Camera Connection", None))
        self.camera_status.setText("")
        self.plc_staus_icon.setText("")
        self.plc_status_title.setText(QCoreApplication.translate("slider", u"PLC Connection", None))
        self.plc_staus.setText("")
        self.laser_status_icon.setText("")
        self.laser_status_title.setText(QCoreApplication.translate("slider", u"Laser", None))
        self.laser_status.setText("")
        self.database_staus_icon.setText("")
        self.database_status_title.setText(QCoreApplication.translate("slider", u"Database Connection", None))
        self.database_staus.setText("")
        self.filter_by_label.setText(QCoreApplication.translate("slider", u"Filter By", None))
        self.filter_date_checkBox.setText("")
        self.date_icon.setText("")
        self.date_label.setText(QCoreApplication.translate("slider", u"Date", None))
        self.date_to_label.setText(QCoreApplication.translate("slider", u"To", None))
        self.filter_width_checkBox.setText("")
        self.width_icon.setText("")
        self.width_label.setText(QCoreApplication.translate("slider", u"Width (cm)", None))
        self.width_to_label.setText(QCoreApplication.translate("slider", u"To", None))
        self.filter_lenght_checkBox.setText("")
        self.height_icon.setText("")
        self.height_label.setText(QCoreApplication.translate("slider", u"Lenght (m)", None))
        self.lenght_to_label.setText(QCoreApplication.translate("slider", u"To", None))
        self.filter_depth_checkBox.setText("")
        self.depth_icon.setText("")
        self.depth_label.setText(QCoreApplication.translate("slider", u"Depth (mm)", None))
        self.depth_to_label.setText(QCoreApplication.translate("slider", u"To", None))
        self.filters_apply_btn.setText(QCoreApplication.translate("slider", u"Apply", None))
        self.notif_clear_filter_btn.setText(QCoreApplication.translate("slider", u"Clear Filters", None))
    # retranslateUi

