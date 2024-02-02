# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QMainWindow, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(717, 586)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(16)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.report_low_depth_input = QDoubleSpinBox(self.page)
        self.report_low_depth_input.setObjectName(u"report_low_depth_input")

        self.horizontalLayout_33.addWidget(self.report_low_depth_input)

        self.report_depth_to_label = QLabel(self.page)
        self.report_depth_to_label.setObjectName(u"report_depth_to_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report_depth_to_label.sizePolicy().hasHeightForWidth())
        self.report_depth_to_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_33.addWidget(self.report_depth_to_label)

        self.report_high_depth_input = QDoubleSpinBox(self.page)
        self.report_high_depth_input.setObjectName(u"report_high_depth_input")

        self.horizontalLayout_33.addWidget(self.report_high_depth_input)


        self.verticalLayout_2.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(16)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, -1, -1, 10)
        self.report_depth_checkBox = QCheckBox(self.page)
        self.report_depth_checkBox.setObjectName(u"report_depth_checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.report_depth_checkBox.sizePolicy().hasHeightForWidth())
        self.report_depth_checkBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_39.addWidget(self.report_depth_checkBox)

        self.report_depth_label = QLabel(self.page)
        self.report_depth_label.setObjectName(u"report_depth_label")

        self.horizontalLayout_39.addWidget(self.report_depth_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(16)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, -1, -1, 10)
        self.report_class_checkBox = QCheckBox(self.page)
        self.report_class_checkBox.setObjectName(u"report_class_checkBox")
        sizePolicy1.setHeightForWidth(self.report_class_checkBox.sizePolicy().hasHeightForWidth())
        self.report_class_checkBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_36.addWidget(self.report_class_checkBox)

        self.report_class_label = QLabel(self.page)
        self.report_class_label.setObjectName(u"report_class_label")

        self.horizontalLayout_36.addWidget(self.report_class_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_36)

        self.report_class_comboBox = QComboBox(self.page)
        self.report_class_comboBox.setObjectName(u"report_class_comboBox")

        self.verticalLayout_2.addWidget(self.report_class_comboBox)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.report_depth_to_label.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.report_depth_checkBox.setText("")
        self.report_depth_label.setText(QCoreApplication.translate("MainWindow", u"Depth (mm)", None))
        self.report_class_checkBox.setText("")
        self.report_class_label.setText(QCoreApplication.translate("MainWindow", u"Class", None))
    # retranslateUi

