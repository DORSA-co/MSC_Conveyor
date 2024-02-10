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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_Tile(object):
    def setupUi(self, Tile):
        if not Tile.objectName():
            Tile.setObjectName(u"Tile")
        Tile.resize(300, 123)
        self.verticalLayout = QVBoxLayout(Tile)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.StyleSheet = QWidget(Tile)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"*{\n"
"	font: auto \"Roboto\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
"#main_frame\n"
"{\n"
"	border:None;\n"
"	background-color: #E0E4EC;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.StyleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.StyleSheet)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(300, 0))
        self.main_frame.setMaximumSize(QSize(300, 16777215))
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.inner_frame = QFrame(self.main_frame)
        self.inner_frame.setObjectName(u"inner_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inner_frame.sizePolicy().hasHeightForWidth())
        self.inner_frame.setSizePolicy(sizePolicy)
        self.inner_frame.setStyleSheet(u"border: None;\n"
"background-color: None;")
        self.inner_frame.setFrameShape(QFrame.StyledPanel)
        self.inner_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.inner_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.meterage_low_label = QLabel(self.inner_frame)
        self.meterage_low_label.setObjectName(u"meterage_low_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.meterage_low_label.sizePolicy().hasHeightForWidth())
        self.meterage_low_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.meterage_low_label.setFont(font)
        self.meterage_low_label.setStyleSheet(u"color: #707070;")

        self.verticalLayout_5.addWidget(self.meterage_low_label, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.inner_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #707070;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.arrow_frame = QFrame(self.inner_frame)
        self.arrow_frame.setObjectName(u"arrow_frame")
        self.arrow_frame.setMinimumSize(QSize(120, 22))
        self.arrow_frame.setMaximumSize(QSize(120, 16777215))
        self.arrow_frame.setStyleSheet(u"background-image: url(:/icons/icons/two_side_arrow.png);\n"
"background-repeat: false;\n"
"background-position: center;\n"
"")
        self.arrow_frame.setFrameShape(QFrame.StyledPanel)
        self.arrow_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.arrow_frame)

        self.verticalSpacer_3 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.meterage_high_label = QLabel(self.inner_frame)
        self.meterage_high_label.setObjectName(u"meterage_high_label")
        sizePolicy1.setHeightForWidth(self.meterage_high_label.sizePolicy().hasHeightForWidth())
        self.meterage_high_label.setSizePolicy(sizePolicy1)
        self.meterage_high_label.setFont(font)
        self.meterage_high_label.setStyleSheet(u"color: #707070;")

        self.verticalLayout_6.addWidget(self.meterage_high_label, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.inner_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #707070;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.inner_frame)

        self.select_label = QLabel(self.main_frame)
        self.select_label.setObjectName(u"select_label")
        self.select_label.setMinimumSize(QSize(0, 8))
        self.select_label.setMaximumSize(QSize(16777215, 8))
        self.select_label.setStyleSheet(u"background-color: #E0E4EC;\n"
"border-radius: 4px;")

        self.verticalLayout_3.addWidget(self.select_label)


        self.verticalLayout_2.addWidget(self.main_frame)


        self.verticalLayout.addWidget(self.StyleSheet)


        self.retranslateUi(Tile)

        QMetaObject.connectSlotsByName(Tile)
    # setupUi

    def retranslateUi(self, Tile):
        Tile.setWindowTitle(QCoreApplication.translate("Tile", u"Form", None))
        self.meterage_low_label.setText(QCoreApplication.translate("Tile", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Tile", u"meter", None))
        self.meterage_high_label.setText(QCoreApplication.translate("Tile", u"10 ", None))
        self.label_4.setText(QCoreApplication.translate("Tile", u"meter", None))
        self.select_label.setText("")
    # retranslateUi

