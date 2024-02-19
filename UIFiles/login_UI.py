# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_loginDialogWin(object):
    def setupUi(self, loginDialogWin):
        if not loginDialogWin.objectName():
            loginDialogWin.setObjectName(u"loginDialogWin")
        loginDialogWin.resize(372, 533)
        self.verticalLayout = QVBoxLayout(loginDialogWin)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalStyleSheet = QWidget(loginDialogWin)
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
"	border-image: url(:/icons/icons/bg_image.jpg);\n"
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
"/**************************PloginFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PloginFrameStyle\"]\n"
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
"/**************************PloginButtonStyle***************************/\n"
"\n"
"*[styleSheet=\"PloginButtonStyle\"]\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(126, 132, 162), stop:1 rgb(31, 42, 77));\n"
"	color: rgba(255, 255, 255, 210);"
                        "\n"
"	border-radius: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"*[styleSheet=\"PloginButtonStyle\"]:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(139, 146, 179), stop:1 rgba(40, 67, 98, 219));\n"
"}\n"
"\n"
"*[styleSheet=\"PloginButtonStyle\"]:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"/**************************PerrorLabelStyle***************************/\n"
"\n"
"*[styleSheet=\"PerrorLabelStyle\"]\n"
"{\n"
"	color:rgb(255, 99, 94);\n"
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
        self.top_frame.setStyleSheet(u"PtopFrameStyle")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 50)
        self.horizontalSpacer = QSpacerItem(315, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
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
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.login_frame = QFrame(self.frame)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setStyleSheet(u"PloginFrameStyle")
        self.login_frame.setFrameShape(QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.login_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 50, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(13, 124, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.username_icon = QLabel(self.login_frame)
        self.username_icon.setObjectName(u"username_icon")
        sizePolicy.setHeightForWidth(self.username_icon.sizePolicy().hasHeightForWidth())
        self.username_icon.setSizePolicy(sizePolicy)
        self.username_icon.setMaximumSize(QSize(25, 25))
        self.username_icon.setPixmap(QPixmap(u":/icons/icons/username.png"))
        self.username_icon.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.username_icon)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.username_input = QLineEdit(self.login_frame)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(200, 40))
        self.username_input.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.username_input)

        self.temp_btn = QPushButton(self.login_frame)
        self.temp_btn.setObjectName(u"temp_btn")
        self.temp_btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.temp_btn.sizePolicy().hasHeightForWidth())
        self.temp_btn.setSizePolicy(sizePolicy)
        self.temp_btn.setMinimumSize(QSize(20, 16))
        self.temp_btn.setMaximumSize(QSize(20, 16))
        self.temp_btn.setStyleSheet(u"PtempButtonStyle")

        self.horizontalLayout_3.addWidget(self.temp_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.password_icon = QLabel(self.login_frame)
        self.password_icon.setObjectName(u"password_icon")
        sizePolicy.setHeightForWidth(self.password_icon.sizePolicy().hasHeightForWidth())
        self.password_icon.setSizePolicy(sizePolicy)
        self.password_icon.setMaximumSize(QSize(25, 25))
        self.password_icon.setPixmap(QPixmap(u":/icons/icons/password.png"))
        self.password_icon.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.password_icon)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.password_input = QLineEdit(self.login_frame)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(200, 40))
        self.password_input.setMaximumSize(QSize(200, 40))
        self.password_input.setFont(font)
        self.password_input.setStyleSheet(u"")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.password_input)

        self.eye_btn = QPushButton(self.login_frame)
        self.eye_btn.setObjectName(u"eye_btn")
        sizePolicy.setHeightForWidth(self.eye_btn.sizePolicy().hasHeightForWidth())
        self.eye_btn.setSizePolicy(sizePolicy)
        self.eye_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.eye_btn.setStyleSheet(u"PeyeButtonStyle")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/white_eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eye_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.eye_btn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_10 = QSpacerItem(13, 124, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.login_btn = QPushButton(self.login_frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(200, 40))
        self.login_btn.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.login_btn.setFont(font1)
        self.login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn.setStyleSheet(u"PloginButtonStyle")

        self.verticalLayout_5.addWidget(self.login_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.login_error_lbl = QLabel(self.login_frame)
        self.login_error_lbl.setObjectName(u"login_error_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login_error_lbl.sizePolicy().hasHeightForWidth())
        self.login_error_lbl.setSizePolicy(sizePolicy1)
        self.login_error_lbl.setStyleSheet(u"PerrorLabelStyle")
        self.login_error_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.login_error_lbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_10.addWidget(self.login_frame)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.inner_frame)


        self.verticalLayout_8.addWidget(self.main_frame)


        self.verticalLayout_2.addWidget(self.PointStyleSheet)


        self.verticalLayout_6.addWidget(self.LocalStyleSheet)


        self.verticalLayout.addWidget(self.GlobalStyleSheet)


        self.retranslateUi(loginDialogWin)

        QMetaObject.connectSlotsByName(loginDialogWin)
    # setupUi

    def retranslateUi(self, loginDialogWin):
        loginDialogWin.setWindowTitle(QCoreApplication.translate("loginDialogWin", u"Dialog", None))
        self.close_btn.setText("")
        self.username_icon.setText("")
        self.username_input.setText(QCoreApplication.translate("loginDialogWin", u"admin", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("loginDialogWin", u"Username", None))
        self.temp_btn.setText("")
        self.password_icon.setText("")
        self.password_input.setText(QCoreApplication.translate("loginDialogWin", u"admin", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("loginDialogWin", u"Password", None))
        self.eye_btn.setText("")
        self.login_btn.setText(QCoreApplication.translate("loginDialogWin", u"LOGIN", None))
        self.login_error_lbl.setText("")
    # retranslateUi

