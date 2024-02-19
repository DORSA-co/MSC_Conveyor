# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_user.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_editUserDialogWin(object):
    def setupUi(self, editUserDialogWin):
        if not editUserDialogWin.objectName():
            editUserDialogWin.setObjectName(u"editUserDialogWin")
        editUserDialogWin.resize(377, 529)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editUserDialogWin.sizePolicy().hasHeightForWidth())
        editUserDialogWin.setSizePolicy(sizePolicy)
        editUserDialogWin.setMinimumSize(QSize(0, 0))
        editUserDialogWin.setMaximumSize(QSize(16777215, 16777215))
        editUserDialogWin.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(editUserDialogWin)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalStyleSheet = QWidget(editUserDialogWin)
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
"	color: rgb(250, 250, 250);\n"
"	font-weight: bold;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"/**************************QLineEdit***************************/\n"
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
"	border-bottom: 2px solid #7E84A2;\n"
"}\n"
"\n"
"/**************************QComboBox***************************/\n"
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
"QComboBox:disab"
                        "led\n"
"{\n"
"	border: 2px solid #F0F0F2;\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled\n"
"{   \n"
"	image: url(:/icons/icons/down_icon_gray.png);\n"
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
"	border-bottom: 2px solid #7E84A2;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.GlobalStyleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
"}\n"
"\n"
"/**************************PframeStyle***************************/\n"
"\n"
"*[styleSheet=\"PframeStyle\"]\n"
"{\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"/**************************PsaveCancelStyle***************************/\n"
"\n"
"*[styleSheet=\"PsaveCancelStyle\"]\n"
"{\n"
"	bac"
                        "kground-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(126, 132, 162), stop:1 rgb(31, 42, 77));\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 20px;\n"
"	min-width: 135;\n"
"	max-width: 135;\n"
"	min-height: 40;\n"
"	max-height: 40;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"*[styleSheet=\"PsaveCancelStyle\"]:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(139, 146, 179), stop:1 rgba(40, 67, 98, 219));\n"
"}\n"
"\n"
"*[styleSheet=\"PsaveCancelStyle\"]:pressed {\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"/**************************PcloseButtonStyle***************************/\n"
"\n"
"*[styleSheet=\"PcloseButtonStyle\"]\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"/**************************PerrorLabelStyle***************************/\n"
"\n"
"*[styleSheet=\"PerrorLabelStyle\"]\n"
"{\n"
"	color:rgb(255, 99, 94);\n"
"}\n"
"\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.PointStyleSheet)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_7 = QVBoxLayout(self.inner_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.top_frame = QFrame(self.inner_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"PtopFrameStyle")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 30)
        self.horizontalSpacer_2 = QSpacerItem(315, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"PcloseButtonStyle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.close_btn)


        self.verticalLayout_7.addWidget(self.top_frame)

        self.frame = QFrame(self.inner_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"PframeStyle")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(35, 20, 35, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.username_label = QLabel(self.frame)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setEnabled(True)

        self.verticalLayout_4.addWidget(self.username_label)

        self.username_input = QLineEdit(self.frame)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(87, 37))

        self.verticalLayout_4.addWidget(self.username_input)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.password_label = QLabel(self.frame)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout_6.addWidget(self.password_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.password_input = QLineEdit(self.frame)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(87, 37))
        self.password_input.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_2.addWidget(self.password_input)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.role_label = QLabel(self.frame)
        self.role_label.setObjectName(u"role_label")

        self.verticalLayout_8.addWidget(self.role_label)

        self.role_combobox = QComboBox(self.frame)
        self.role_combobox.setObjectName(u"role_combobox")
        self.role_combobox.setMinimumSize(QSize(87, 37))

        self.verticalLayout_8.addWidget(self.role_combobox)


        self.verticalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.save_btn = QPushButton(self.frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_btn.setStyleSheet(u"PsaveCancelStyle")

        self.horizontalLayout_3.addWidget(self.save_btn, 0, Qt.AlignHCenter)

        self.cancel_btn = QPushButton(self.frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_btn.setStyleSheet(u"PsaveCancelStyle")

        self.horizontalLayout_3.addWidget(self.cancel_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.error_lbl = QLabel(self.frame)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setStyleSheet(u"PerrorLabelStyle")

        self.verticalLayout_5.addWidget(self.error_lbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.inner_frame)


        self.verticalLayout_9.addWidget(self.main_frame)


        self.verticalLayout_2.addWidget(self.PointStyleSheet)


        self.verticalLayout.addWidget(self.LocalStyleSheet)


        self.horizontalLayout.addWidget(self.GlobalStyleSheet)


        self.retranslateUi(editUserDialogWin)

        QMetaObject.connectSlotsByName(editUserDialogWin)
    # setupUi

    def retranslateUi(self, editUserDialogWin):
        editUserDialogWin.setWindowTitle(QCoreApplication.translate("editUserDialogWin", u"Edit User", None))
        self.close_btn.setText("")
        self.username_label.setText(QCoreApplication.translate("editUserDialogWin", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("editUserDialogWin", u"Password", None))
        self.role_label.setText(QCoreApplication.translate("editUserDialogWin", u"Role", None))
        self.save_btn.setText(QCoreApplication.translate("editUserDialogWin", u"Save", None))
        self.cancel_btn.setText(QCoreApplication.translate("editUserDialogWin", u"Cancel", None))
        self.error_lbl.setText("")
    # retranslateUi

