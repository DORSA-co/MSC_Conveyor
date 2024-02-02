# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_viewer2.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import assets_rc

class Ui_ViewerWindow(object):
    def setupUi(self, ViewerWindow):
        if not ViewerWindow.objectName():
            ViewerWindow.setObjectName(u"ViewerWindow")
        ViewerWindow.resize(800, 600)
        self.StyleSheet = QWidget(ViewerWindow)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"QLabel{\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
"#top_frame{\n"
"	background-color: #7E84A2;\n"
"}\n"
"\n"
"#top_frame QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"#main_stackedWidget{\n"
"	background-color: #17203A;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.StyleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.StyleSheet)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.logined_username_lbl = QLabel(self.top_frame)
        self.logined_username_lbl.setObjectName(u"logined_username_lbl")

        self.horizontalLayout_14.addWidget(self.logined_username_lbl)

        self.help_btn = QPushButton(self.top_frame)
        self.help_btn.setObjectName(u"help_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.help_btn.sizePolicy().hasHeightForWidth())
        self.help_btn.setSizePolicy(sizePolicy1)
        self.help_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/help_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btn.setIcon(icon)
        self.help_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_14.addWidget(self.help_btn)

        self.minimize_btn = QPushButton(self.top_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy1.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy1)
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.top_frame)
        self.maximize_btn.setObjectName(u"maximize_btn")
        sizePolicy1.setHeightForWidth(self.maximize_btn.sizePolicy().hasHeightForWidth())
        self.maximize_btn.setSizePolicy(sizePolicy1)
        self.maximize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon2)
        self.maximize_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_14.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_stackedWidget = QStackedWidget(self.StyleSheet)
        self.main_stackedWidget.setObjectName(u"main_stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.main_stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.main_stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.main_stackedWidget)

        ViewerWindow.setCentralWidget(self.StyleSheet)

        self.retranslateUi(ViewerWindow)

        QMetaObject.connectSlotsByName(ViewerWindow)
    # setupUi

    def retranslateUi(self, ViewerWindow):
        ViewerWindow.setWindowTitle(QCoreApplication.translate("ViewerWindow", u"MainWindow", None))
        self.logined_username_lbl.setText("")
        self.help_btn.setText("")
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
    # retranslateUi

