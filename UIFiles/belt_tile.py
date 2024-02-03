# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'belt_tile.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import assets_rc

class Ui_Tile(object):
    def setupUi(self, Tile):
        if not Tile.objectName():
            Tile.setObjectName(u"Tile")
        Tile.resize(300, 146)
        self.verticalLayout = QVBoxLayout(Tile)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.StyleSheet = QWidget(Tile)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"#frame\n"
"{\n"
"	border:None;\n"
"	background-color: #F7F8FA;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.StyleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.StyleSheet)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.meterage_low_label = QLabel(self.frame)
        self.meterage_low_label.setObjectName(u"meterage_low_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meterage_low_label.sizePolicy().hasHeightForWidth())
        self.meterage_low_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.meterage_low_label.setFont(font)

        self.horizontalLayout.addWidget(self.meterage_low_label)

        self.left_arrow = QPushButton(self.frame)
        self.left_arrow.setObjectName(u"left_arrow")
        self.left_arrow.setStyleSheet(u"#left_arrow{\n"
"	border: 0px solid gray;\n"
"}")

        self.horizontalLayout.addWidget(self.left_arrow)

        self.right_arrow = QPushButton(self.frame)
        self.right_arrow.setObjectName(u"right_arrow")
        self.right_arrow.setStyleSheet(u"#right_arrow{\n"
"	border: 0px solid gray;\n"
"}")

        self.horizontalLayout.addWidget(self.right_arrow)

        self.meterage_high_label = QLabel(self.frame)
        self.meterage_high_label.setObjectName(u"meterage_high_label")
        sizePolicy.setHeightForWidth(self.meterage_high_label.sizePolicy().hasHeightForWidth())
        self.meterage_high_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.meterage_high_label.setFont(font1)

        self.horizontalLayout.addWidget(self.meterage_high_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.frame2 = QFrame(self.frame)
        self.frame2.setObjectName(u"frame2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy1)
        self.frame2.setStyleSheet(u"border: None;")
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame2)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: #7892DF;\n"
"min-height: 5px;\n"
"max-height: 5px;\n"
"border-radius: 2px;")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.StyleSheet)


        self.retranslateUi(Tile)

        QMetaObject.connectSlotsByName(Tile)
    # setupUi

    def retranslateUi(self, Tile):
        Tile.setWindowTitle(QCoreApplication.translate("Tile", u"Form", None))
        self.meterage_low_label.setText(QCoreApplication.translate("Tile", u"0", None))
        self.left_arrow.setText("")
        self.right_arrow.setText("")
        self.meterage_high_label.setText(QCoreApplication.translate("Tile", u"10 ", None))
        self.label.setText("")
        self.label_2.setText("")
    # retranslateUi

