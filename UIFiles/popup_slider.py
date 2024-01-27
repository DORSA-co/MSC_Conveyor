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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import assets_rc

class Ui_slider(object):
    def setupUi(self, slider):
        if not slider.objectName():
            slider.setObjectName(u"slider")
        slider.resize(544, 812)
        self.verticalLayout = QVBoxLayout(slider)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(slider)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 0))
        self.frame.setMaximumSize(QSize(800, 16777215))
        self.frame.setStyleSheet(u"QSpinBox, QDoubleSpinBox , QDateEdit\n"
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
"	border-bottom: 2px solid #F0F0F2;\n"
"	color: rgb(120, 120, 120);\n"
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
"}"
                        "\n"
"\n"
"QSpinBox::down-arrow:disabled ,  QDoubleSpinBox::down-arrow:disabled,\n"
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
"QSpinBox::up-button:"
                        "disabled ,\n"
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
"	min-height: 120p"
                        "x;\n"
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
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.close = QPushButton(self.frame)
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

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
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

        self.stackedWidget.addWidget(self.system_status_page)
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
        self.date_frame.setFrameShape(QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.date_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.date_icon = QPushButton(self.date_frame)
        self.date_icon.setObjectName(u"date_icon")
        self.date_icon.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.date_icon.sizePolicy().hasHeightForWidth())
        self.date_icon.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/date.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.dateEdit = QDateEdit(self.date_frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setEnabled(True)

        self.horizontalLayout_10.addWidget(self.dateEdit)

        self.label_2 = QLabel(self.date_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.dateEdit_2 = QDateEdit(self.date_frame)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setEnabled(True)

        self.horizontalLayout_10.addWidget(self.dateEdit_2)


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
        self.width_icon = QPushButton(self.width_frame)
        self.width_icon.setObjectName(u"width_icon")
        self.width_icon.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.width_icon.sizePolicy().hasHeightForWidth())
        self.width_icon.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/width.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.doubleSpinBox = QDoubleSpinBox(self.width_frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.doubleSpinBox)

        self.label_3 = QLabel(self.width_frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_3)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.width_frame)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_2)


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
        self.height_icon = QPushButton(self.height_frame)
        self.height_icon.setObjectName(u"height_icon")
        self.height_icon.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.height_icon.sizePolicy().hasHeightForWidth())
        self.height_icon.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/height.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.doubleSpinBox_3 = QDoubleSpinBox(self.height_frame)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_3)

        self.label_4 = QLabel(self.height_frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.label_4)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.height_frame)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_4)


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
        self.depth_icon = QPushButton(self.depth_frame)
        self.depth_icon.setObjectName(u"depth_icon")
        self.depth_icon.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.depth_icon.sizePolicy().hasHeightForWidth())
        self.depth_icon.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/depth.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.doubleSpinBox_5 = QDoubleSpinBox(self.depth_frame)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_5)

        self.label_5 = QLabel(self.depth_frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.label_5)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.depth_frame)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9.addWidget(self.depth_frame)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.filters_apply_btn = QPushButton(self.filters_frame)
        self.filters_apply_btn.setObjectName(u"filters_apply_btn")

        self.verticalLayout_9.addWidget(self.filters_apply_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.verticalLayout_4.addWidget(self.filters_frame)

        self.stackedWidget.addWidget(self.notification_filter_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(slider)

        self.stackedWidget.setCurrentIndex(1)


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
        self.date_icon.setText("")
        self.date_label.setText(QCoreApplication.translate("slider", u"Date", None))
        self.label_2.setText(QCoreApplication.translate("slider", u"To", None))
        self.width_icon.setText("")
        self.width_label.setText(QCoreApplication.translate("slider", u"Width", None))
        self.label_3.setText(QCoreApplication.translate("slider", u"To", None))
        self.height_icon.setText("")
        self.height_label.setText(QCoreApplication.translate("slider", u"Height", None))
        self.label_4.setText(QCoreApplication.translate("slider", u"To", None))
        self.depth_icon.setText("")
        self.depth_label.setText(QCoreApplication.translate("slider", u"Depth", None))
        self.label_5.setText(QCoreApplication.translate("slider", u"To", None))
        self.filters_apply_btn.setText(QCoreApplication.translate("slider", u"Apply", None))
    # retranslateUi

