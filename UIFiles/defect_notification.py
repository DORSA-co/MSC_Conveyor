# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defect_notification.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_Notification(object):
    def setupUi(self, Notification):
        if not Notification.objectName():
            Notification.setObjectName(u"Notification")
        Notification.resize(587, 170)
        self.horizontalLayout_2 = QHBoxLayout(Notification)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.GlobalStyleSheet = QWidget(Notification)
        self.GlobalStyleSheet.setObjectName(u"GlobalStyleSheet")
        self.GlobalStyleSheet.setStyleSheet(u"/**************************Global Font***************************/\n"
"\n"
"QWidget\n"
"{\n"
"	font: auto \"Roboto\";\n"
"}\n"
"\n"
"/**************************QLabel***************************/\n"
"\n"
"QLabel{\n"
"	color:#505050;\n"
"}\n"
"\n"
"/**************************QCheckBox***************************/\n"
"\n"
"QCheckBox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #E0E4EC;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #7892DF;\n"
"    background-color: #7892DF;\n"
"    image: url(:/icons/icons/tick.png)\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid rgba(194, 197, 204, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    border: 2px solid #E0E4EC;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.GlobalStyleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LocalStyleSheet = QWidget(self.GlobalStyleSheet)
        self.LocalStyleSheet.setObjectName(u"LocalStyleSheet")
        self.LocalStyleSheet.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.LocalStyleSheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PointStyleSheet = QWidget(self.LocalStyleSheet)
        self.PointStyleSheet.setObjectName(u"PointStyleSheet")
        self.PointStyleSheet.setStyleSheet(u"/**************************PmainStyle***************************/\n"
"\n"
"*[styleSheet=\"PmainStyle\"]\n"
"{\n"
"	border:1px solid #E0E4EC;\n"
"	border-radius: 15px;\n"
"	background-color: #F7F8FA;\n"
"}\n"
"\n"
"/**************************PcolorFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PcolorFrameStyle\"]\n"
"{\n"
"	border: None;\n"
"	background-color: red;\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"/**************************PiLabelStyle***************************/\n"
"\n"
"*[styleSheet=\"PiLabelStyle\"]\n"
"{\n"
"	color: #FFFFFF\n"
"}\n"
"\n"
"/**************************PcloseButtonStyle***************************/\n"
"\n"
"*[styleSheet=\"PcloseButtonStyle\"]\n"
"{\n"
"	border:none;\n"
"}\n"
"\n"
"*[styleSheet=\"PcloseButtonStyle\"]:hover\n"
"{\n"
"	background-color:#f0f0f0;\n"
"}\n"
"\n"
"/**************************PtagLabelStyle***************************/\n"
"\n"
"*[styleSheet=\"PtagLabelStyle\"]\n"
"{\n"
"	color:rgb(71, 118, 239);\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.PointStyleSheet)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.PointStyleSheet)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(0, 100))
        self.main_frame.setMaximumSize(QSize(16777215, 100))
        self.main_frame.setStyleSheet(u"PmainStyle")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 0, -1)
        self.select_checkBox = QCheckBox(self.main_frame)
        self.select_checkBox.setObjectName(u"select_checkBox")
        self.select_checkBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_checkBox.sizePolicy().hasHeightForWidth())
        self.select_checkBox.setSizePolicy(sizePolicy)
        self.select_checkBox.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.select_checkBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, -1, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.side_label = QLabel(self.main_frame)
        self.side_label.setObjectName(u"side_label")

        self.horizontalLayout_6.addWidget(self.side_label)

        self.tag_label = QLabel(self.main_frame)
        self.tag_label.setObjectName(u"tag_label")
        self.tag_label.setStyleSheet(u"PtagLabelStyle")

        self.horizontalLayout_6.addWidget(self.tag_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.defect_type_label = QLabel(self.main_frame)
        self.defect_type_label.setObjectName(u"defect_type_label")

        self.horizontalLayout_5.addWidget(self.defect_type_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_label = QLabel(self.main_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.date_label)

        self.horizontalSpacer = QSpacerItem(27, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.time_label = QLabel(self.main_frame)
        self.time_label.setObjectName(u"time_label")

        self.horizontalLayout.addWidget(self.time_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.defect_color_frame = QFrame(self.main_frame)
        self.defect_color_frame.setObjectName(u"defect_color_frame")
        self.defect_color_frame.setMinimumSize(QSize(30, 30))
        self.defect_color_frame.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.defect_color_frame.setFont(font)
        self.defect_color_frame.setStyleSheet(u"PcolorFrameStyle")
        self.defect_color_frame.setFrameShape(QFrame.StyledPanel)
        self.defect_color_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.defect_color_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.i_label = QLabel(self.defect_color_frame)
        self.i_label.setObjectName(u"i_label")
        self.i_label.setEnabled(True)
        self.i_label.setMinimumSize(QSize(0, 0))
        self.i_label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.i_label.setFont(font1)
        self.i_label.setStyleSheet(u"PiLabelStyle")
        self.i_label.setScaledContents(True)
        self.i_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.i_label, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.defect_color_frame)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 5, -1)
        self.close_btn = QPushButton(self.main_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(30, 30))
        self.close_btn.setStyleSheet(u"PcloseButtonStyle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(15, 15))

        self.verticalLayout_5.addWidget(self.close_btn, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addWidget(self.main_frame)


        self.verticalLayout.addWidget(self.PointStyleSheet)


        self.verticalLayout_2.addWidget(self.LocalStyleSheet)


        self.horizontalLayout_2.addWidget(self.GlobalStyleSheet)


        self.retranslateUi(Notification)

        QMetaObject.connectSlotsByName(Notification)
    # setupUi

    def retranslateUi(self, Notification):
        Notification.setWindowTitle(QCoreApplication.translate("Notification", u"Form", None))
        self.select_checkBox.setText("")
        self.side_label.setText(QCoreApplication.translate("Notification", u"Top Side", None))
        self.tag_label.setText(QCoreApplication.translate("Notification", u"(Tag)", None))
        self.defect_type_label.setText(QCoreApplication.translate("Notification", u"Critical", None))
        self.date_label.setText(QCoreApplication.translate("Notification", u"24/01/2024 ", None))
        self.time_label.setText(QCoreApplication.translate("Notification", u"12:47:30 PM", None))
        self.i_label.setText(QCoreApplication.translate("Notification", u"i", None))
        self.close_btn.setText("")
    # retranslateUi

