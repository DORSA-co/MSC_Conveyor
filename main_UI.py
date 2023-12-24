import sys



from PySide6.QtWidgets import QMainWindow, QHeaderView
from PySide6 import QtCore
from PageUI.LiveView_UI import LiveView_UI
from PageUI.Report_UI import Report_UI
from PageUI.Setting_UI import Setting_UI
from PageUI.users_UI import usersPageUI
from PageUI.AlgorithmCalibration_UI import AlgorithmCalibration_UI
from PageUI.Common_Function_UI import Common_Function_UI 
from UIFiles.assets import assets_rc
from UIFiles.main_UI import Ui_MainWindow

MAIN_UI_PATH = "UIFiles/main_UI.ui"

class mainUI(QMainWindow):

    """this class is used to build class for mainwindow to load GUI application

    :param QtWidgets: _description_

    """
    def __init__(self):
        """this function is used to laod ui file and build GUI application"""
        super(mainUI,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

        self.Page_LiveView = LiveView_UI(self.ui)
        self.Page_Report = Report_UI(self.ui)
        self.Page_AlgorithmCalibration = AlgorithmCalibration_UI(self.ui)
        self.Page_Setting = Setting_UI(self.ui)
        self.Page_Users = usersPageUI(self.ui)
        self.common_func=Common_Function_UI()

        self.external_page_change_event = None

        self.pages = {
            'live': self.ui.Live_View_Page,
            'help': self.ui.Help_page,
            'reports': self.ui.Report_page,
            'settings': self.ui.Setting_Page,
            'users': self.ui.Users_page
        }

        self.buttons_connection()
        #self.laod_table_parms()
        
        self.current_page_name = ''
        self.previouse_page_name = ''
        


    def laod_table_parms(self):
        #self.tableWidget.verticalHeader().setStretchLastSection(True)
        header = self.ui.tableWidget.horizontalHeader()
        self.ui.tableWidget.horizontalHeaderVisible = True
        #header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Stretch)
        header.setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.ui.tableWidget.setColumnWidth(0, 60)  

    def change_page_connector(self, func):
        self.external_page_change_event = func

    def load_page(self, name):
        self.previouse_page_name = self.current_page_name
        self.ui.pages_stackwgt.setCurrentWidget(self.pages[name])
        self.current_page_name = name
        if self.external_page_change_event is not None:
            self.external_page_change_event(self.previouse_page_name,
                                            self.current_page_name)

    def buttons_connection(self):
        """main butoons connect -- exit , minize , maximize, help --"""
        self.ui.close_btn.clicked.connect(self.close_win)
        self.ui.minimize_btn.clicked.connect(self.minimize)
        self.ui.maximize_btn.clicked.connect(self.maxmize_minimize)
        self.ui.LiveDetectionBT.clicked.connect(lambda : self.load_page('live'))
        self.ui.HelpConnectionBT.clicked.connect(lambda :self.load_page('help'))
        self.ui.ReportConnectionBT.clicked.connect(lambda :self.load_page('reports'))
        self.ui.SettingBT.clicked.connect(lambda :self.load_page('settings'))
        self.ui.usersBtn.clicked.connect(lambda :self.load_page('users'))

    def minimize(self):
        """Minimize winodw"""
        self.showMinimized()

    def close_win(self):
        """
        this function closes the app
        Inputs: None
        Returns: None
        """

        res = self.common_func.show_alert_window(
            title="Exit",
            message="Do you want to exit?",
            need_confirm=True,
            level=1,
        )

        if res:
            self.app_close_flag = True
            self.close()
            sys.exit()

    def maxmize_minimize(self):
        """Maximize or Minimize window"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


