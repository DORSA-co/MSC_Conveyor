# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from GUIComponents import PhotoViewer
import assets_rc

class Ui_ViewerWindow(object):
    def setupUi(self, ViewerWindow):
        if not ViewerWindow.objectName():
            ViewerWindow.setObjectName(u"ViewerWindow")
        ViewerWindow.resize(798, 758)
        self.GlobalStyleSheet = QWidget(ViewerWindow)
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
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	color: rgb(120, 120, 120);\n"
"}\n"
"\n"
"/**************************QGraphicsView***************************/\n"
"\n"
"QGraphicsView{\n"
"	border: None;\n"
"}\n"
"\n"
"/**************************QTable***************************/\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"	gridline-color: #D7D7D9;\n"
"	color: rgb(20, 20, 20);\n"
"	border: 2px solid #D7D7D9;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #E0E4EC;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom: 2px solid #BDBDBF;\n"
"	border-right: 1px solid #D7D7D9;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"   border-top-left-radius: 4px;\n"
"	border-left: None"
                        ";\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"   border-top-right-radius: 4px;\n"
"	border-right: None;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #E0E4EC;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #D7D7D9;\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"	\n"
"	image: url(:/icons/icons/table_sort_icon.png);\n"
"}\n"
"\n"
"/**************************QScrollBar***************************/\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #D7D7D9;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
" "
                        "   height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #D7D7D9;\n"
