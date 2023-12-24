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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import Assets_rc

class Ui_editUserDialogWin(object):
    def setupUi(self, editUserDialogWin):
        if not editUserDialogWin.objectName():
            editUserDialogWin.setObjectName(u"editUserDialogWin")
        editUserDialogWin.resize(550, 442)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editUserDialogWin.sizePolicy().hasHeightForWidth())
        editUserDialogWin.setSizePolicy(sizePolicy)
        editUserDialogWin.setMinimumSize(QSize(550, 400))
        editUserDialogWin.setMaximumSize(QSize(550, 442))
        editUserDialogWin.setStyleSheet(u"*{\n"
"	\n"
"	font: auto \"Arial\";\n"
"	font-size: 14px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"#editUserDialogWin{\n"
"	background-color: rgb(250, 250, 250);\n"
"	\n"
"	border:3px solid rgb(12, 53, 106);\n"
"	\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	min-height: 40px;\n"
"	border-radius: 5px;\n"
"\n"
"	\n"
"}\n"
"/*\n"
"QPushButton:hover{\n"
"\n"
"	background-color:rgb(22, 38, 76);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	color: #808080;\n"
"	background-color:rgb(210, 210, 210);\n"
"\n"
"}\n"
"*/\n"
"\n"
"/*********************************************/\n"
"QLabel{\n"
"	color: rgb(50,50,50);\n"
"color: #202020;\n"
"}\n"
"\n"
"\n"
"/*********************************************/\n"
"\n"
"\n"
"/*******************************************/\n"
"QLineEdit\n"
"{\n"
"	border:2px solid rgb(6, 76, 130);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"    min-width: 6em;\n"
"	min-height: 35px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"\n"
""
                        "\n"
"/*******************************************/\n"
"\n"
"\n"
"QGroupBox{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 1px solid black;\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	color: rgb(6, 76, 130);\n"
"	background: #ffffff;\n"
"	selection-background-color: rgb(255, 204, 75);\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"	background: #e4f0fa;\n"
"}\n"
"\n"
"\n"
"/*********************************************/\n"
"QComboBox\n"
"{\n"
"	border:2px solid rgb(12, 53, 105);\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 8px;\n"
"    min-width: 6em;\n"
"	min-height: 35px;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QComboBox:enabled{\n"
"color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QComboBox:disabled\n"
"{\n"
"	border:2px solid rgb(210, 210, 210);\n"
"	color:(210, 210, 210);\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{   \n"
"	image: url(:/icons/icon/icons8-down-white-48.png);\n"
"	width: 15px;\n"
"    height: 15px;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	 backgrou"
                        "nd-color: rgb(12, 53, 106);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled \n"
"{\n"
"	 background-color: rgb(210, 210, 210);\n"
"	 min-width: 30px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"    selection-background-color: rgb(6, 76, 130);\n"
"	selection-color: rgb(6, 76, 130);\n"
"\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    border: none;\n"
"	height:30px;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(editUserDialogWin)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(60, 40, 60, 40)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(50)
        self.username_input = QLineEdit(editUserDialogWin)
        self.username_input.setObjectName(u"username_input")

        self.gridLayout.addWidget(self.username_input, 0, 1, 1, 1)

        self.role_combobox = QComboBox(editUserDialogWin)
        self.role_combobox.setObjectName(u"role_combobox")

        self.gridLayout.addWidget(self.role_combobox, 2, 1, 1, 1)

        self.label_2 = QLabel(editUserDialogWin)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(editUserDialogWin)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label = QLabel(editUserDialogWin)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.password_input = QLineEdit(editUserDialogWin)
        self.password_input.setObjectName(u"password_input")

        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.error_lbl = QLabel(editUserDialogWin)
        self.error_lbl.setObjectName(u"error_lbl")
        self.error_lbl.setStyleSheet(u"color:rgb(255, 99, 94);")

        self.verticalLayout.addWidget(self.error_lbl)

        self.horizontalFrame = QFrame(editUserDialogWin)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.save_btn = QPushButton(self.horizontalFrame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(12, 53, 106);\n"
"color:#ffffff;\n"
"max-width: 200px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(6, 29, 56);\n"
"color:#ffffff;\n"
"max-width: 200px;\n"
"}")

        self.horizontalLayout.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(self.horizontalFrame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(12, 53, 106);\n"
"color:#ffffff;\n"
"max-width: 200px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(6, 29, 56);\n"
"color:#ffffff;\n"
"max-width: 200px;\n"
"}")

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addWidget(self.horizontalFrame)


        self.retranslateUi(editUserDialogWin)

        QMetaObject.connectSlotsByName(editUserDialogWin)
    # setupUi

    def retranslateUi(self, editUserDialogWin):
        editUserDialogWin.setWindowTitle(QCoreApplication.translate("editUserDialogWin", u"Edit User", None))
        self.label_2.setText(QCoreApplication.translate("editUserDialogWin", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("editUserDialogWin", u"Role", None))
        self.label.setText(QCoreApplication.translate("editUserDialogWin", u"Username", None))
        self.error_lbl.setText(QCoreApplication.translate("editUserDialogWin", u"Error", None))
        self.save_btn.setText(QCoreApplication.translate("editUserDialogWin", u"Save", None))
        self.cancel_btn.setText(QCoreApplication.translate("editUserDialogWin", u"Cancel", None))
    # retranslateUi

