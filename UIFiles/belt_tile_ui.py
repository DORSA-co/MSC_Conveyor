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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Tile(object):
    def setupUi(self, Tile):
        if not Tile.objectName():
            Tile.setObjectName(u"Tile")
        Tile.resize(302, 149)
        self.verticalLayout = QVBoxLayout(Tile)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.StyleSheet = QWidget(Tile)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.verticalLayout_2 = QVBoxLayout(self.StyleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.StyleSheet)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.meterage_label = QLabel(self.frame)
        self.meterage_label.setObjectName(u"meterage_label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.meterage_label.setFont(font)

        self.verticalLayout_3.addWidget(self.meterage_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.StyleSheet)


        self.retranslateUi(Tile)

        QMetaObject.connectSlotsByName(Tile)
    # setupUi

    def retranslateUi(self, Tile):
        Tile.setWindowTitle(QCoreApplication.translate("Tile", u"Form", None))
        self.meterage_label.setText(QCoreApplication.translate("Tile", u"0 - 10 m", None))
    # retranslateUi