"    min-width: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #F7F8FA;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.GlobalStyleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LocalStyleSheet = QWidget(self.GlobalStyleSheet)
        self.LocalStyleSheet.setObjectName(u"LocalStyleSheet")
        self.LocalStyleSheet.setStyleSheet(u"/**************************LtopFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"LtopFrameStyle\"]\n"
"{\n"
"	background-color: #F7F8FA;\n"
"}\n"
"\n"
"*[styleSheet=\"LtopFrameStyle\"] .QPushButton{\n"
"	border: 0px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.LocalStyleSheet)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PointStyleSheet = QWidget(self.LocalStyleSheet)
        self.PointStyleSheet.setObjectName(u"PointStyleSheet")
        self.PointStyleSheet.setStyleSheet(u"/**************************PmainStackedWidgetStyle*******************/\n"
"\n"
"*[styleSheet=\"PmainStackedWidgetStyle\"]\n"
"{\n"
"	background-color: #E0E4EC;\n"
"}\n"
"\n"
"/**************************PtileScrollAreaStyle*******************/\n"
"\n"
"*[styleSheet=\"PtileScrollAreaStyle\"]\n"
"{\n"
"	background-color: #ebf0f7;\n"
"	border: 2px solid #ebf0f7;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"/**************************PtileFrameStyle*******************/\n"
"\n"
"*[styleSheet=\"PtileFrameStyle\"]\n"
"{\n"
"	background-color: #ebf0f7;\n"
"	border:None;\n"
"}\n"
"\n"
"/**************************P3dviewButtonStyle*******************/\n"
"\n"
"*[styleSheet=\"P3dviewButtonStyle\"]\n"
"{\n"
"	background-color: transparent;\n"
"	color:  rgba(46, 76, 153, 255);\n"
"	border-radius: 20px;\n"
"	min-width: 100;\n"
"	max-width: 100;\n"
"	min-height: 40;\n"
"	max-height: 40;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	text-align: right;\n"
"}\n"
"\n"
"*[styleSheet=\"P3dviewButtonStyle\"]:disabled\n"
"{\n"
"	colo"
                        "r:  rgba(120, 120, 120, 255);\n"
"}\n"
"\n"
"*[styleSheet=\"P3dviewButtonStyle\"]:hover\n"
"{\n"
"	color:  rgba(76, 126, 255, 255);\n"
"}\n"
"\n"
"*[styleSheet=\"P3dviewButtonStyle\"]:pressed\n"
"{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"/**************************PimageViewerStyle*******************/\n"
"\n"
"*[styleSheet=\"PimageViewerStyle\"]\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.PointStyleSheet)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.PointStyleSheet)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setStyleSheet(u"LtopFrameStyle")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.help_btn = QPushButton(self.top_frame)
        self.help_btn.setObjectName(u"help_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
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


        self.verticalLayout_4.addWidget(self.top_frame)

        self.main_stackedWidget = QStackedWidget(self.PointStyleSheet)
        self.main_stackedWidget.setObjectName(u"main_stackedWidget")
        self.main_stackedWidget.setStyleSheet(u"PmainStackedWidgetStyle")
        self.image_page = QWidget()
        self.image_page.setObjectName(u"image_page")
        self.verticalLayout_3 = QVBoxLayout(self.image_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.view_3d_btn = QPushButton(self.image_page)
        self.view_3d_btn.setObjectName(u"view_3d_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.view_3d_btn.sizePolicy().hasHeightForWidth())
        self.view_3d_btn.setSizePolicy(sizePolicy2)
        self.view_3d_btn.setMinimumSize(QSize(100, 40))
        self.view_3d_btn.setMaximumSize(QSize(100, 40))
        self.view_3d_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.view_3d_btn.setStyleSheet(u"P3dviewButtonStyle")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/view_3d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.view_3d_btn.setIcon(icon4)
        self.view_3d_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.view_3d_btn, 0, Qt.AlignLeft)

        self.tile_image_viewer = PhotoViewer(self.image_page)
        self.tile_image_viewer.setObjectName(u"tile_image_viewer")
        self.tile_image_viewer.setMinimumSize(QSize(780, 413))
        self.tile_image_viewer.setStyleSheet(u"PimageViewerStyle")

        self.verticalLayout_3.addWidget(self.tile_image_viewer)

        self.viewer_defect_table = QTableWidget(self.image_page)
        if (self.viewer_defect_table.columnCount() < 2):
            self.viewer_defect_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.viewer_defect_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.viewer_defect_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.viewer_defect_table.rowCount() < 1):
            self.viewer_defect_table.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.viewer_defect_table.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.viewer_defect_table.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.viewer_defect_table.setItem(0, 1, __qtablewidgetitem4)
        self.viewer_defect_table.setObjectName(u"viewer_defect_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.viewer_defect_table.sizePolicy().hasHeightForWidth())
        self.viewer_defect_table.setSizePolicy(sizePolicy3)
        self.viewer_defect_table.setMinimumSize(QSize(0, 90))
        self.viewer_defect_table.setMaximumSize(QSize(16777215, 90))
        self.viewer_defect_table.horizontalHeader().setDefaultSectionSize(150)
        self.viewer_defect_table.horizontalHeader().setStretchLastSection(True)
        self.viewer_defect_table.verticalHeader().setVisible(False)
        self.viewer_defect_table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.viewer_defect_table)

        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.tiles_scrollArea = QScrollArea(self.image_page)
        self.tiles_scrollArea.setObjectName(u"tiles_scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tiles_scrollArea.sizePolicy().hasHeightForWidth())
        self.tiles_scrollArea.setSizePolicy(sizePolicy4)
        self.tiles_scrollArea.setMinimumSize(QSize(0, 120))
        self.tiles_scrollArea.setMaximumSize(QSize(16777215, 120))
        self.tiles_scrollArea.setStyleSheet(u"PtileScrollAreaStyle")
        self.tiles_scrollArea.setWidgetResizable(True)
        self.tiles_frame = QWidget()
        self.tiles_frame.setObjectName(u"tiles_frame")
        self.tiles_frame.setGeometry(QRect(0, 0, 776, 116))
        self.tiles_frame.setStyleSheet(u"PtileFrameStyle")
        self.horizontalLayout = QHBoxLayout(self.tiles_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.tiles_scrollArea.setWidget(self.tiles_frame)

        self.verticalLayout_3.addWidget(self.tiles_scrollArea)

        self.main_stackedWidget.addWidget(self.image_page)

        self.verticalLayout_4.addWidget(self.main_stackedWidget)


        self.verticalLayout_2.addWidget(self.PointStyleSheet)


        self.verticalLayout.addWidget(self.LocalStyleSheet)

        ViewerWindow.setCentralWidget(self.GlobalStyleSheet)

        self.retranslateUi(ViewerWindow)

        QMetaObject.connectSlotsByName(ViewerWindow)
    # setupUi

    def retranslateUi(self, ViewerWindow):
        ViewerWindow.setWindowTitle(QCoreApplication.translate("ViewerWindow", u"MainWindow", None))
        self.help_btn.setText("")
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
        self.view_3d_btn.setText(QCoreApplication.translate("ViewerWindow", u"3D View", None))
        ___qtablewidgetitem = self.viewer_defect_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ViewerWindow", u"x", None));
        ___qtablewidgetitem1 = self.viewer_defect_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ViewerWindow", u"y", None));
        ___qtablewidgetitem2 = self.viewer_defect_table.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ViewerWindow", u"New Row", None));

        __sortingEnabled = self.viewer_defect_table.isSortingEnabled()
        self.viewer_defect_table.setSortingEnabled(False)
        self.viewer_defect_table.setSortingEnabled(__sortingEnabled)

    # retranslateUi

