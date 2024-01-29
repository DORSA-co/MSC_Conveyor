from persiantools import jdatetime

from UIFiles.main_UI import Ui_MainWindow
from .Common_Function_UI import Common_Function_UI
from uiUtils.guiBackend import GUIBackend
from uiUtils.GUIComponents import deleteButton

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
        
        self.buttons = {
            'apply': self.ui.report_filter_apply_btn
        }
        
        self.table_widget_func = None

    def startup(self,):
        GUIBackend.set_table_cheaders(self.ui.report_table, self.TABLE_HEADERS)
        
    def button_connector(self, name, func):
        self.buttons[name].clicked.connect(func)

    def get_filters(self):
        """Get all filters in report page."""
        filters = {}
        for key in self.filters['ranges'].keys():
            if GUIBackend.get_checkbox_value(self.filter_checkboxes[key]):
                start_range = GUIBackend.get_input(self.filters['ranges'][key][0])
                end_range = GUIBackend.get_input(self.filters['ranges'][key][1])
                filters[key] = (start_range, end_range)
        
        return filters
    
    def show_filter_results(self, results: list[dict]):
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
                    GUIBackend.set_table_cell_value(self.ui.report_table, (i, j), value='{}'.format(i+1))

                elif header == 'delete':
                    delete_btn = deleteButton()
                    GUIBackend.button_connector_argument_pass(delete_btn, self.table_widget_func, (result, 'delete'))
                    GUIBackend.set_table_cell_widget(self.ui.report_table, (i, j), delete_btn)

    
    def table_widget_connector(self, func):
        self.table_widget_func = func

