# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'verify_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import assets_rc
import assets_rc

class Ui_verifyDialogWin(object):
    def setupUi(self, verifyDialogWin):
        if not verifyDialogWin.objectName():
            verifyDialogWin.setObjectName(u"verifyDialogWin")
        verifyDialogWin.resize(309, 286)
        self.verticalLayout = QVBoxLayout(verifyDialogWin)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalStyleSheet = QWidget(verifyDialogWin)
        self.GlobalStyleSheet.setObjectName(u"GlobalStyleSheet")
        self.GlobalStyleSheet.setStyleSheet(u"/**************************Global Font***************************/\n"
"\n"
"QWidget\n"
"{\n"
"	font: auto \"Roboto\";\n"
"}\n"
"\n"
"/**************************QLineEdit***************************/\n"
"\n"
"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: None;\n"
"	border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"	color: rgba(255, 255, 255, 230);\n"
"	padding-bottom: 7px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 3px solid #7E84A2;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.GlobalStyleSheet)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.LocalStyleSheet = QWidget(self.GlobalStyleSheet)
        self.LocalStyleSheet.setObjectName(u"LocalStyleSheet")
        self.verticalLayout_2 = QVBoxLayout(self.LocalStyleSheet)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PointStyleSheet = QWidget(self.LocalStyleSheet)
        self.PointStyleSheet.setObjectName(u"PointStyleSheet")
        self.PointStyleSheet.setStyleSheet(u"/**************************PmainFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PmainFrameStyle\"]\n"
"{\n"
"	background-color: rgba(23, 32, 58, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/**************************PinnerFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PinnerFrameStyle\"]\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, 			y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 120), stop:0.835227 rgba(0, 0, 0, 150));	\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/**************************PtopFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PtopFrameStyle\"]\n"
"{\n"
"	border: None;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/**************************PverifyFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PverifyFrameStyle\"]\n"
"{\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"/**************************PcloseButtonStyle***************************/\n"
"\n"
""
                        "*[styleSheet=\"PcloseButtonStyle\"]\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"/**************************PtempButtonStyle***************************/\n"
"\n"
"*[styleSheet=\"PtempButtonStyle\"]\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"*[styleSheet=\"PtempButtonStyle\"]:pressed{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"/**************************PeyeButtonStyle***************************/\n"
"\n"
"*[styleSheet=\"PeyeButtonStyle\"]\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"*[styleSheet=\"PeyeButtonStyle\"]:pressed{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"/**************************PverifyButtonStyle***************************/\n"
"\n"
"*[styleSheet=\"PverifyButtonStyle\"]\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(126, 132, 162), stop:1 rgb(31, 42, 77));\n"
"	color: rgba(255, 255, 255, 210"
                        ");\n"
"	border-radius: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"*[styleSheet=\"PverifyButtonStyle\"]:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(139, 146, 179), stop:1 rgba(40, 67, 98, 219));\n"
"}\n"
"\n"
"*[styleSheet=\"PverifyButtonStyle\"]:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"/**************************PerrorLabelStyle***************************/\n"
"\n"
"*[styleSheet=\"PerrorLabelStyle\"]\n"
"{\n"
"	color:rgb(255, 99, 94);\n"
"}\n"
"\n"
"/**************************PmessageLabelStyle***************************/\n"
"\n"
"*[styleSheet=\"PmessageLabelStyle\"]\n"
"{\n"
"	color: white;\n"
"	padding-left: 0px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.PointStyleSheet)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.PointStyleSheet)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"PmainFrameStyle")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.inner_frame = QFrame(self.main_frame)
        self.inner_frame.setObjectName(u"inner_frame")
        self.inner_frame.setStyleSheet(u"PinnerFrameStyle")
        self.inner_frame.setFrameShape(QFrame.StyledPanel)
        self.inner_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.inner_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 9, 5, 0)
        self.top_frame = QFrame(self.inner_frame)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setStyleSheet(u"PtopFrameStyle")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 9)
        self.horizontalSpacer = QSpacerItem(315, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"PcloseButtonStyle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.close_btn)


        self.verticalLayout_4.addWidget(self.top_frame)

        self.frame = QFrame(self.inner_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verify_frame = QFrame(self.frame)
        self.verify_frame.setObjectName(u"verify_frame")
        self.verify_frame.setStyleSheet(u"PverifyFrameStyle")
        self.verify_frame.setFrameShape(QFrame.StyledPanel)
        self.verify_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.verify_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_11 = QSpacerItem(13, 124, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 20, 0, 20)
        self.verify_message = QLabel(self.verify_frame)
        self.verify_message.setObjectName(u"verify_message")
        self.verify_message.setStyleSheet(u"PmessageLabelStyle")

        self.verticalLayout_5.addWidget(self.verify_message)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verify_password_input = QLineEdit(self.verify_frame)
        self.verify_password_input.setObjectName(u"verify_password_input")
        self.verify_password_input.setMinimumSize(QSize(200, 40))
        self.verify_password_input.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.verify_password_input.setFont(font)
        self.verify_password_input.setStyleSheet(u"")
        self.verify_password_input.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_12.addWidget(self.verify_password_input)

        self.verify_eye_btn = QPushButton(self.verify_frame)
        self.verify_eye_btn.setObjectName(u"verify_eye_btn")
        sizePolicy1.setHeightForWidth(self.verify_eye_btn.sizePolicy().hasHeightForWidth())
        self.verify_eye_btn.setSizePolicy(sizePolicy1)
        self.verify_eye_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.verify_eye_btn.setStyleSheet(u"PeyeButtonStyle")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/white_eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verify_eye_btn.setIcon(icon1)

        self.horizontalLayout_12.addWidget(self.verify_eye_btn)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_12 = QSpacerItem(13, 124, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.verify_btn = QPushButton(self.verify_frame)
        self.verify_btn.setObjectName(u"verify_btn")
        self.verify_btn.setMinimumSize(QSize(200, 40))
        self.verify_btn.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.verify_btn.setFont(font1)
        self.verify_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.verify_btn.setStyleSheet(u"PverifyButtonStyle")

        self.verticalLayout_11.addWidget(self.verify_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verify_error_lbl = QLabel(self.verify_frame)
        self.verify_error_lbl.setObjectName(u"verify_error_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verify_error_lbl.sizePolicy().hasHeightForWidth())
        self.verify_error_lbl.setSizePolicy(sizePolicy2)
        self.verify_error_lbl.setStyleSheet(u"PerrorLabelStyle")
        self.verify_error_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.verify_error_lbl)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.verify_frame)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.inner_frame)


        self.verticalLayout_8.addWidget(self.main_frame)


        self.verticalLayout_2.addWidget(self.PointStyleSheet)


        self.verticalLayout_6.addWidget(self.LocalStyleSheet)


        self.verticalLayout.addWidget(self.GlobalStyleSheet)


        self.retranslateUi(verifyDialogWin)

        QMetaObject.connectSlotsByName(verifyDialogWin)
    # setupUi

    def retranslateUi(self, verifyDialogWin):
        verifyDialogWin.setWindowTitle(QCoreApplication.translate("verifyDialogWin", u"Dialog", None))
        self.close_btn.setText("")
        self.verify_message.setText(QCoreApplication.translate("verifyDialogWin", u"Enter Your Password", None))
        self.verify_password_input.setText(QCoreApplication.translate("verifyDialogWin", u"admin", None))
        self.verify_password_input.setPlaceholderText(QCoreApplication.translate("verifyDialogWin", u"Password", None))
        self.verify_eye_btn.setText("")
        self.verify_btn.setText(QCoreApplication.translate("verifyDialogWin", u"VERIFY", None))
        self.verify_error_lbl.setText("")
    # retranslateUi

