# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defectType.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1068, 406)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 50))
        self.label_6.setMaximumSize(QSize(50, 50))
        self.label_6.setStyleSheet(u"background-color:red;")

        self.horizontalLayout.addWidget(self.label_6)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.spinBox_3 = QSpinBox(Form)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.spinBox_4 = QSpinBox(Form)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout.addWidget(self.spinBox_4, 0, 3, 1, 1)

        self.spinBox_2 = QSpinBox(Form)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout.addWidget(self.spinBox_2, 1, 3, 1, 1)

        self.spinBox_5 = QSpinBox(Form)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.gridLayout.addWidget(self.spinBox_5, 1, 1, 1, 1)

        self.spinBox_6 = QSpinBox(Form)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout.addWidget(self.spinBox_6, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Class Name", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Color:", None))
        self.label_6.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Signal", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Width", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Lenght", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"Depth", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"< x <", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"< x <", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"< x <", None))
    # retranslateUi

