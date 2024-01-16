import sys
import time


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
from uiUtils.guiBackend import GUIBackend
from uiUtils.GUIComponents import SIDEBAR_BUTTON_SELECTED_STYLE, SIDEBAR_BUTTON_UNSELECTED_STYLE
from Constants import Constant
from Constants import IconsPath
from uiUtils.uiStyler import Styler

class mainUI(QMainWindow):

    """this class is used to build class for mainwindow to load GUI application

    :param QtWidgets: _description_

    """
    def __init__(self):
        """this function is used to laod ui file and build GUI application"""
        super(mainUI, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

        uiStyler = Styler(self.ui)
        uiStyler.render()

        self.Page_LiveView = LiveView_UI(self.ui)
        # self.Page_Report = Report_UI(self.ui)
        # self.Page_AlgorithmCalibration = AlgorithmCalibration_UI(self.ui)
        self.Page_Setting = Setting_UI(self.ui)
        self.Page_Users = usersPageUI(self.ui)
        self.common_func=Common_Function_UI()

        self.external_page_change_event = None
        self.move_refresh_time = 0

        self.pages = {
            'live': self.ui.live_view_page,
            'reports': self.ui.report_page,
            'settings': self.ui.settings_page,
            'users': self.ui.users_page,
            'about': self.ui.about_page
        }

        self.sidebar_pages_buttons = {
            'live': self.ui.side_live_view_btn,
            'reports': self.ui.side_report_btn,
            'settings': self.ui.side_settings_btn,
            'users': self.ui.side_users_btn,
            'about': self.ui.side_about_btn
        }

        self.tabs = {
            'users':(
                self.ui.user_tabs,
                {
                    'register': self.ui.user_register_tab,
                    'edit_profile':self.ui.user_profile_tab,
                    'all_users': self.ui.all_users_tab
                }
                ),
            
            'settings':(
                self.ui.settings_tabs,
                {
                    'camera': self.ui.camera_tab,
                    'algorithm': self.ui.algorithm_tab
                
                }
                )

        }

        self.buttons_connection()
        self.sidebar_button_connector()
        #self.laod_table_parms()
        
        self.current_page_name = ''
        self.previouse_page_name = ''

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = QtCore.QPoint(event.position().x(),event.position().y())
        else:
            super().mousePressEvent(event)


    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton and event.y() < self.ui.top_frame.height():
            if time.time() - self.move_refresh_time > Constant.RefreshRates.MOUSE_MOVE:
                self.move_refresh_time = time.time()
                self.move(self.pos() + QtCore.QPoint(event.scenePosition().x(),event.scenePosition().y()) - self.offset)

        else:
            super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
    

    def sidebar_button_connector(self):
        for page_name in self.sidebar_pages_buttons.keys():
            GUIBackend.button_connector( self.sidebar_pages_buttons[page_name], 
                                        self.sidebar_menu_handler(page_name) )
            
    
    def sidebar_menu_handler(self, new_page_name:str):
        """event happend when side bar menu button clicked

        Args:
            new_page_name (str): name of page that its button clicked
        """
        def func():
            self.previouse_page_name = self.current_page_name
            self.go_to_page(new_page_name)
            self.current_page_name = new_page_name

            if (self.current_page_name != self.previouse_page_name 
                and self.external_page_change_event is not None):
                self.internal_page_change_event()
            
        return func
    
    def sidebar_btns_style_handler(self, page_name):
        for page in self.sidebar_pages_buttons:
            if page_name==page:
                GUIBackend.set_style(self.sidebar_pages_buttons[page], SIDEBAR_BUTTON_SELECTED_STYLE)
            else:
                GUIBackend.set_style(self.sidebar_pages_buttons[page], SIDEBAR_BUTTON_UNSELECTED_STYLE)
    
    def go_to_page(self, page_name:str):
        """change page to the page with page_name
        """
        self.ui.main_stackedWidget.setCurrentWidget(self.pages[page_name])
        self.sidebar_btns_style_handler(page_name)


    def internal_page_change_event(self, ):
        """this function called when page change
        """
        self.external_page_change_event(self.previouse_page_name,
                                                self.current_page_name)
            
        
    def set_access_pages(self, pages:list[str], flag:bool = True):
        """enable or disable some pages

        Args:
            pages (list[str]): list of page names 
            flag (bool): if True, make pages enable. if False, make pages disable
        """
        if isinstance(pages, str):
            if pages == 'all':
                pages = list(self.sidebar_pages_buttons.keys())

        for page_name in self.sidebar_pages_buttons.keys():
            btn = self.sidebar_pages_buttons[page_name]
            if page_name in pages:
                GUIBackend.set_wgt_visible( btn, flag )
            else:
                GUIBackend.set_wgt_visible(btn , not(flag))
        
        self.go_to_page(pages[0])

    
    def set_access_tabs(self, tabs_access: dict[str,list], flag:bool = True):
        """enable or disable some tabs
        """
        for tabgropup_name in self.tabs.keys():
            tab_group_widget, sub_tabs = self.tabs[tabgropup_name]
            if tabgropup_name in tabs_access.keys():
                GUIBackend.set_wgt_visible(tab_group_widget, True)
                sub_tabs_access = tabs_access[tabgropup_name]

                if isinstance(sub_tabs_access, str):
                    if sub_tabs_access == 'all':
                        sub_tabs_access = list(sub_tabs.keys())
                    
                for sub_tab_name in sub_tabs.keys():
                    if sub_tab_name in sub_tabs_access:
                        GUIBackend.set_visible_tab(tab_group_widget,
                                                       sub_tabs[sub_tab_name],True )
                    else:
                        GUIBackend.set_visible_tab(tab_group_widget,
                                                       sub_tabs[sub_tab_name],False )
            else:
                GUIBackend.set_wgt_visible(tab_group_widget, False)


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

    def buttons_connection(self):
        """main butoons connect -- exit , minize , maximize, help --"""
        self.ui.close_btn.clicked.connect(self.close_win)
        self.ui.minimize_btn.clicked.connect(self.minimize)
        self.ui.maximize_btn.clicked.connect(self.maxmize_minimize)
        self.ui.menu_btn.clicked.connect(self.move_side_frame)

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

    def move_side_frame(self):
        w = self.ui.side_frame.width()

        if w <= Constant.SideBarAnimation.WIDTH_START_VALUE:
            self.minWidth = QtCore.QPropertyAnimation(self.ui.side_frame, b"minimumWidth")
            self.minWidth.setDuration(Constant.SideBarAnimation.ANIMATION_DURATION)
            self.minWidth.setStartValue(w)
            self.minWidth.setEndValue(Constant.SideBarAnimation.WIDTH_STOP_VALUE)
            self.minWidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.group = QtCore.QParallelAnimationGroup()
            self.group.addAnimation(self.minWidth)

            self.maxWidth = QtCore.QPropertyAnimation(self.ui.side_frame, b"maximumWidth")
            self.maxWidth.setDuration(Constant.SideBarAnimation.ANIMATION_DURATION)
            self.maxWidth.setStartValue(w)
            self.maxWidth.setEndValue(Constant.SideBarAnimation.WIDTH_STOP_VALUE)
            self.maxWidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.group.addAnimation(self.maxWidth)
            self.group.start()

            GUIBackend.set_button_icon(self.ui.menu_btn, IconsPath.IconsPath.OPEN_MENU_ICON)

        else:
            self.minWidth = QtCore.QPropertyAnimation(self.ui.side_frame, b"minimumWidth")
            self.minWidth.setDuration(Constant.SideBarAnimation.ANIMATION_DURATION)
            self.minWidth.setStartValue(w)
            self.minWidth.setEndValue(Constant.SideBarAnimation.WIDTH_START_VALUE)
            self.minWidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.group = QtCore.QParallelAnimationGroup()
            self.group.addAnimation(self.minWidth)

            self.maxWidth = QtCore.QPropertyAnimation(self.ui.side_frame, b"maximumWidth")
            self.maxWidth.setDuration(Constant.SideBarAnimation.ANIMATION_DURATION)
            self.maxWidth.setStartValue(w)
            self.maxWidth.setEndValue(Constant.SideBarAnimation.WIDTH_START_VALUE)
            self.maxWidth.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.group.addAnimation(self.maxWidth)
            self.group.start()

            GUIBackend.set_button_icon(self.ui.menu_btn, IconsPath.IconsPath.CLOSE_MENU_ICON)


