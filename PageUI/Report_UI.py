from persiantools import jdatetime
import math

from UIFiles.main_UI import Ui_MainWindow
from .Common_Function_UI import Common_Function_UI
from uiUtils.guiBackend import GUIBackend
from uiUtils.GUIComponents import deleteButton, viewButton
from uiUtils.GUIComponents import singleAnimation
from Constants.Constant import ReportFiltersAnimation, ReportTableLimit

class Report_UI(Common_Function_UI):

    """Description of the code
    :param
    """

    def __init__(self, ui: Ui_MainWindow):
        """Description of the code"""

        self.ui = ui

        self.TABLE_HEADERS = [
                        'NO.',
                        'date',
                        'time',
                        'x',
                        'y', 
                        'min_width',
                        'mean_width',
                        'max_width',
                        'length', 
                        'min_depth', 
                        'mean_depth', 
                        'max_depth',
                        'delete',
                        'view'
                    ]
        
        self.filters = {
            'ranges': {'date': (self.ui.report_start_date_input, self.ui.report_end_date_input),
                       'width': (self.ui.report_low_width_input, self.ui.report_high_width_input),
                       'length': (self.ui.report_low_length_input, self.ui.report_high_length_input), 
                       'depth': (self.ui.report_low_depth_input, self.ui.report_high_depth_input)
            }
        }

        self.filter_checkboxes = {
            'date': self.ui.report_date_checkBox,
            # 'class': self.ui.report_class_checkBox,
            'width': self.ui.report_width_checkBox,
            'length': self.ui.report_length_checkBox,
            'depth': self.ui.report_depth_checkBox,
        }

        self.filter_frames = {
            'date': self.ui.report_date_filter_frame,
            # 'class': self.ui.report_class_filter_frame,
            'width': self.ui.report_width_filter_frame,
            'length': self.ui.report_length_filter_frame,
            'depth': self.ui.report_depth_filter_frame,
        }
        
        self.buttons = {
            'apply': self.ui.report_filter_apply_btn,
            'next': self.ui.report_next_btn,
            'prev': self.ui.report_prev_btn,
            'first_page': self.ui.report_first_page_btn,
            'second_page': self.ui.report_second_page_btn,
            'third_page': self.ui.report_third_page_btn,
        }

        
        self.table_widget_func = None


        for name in self.filter_frames:
            GUIBackend.checkbox_connector_with_arg(self.filter_checkboxes[name],
                                                   self.slide_filter,
                                                   (name, )
                                                   )
            

        self.button_connector('next', self.table_next_page)
        self.button_connector('prev', self.table_previous_page)
        # self.button_connector('first', self.table_previous_page)
        # self.button_connector('prev', self.table_previous_page)
        # self.button_connector('prev', self.table_previous_page)


        self.table_current_page = 1
        self.table_total_pages = 0
        self.table_total_contents = []
        self.handle_next_prev_enablity()

    def startup(self,):
        GUIBackend.set_table_cheaders(self.ui.report_table, self.TABLE_HEADERS)
        
    def button_connector(self, name, func):
        GUIBackend.button_connector(self.buttons[name], func)

    def get_filters(self):
        """Get all filters in report page."""
        filters = {}
        for key in self.filters['ranges'].keys():
            if GUIBackend.get_checkbox_value(self.filter_checkboxes[key]):
                start_range = GUIBackend.get_input(self.filters['ranges'][key][0])
                end_range = GUIBackend.get_input(self.filters['ranges'][key][1])
                filters[key] = (start_range, end_range)
        
        return filters
    
    def table_next_page(self):
        self.table_current_page += 1
        self.handle_next_prev_enablity()
        self.set_table_contents()

    def table_previous_page(self):
        self.table_current_page -= 1
        self.handle_next_prev_enablity()
        self.set_table_contents()

    def handle_next_prev_enablity(self):
        GUIBackend.set_disable_enable(self.buttons['next'], not(self.table_current_page == self.table_total_pages or self.table_total_pages==0))
        GUIBackend.set_disable_enable(self.buttons['prev'], not(self.table_current_page == 1 or self.table_total_pages==0))

    def show_filter_results(self, results: list[dict]):
        self.table_total_contents = results
        self.table_current_page = 1
        self.table_total_pages = math.ceil(len(self.table_total_contents)/ReportTableLimit.REPORT_TABLE_LIMIT)
        self.handle_next_prev_enablity()
        # self.handle_page_numbers_enablity()
        self.set_table_contents()
    
    def set_table_contents(self):
        table_page_start_idx = ReportTableLimit.REPORT_TABLE_LIMIT*(self.table_current_page-1)
        table_page_end_idx = min(ReportTableLimit.REPORT_TABLE_LIMIT*(self.table_current_page), len(self.table_total_contents))

        results = self.table_total_contents[table_page_start_idx:table_page_end_idx]
        GUIBackend.set_table_dim(self.ui.report_table, len(results), len(self.TABLE_HEADERS))
        for i, result in enumerate(results):
            for j, header in enumerate(self.TABLE_HEADERS):
                value = result.get(header, None)

                if value is not None:
                    if header == 'date':
                        value = value.strftime('%Y/%m/%d')
                    if  header == 'time':
                        value = value.strftime('%H:%M:%S')

                if value is not None:
                    GUIBackend.set_table_cell_value(self.ui.report_table, (i, j), value=value)

                elif header == 'NO.':
                    GUIBackend.set_table_cell_value(self.ui.report_table, (i, j), value='{}'.format(i+1+table_page_start_idx))

                elif header == 'delete':
                    delete_btn = deleteButton()
                    GUIBackend.button_connector_argument_pass(delete_btn, self.table_widget_func, (result, 'delete'))
                    GUIBackend.set_table_cell_widget(self.ui.report_table, (i, j), delete_btn)

                elif header == 'view':
                    view_btn = viewButton()
                    GUIBackend.button_connector_argument_pass(view_btn, self.table_widget_func, (result, 'view'))
                    GUIBackend.set_table_cell_widget(self.ui.report_table, (i, j), view_btn)

    
    def table_widget_connector(self, func):
        self.table_widget_func = func

    def slide_filter(self, name):
        if GUIBackend.get_checkbox_value(self.filter_checkboxes[name]):
            self.__slide_filter_in(name)
        else:
            self.__slide_filter_out(name)

    def __filter_animation_builder(self, name):
        self.filter_animation = singleAnimation(self.filter_frames[name],
                                               b'maximumHeight',
                                               ReportFiltersAnimation.ANIMATION_DURATION,
                                               ReportFiltersAnimation.HEIGHT_START_VALUE,
                                               ReportFiltersAnimation.HEIGHT_STOP_VALUE
                                               )
    
    def __slide_filter_in(self, name):
        self.__filter_animation_builder(name)
        self.filter_animation.forward()
        
    def __slide_filter_out(self, name):
        self.__filter_animation_builder(name)
        self.filter_animation.backward()