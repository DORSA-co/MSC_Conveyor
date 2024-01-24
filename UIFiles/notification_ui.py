# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notification.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import assets_rc

class Ui_Notification(object):
    def setupUi(self, Notification):
        if not Notification.objectName():
            Notification.setObjectName(u"Notification")
        Notification.resize(305, 81)
        self.horizontalLayout_2 = QHBoxLayout(Notification)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.StyleSheet = QWidget(Notification)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"#main_frame\n"
"{\n"
"	border-bottom: 3px solid gray;\n"
"	background-color: #F7F8FA;\n"
"}\n"
"QLabel{\n"
"	color:#202020;\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.StyleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.StyleSheet)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 3)
        self.frame = QFrame(self.main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(10, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.defect_color = QLabel(self.frame)
        self.defect_color.setObjectName(u"defect_color")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defect_color.sizePolicy().hasHeightForWidth())
        self.defect_color.setSizePolicy(sizePolicy)
        self.defect_color.setMinimumSize(QSize(10, 0))
        self.defect_color.setStyleSheet(u"background-color:rgb(197, 63, 59);")

        self.horizontalLayout_5.addWidget(self.defect_color)


        self.horizontalLayout_4.addWidget(self.frame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.select_checkBox = QCheckBox(self.main_frame)
        self.select_checkBox.setObjectName(u"select_checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select_checkBox.sizePolicy().hasHeightForWidth())
        self.select_checkBox.setSizePolicy(sizePolicy1)
        self.select_checkBox.setStyleSheet(u"QCheckBox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"/* Unchecked State */\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #C8C8C8;\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* Checked State */\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid #3A9AD9;\n"
"    background-color: #3A9AD9;\n"
"    image: url(:/icons/checked-icon.png);  /* Path to your check mark icon */\n"
"}\n"
"\n"
"/* Hover State */\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid #3A9AD9;\n"
"}\n"
"\n"
"/* Disabled State */\n"
"QCheckBox::indicator:disabled {\n"
"    border: 2px solid #E5E5E5;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.select_checkBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 3, -1, 3)
        self.side_label = QLabel(self.main_frame)
        self.side_label.setObjectName(u"side_label")

        self.verticalLayout.addWidget(self.side_label)

        self.defect_type_label = QLabel(self.main_frame)
        self.defect_type_label.setObjectName(u"defect_type_label")

        self.verticalLayout.addWidget(self.defect_type_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_label = QLabel(self.main_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setStyleSheet(u"color:#404040;")

        self.horizontalLayout.addWidget(self.date_label)

        self.horizontalSpacer = QSpacerItem(27, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.time_label = QLabel(self.main_frame)
        self.time_label.setObjectName(u"time_label")

        self.horizontalLayout.addWidget(self.time_label)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.icon_label = QLabel(self.main_frame)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMaximumSize(QSize(47, 50))
        self.icon_label.setPixmap(QPixmap(u":/icons/icons/warning_icon.png"))

        self.horizontalLayout_3.addWidget(self.icon_label)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.main_frame)


        self.horizontalLayout_2.addWidget(self.StyleSheet)


        self.retranslateUi(Notification)

        QMetaObject.connectSlotsByName(Notification)
    # setupUi

    def retranslateUi(self, Notification):
        Notification.setWindowTitle(QCoreApplication.translate("Notification", u"Form", None))
        self.defect_color.setText("")
        self.select_checkBox.setText("")
        self.side_label.setText(QCoreApplication.translate("Notification", u"Top Side", None))
        self.defect_type_label.setText(QCoreApplication.translate("Notification", u"Critical", None))
        self.date_label.setText(QCoreApplication.translate("Notification", u"24/01/2024 ", None))
        self.time_label.setText(QCoreApplication.translate("Notification", u"12:47:30 PM", None))
        self.icon_label.setText("")
    # retranslateUi

