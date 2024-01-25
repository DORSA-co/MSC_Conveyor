# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defect_notification.ui'
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
        Notification.resize(324, 100)
        self.horizontalLayout_2 = QHBoxLayout(Notification)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.StyleSheet = QWidget(Notification)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"QLabel{\n"
"	color:#505050;\n"
"\n"
"}\n"
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
"    border: 2px solid rgba(194, 197, 204, 255);\n"
"}\n"
"\n"
"/* Disabled State */\n"
"QCheckBox::indicator:disabled {\n"
"    border: 2px solid #E0E4EC;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"\n"
"#main_frame\n"
"{\n"
"	border:1px solid #E0E4EC;\n"
"	border-radius: 15px;\n"
"	background-color: #F7F8FA;\n"
"}\n"
"\n"
"#defect_color_frame{\n"
"	border: None;\n"
"}\n"
"\n"
"#defect_color_frame .QLabel\n"
"{\n"
"	borde"
                        "r-radius:4px;\n"
"}\n"
"\n"
"#i_label{\n"
"	color: #FFFFFF\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.StyleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.StyleSheet)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(0, 100))
        self.main_frame.setMaximumSize(QSize(16777215, 100))
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 15, 3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 0, -1)
        self.select_checkBox = QCheckBox(self.main_frame)
        self.select_checkBox.setObjectName(u"select_checkBox")
        self.select_checkBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_checkBox.sizePolicy().hasHeightForWidth())
        self.select_checkBox.setSizePolicy(sizePolicy)
        self.select_checkBox.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.select_checkBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, -1, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.side_label = QLabel(self.main_frame)
        self.side_label.setObjectName(u"side_label")

        self.horizontalLayout_6.addWidget(self.side_label)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.defect_type_label = QLabel(self.main_frame)
        self.defect_type_label.setObjectName(u"defect_type_label")

        self.horizontalLayout_5.addWidget(self.defect_type_label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_label = QLabel(self.main_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.date_label)

        self.horizontalSpacer = QSpacerItem(27, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.time_label = QLabel(self.main_frame)
        self.time_label.setObjectName(u"time_label")

        self.horizontalLayout.addWidget(self.time_label)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.defect_color_frame = QFrame(self.main_frame)
        self.defect_color_frame.setObjectName(u"defect_color_frame")
        self.defect_color_frame.setMinimumSize(QSize(30, 30))
        self.defect_color_frame.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(16)
        self.defect_color_frame.setFont(font)
        self.defect_color_frame.setStyleSheet(u"#defect_color_frame{\n"
"	background-color: red;\n"
"	border-radius:15px;\n"
"	border: None;\n"
"}\n"
"")
        self.defect_color_frame.setFrameShape(QFrame.StyledPanel)
        self.defect_color_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.defect_color_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.i_label = QLabel(self.defect_color_frame)
        self.i_label.setObjectName(u"i_label")
        self.i_label.setEnabled(True)
        self.i_label.setMinimumSize(QSize(0, 0))
        self.i_label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"TeX Gyre Schola"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.i_label.setFont(font1)
        self.i_label.setScaledContents(True)
        self.i_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.i_label, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.defect_color_frame)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.main_frame)


        self.horizontalLayout_2.addWidget(self.StyleSheet)


        self.retranslateUi(Notification)

        QMetaObject.connectSlotsByName(Notification)
    # setupUi

    def retranslateUi(self, Notification):
        Notification.setWindowTitle(QCoreApplication.translate("Notification", u"Form", None))
        self.select_checkBox.setText("")
        self.side_label.setText(QCoreApplication.translate("Notification", u"Top Side", None))
        self.defect_type_label.setText(QCoreApplication.translate("Notification", u"Critical", None))
        self.date_label.setText(QCoreApplication.translate("Notification", u"24/01/2024 ", None))
        self.time_label.setText(QCoreApplication.translate("Notification", u"12:47:30 PM", None))
        self.i_label.setText(QCoreApplication.translate("Notification", u"i", None))
    # retranslateUi

