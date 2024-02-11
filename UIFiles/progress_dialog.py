# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_dialog.ui'
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
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_progressDialog(object):
    def setupUi(self, progressDialog):
        if not progressDialog.objectName():
            progressDialog.setObjectName(u"progressDialog")
        progressDialog.resize(798, 167)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(progressDialog.sizePolicy().hasHeightForWidth())
        progressDialog.setSizePolicy(sizePolicy)
        progressDialog.setMinimumSize(QSize(0, 0))
        progressDialog.setMaximumSize(QSize(16777215, 16777215))
        progressDialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(progressDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.StyleSheet = QWidget(progressDialog)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setStyleSheet(u"*{\n"
"	font: auto \"Roboto\";\n"
"}\n"
"\n"
"/************************************************************/\n"
"\n"
"#main_frame{\n"
"	background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(23, 32, 58, 255), stop:1 rgba(10, 14, 26, 255));	\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"#main_frame .QLabel{\n"
"	color: white;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.StyleSheet)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.StyleSheet)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(40, 22, 40, 22)
        self.title_frame = QFrame(self.main_frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.title_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.title_lbl = QLabel(self.title_frame)
        self.title_lbl.setObjectName(u"title_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_lbl.sizePolicy().hasHeightForWidth())
        self.title_lbl.setSizePolicy(sizePolicy1)
        self.title_lbl.setStyleSheet(u"font-size:22px;\n"
"font-weight: bold;")
        self.title_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title_lbl)

        self.dots_label = QLabel(self.title_frame)
        self.dots_label.setObjectName(u"dots_label")
        sizePolicy1.setHeightForWidth(self.dots_label.sizePolicy().hasHeightForWidth())
        self.dots_label.setSizePolicy(sizePolicy1)
        self.dots_label.setStyleSheet(u"font-size:22px;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.dots_label)

        self.leftp_label = QLabel(self.title_frame)
        self.leftp_label.setObjectName(u"leftp_label")
        sizePolicy1.setHeightForWidth(self.leftp_label.sizePolicy().hasHeightForWidth())
        self.leftp_label.setSizePolicy(sizePolicy1)
        self.leftp_label.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout.addWidget(self.leftp_label)

        self.progressbar_value_label = QLabel(self.title_frame)
        self.progressbar_value_label.setObjectName(u"progressbar_value_label")
        sizePolicy1.setHeightForWidth(self.progressbar_value_label.sizePolicy().hasHeightForWidth())
        self.progressbar_value_label.setSizePolicy(sizePolicy1)
        self.progressbar_value_label.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout.addWidget(self.progressbar_value_label)

        self.percent_rightp_label = QLabel(self.title_frame)
        self.percent_rightp_label.setObjectName(u"percent_rightp_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.percent_rightp_label.sizePolicy().hasHeightForWidth())
        self.percent_rightp_label.setSizePolicy(sizePolicy2)
        self.percent_rightp_label.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout.addWidget(self.percent_rightp_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.description_lbl = QLabel(self.title_frame)
        self.description_lbl.setObjectName(u"description_lbl")
        sizePolicy2.setHeightForWidth(self.description_lbl.sizePolicy().hasHeightForWidth())
        self.description_lbl.setSizePolicy(sizePolicy2)
        self.description_lbl.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.description_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.description_lbl)


        self.verticalLayout_3.addWidget(self.title_frame)

        self.progressbar = QProgressBar(self.main_frame)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setStyleSheet(u"QProgressBar {\n"
"	background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(80, 80, 80), stop: 1 rgb(180, 180, 180));\n"
"    border-radius: 5px;\n"
"	min-height: 10px;\n"
"	max-height: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 5px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                stop: 0 #F7F8FA, \n"
"                                stop: 0.3 #7E84A2,\n"
"                                stop: 0.6 #7892DF,\n"
"                                stop: 1 #4C7EFF);\n"
"}")
        self.progressbar.setValue(87)
        self.progressbar.setTextVisible(False)

        self.verticalLayout_3.addWidget(self.progressbar)

        self.progress_frame = QFrame(self.main_frame)
        self.progress_frame.setObjectName(u"progress_frame")
        self.progress_frame.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.progress_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(110, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.complete_count_lbl = QLabel(self.progress_frame)
        self.complete_count_lbl.setObjectName(u"complete_count_lbl")

        self.horizontalLayout_3.addWidget(self.complete_count_lbl)

        self.slash_label = QLabel(self.progress_frame)
        self.slash_label.setObjectName(u"slash_label")

        self.horizontalLayout_3.addWidget(self.slash_label)

        self.total_count_lbl = QLabel(self.progress_frame)
        self.total_count_lbl.setObjectName(u"total_count_lbl")

        self.horizontalLayout_3.addWidget(self.total_count_lbl)

        self.progress_operetion_lbl = QLabel(self.progress_frame)
        self.progress_operetion_lbl.setObjectName(u"progress_operetion_lbl")

        self.horizontalLayout_3.addWidget(self.progress_operetion_lbl)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.cancel_btn = QPushButton(self.progress_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setEnabled(True)
        self.cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_btn.setStyleSheet(u"#cancel_btn\n"
"{\n"
"	border: 2px solid  #7892df;\n"
"	color:  #8aa7ff;\n"
"	border-radius: 18px;\n"
"	min-width: 100;\n"
"	max-width: 100;\n"
"	min-height: 36;\n"
"	max-height: 36;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	qproperty-icon: url(:/icons/icons/cancel_icon.png);\n"
"}\n"
"\n"
"#cancel_btn:disabled\n"
"{\n"
"	border: 2px solid rgba(189, 189, 191, 255);\n"
"	color: rgba(120, 120, 120, 255);\n"
"}\n"
"\n"
"#cancel_btn:hover\n"
"{\n"
"	border: 2px solid rgba(76, 126, 255, 255);\n"
"	color:  rgba(76, 126, 255, 255);\n"
"	qproperty-icon: url(:/icons/icons/cancel_hover.png);\n"
"}\n"
"\n"
"#cancel_btn:pressed\n"
"{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.cancel_btn)


        self.verticalLayout_3.addWidget(self.progress_frame)


        self.verticalLayout_2.addWidget(self.main_frame)


        self.verticalLayout.addWidget(self.StyleSheet)


        self.retranslateUi(progressDialog)

        QMetaObject.connectSlotsByName(progressDialog)
    # setupUi

    def retranslateUi(self, progressDialog):
        progressDialog.setWindowTitle(QCoreApplication.translate("progressDialog", u"Edit User", None))
        self.title_lbl.setText(QCoreApplication.translate("progressDialog", u"title", None))
        self.dots_label.setText(QCoreApplication.translate("progressDialog", u"...", None))
        self.leftp_label.setText(QCoreApplication.translate("progressDialog", u"  (", None))
        self.progressbar_value_label.setText(QCoreApplication.translate("progressDialog", u"55", None))
        self.percent_rightp_label.setText(QCoreApplication.translate("progressDialog", u"% )", None))
        self.description_lbl.setText(QCoreApplication.translate("progressDialog", u"bla bla bla", None))
        self.complete_count_lbl.setText(QCoreApplication.translate("progressDialog", u"-", None))
        self.slash_label.setText(QCoreApplication.translate("progressDialog", u"/", None))
        self.total_count_lbl.setText(QCoreApplication.translate("progressDialog", u"-", None))
        self.progress_operetion_lbl.setText(QCoreApplication.translate("progressDialog", u"removed", None))
        self.cancel_btn.setText(QCoreApplication.translate("progressDialog", u"Cancel", None))
    # retranslateUi

