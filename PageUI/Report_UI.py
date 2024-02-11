from persiantools import jdatetime
import math

from UIFiles.main_UI import Ui_MainWindow
from .Common_Function_UI import Common_Function_UI
from uiUtils.guiBackend import GUIBackend
from uiUtils.GUIComponents import deleteButton, viewButton, pageNavigationButton, tabelCheckbox
from uiUtils.GUIComponents import singleAnimation, proggressDialogUI
from Constants.Constant import ReportFiltersAnimation, ReportTableLimit

class Report_UI(Common_Function_UI):

    """Description of the code
    :param
    """

    def __init__(self, ui: Ui_MainWindow):
        """Description of the code"""

        self.ui = ui
        self.deleteProgressDialog = proggressDialogUI()        
        self.deleteProgressDialog.setup('Remove','', operation_name='removed')

        self.TABLE_HEADERS = [
                        ' ',
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
        
        self.TABLE_HEADERS_UNITS = [
            '',
            '',
            '',
            '',
            '',
            '',
            ' (cm)',
            ' (cm)',
            ' (cm)',
            ' (m)',
            ' (mm)',
            ' (mm)',
            ' (mm)',
            '',
            ''
        ]

        self.TABLE_COLLUMN_WIDTH = [
                        50,
                        50,
                        150,
                        150,
                        150,
                        150, 
                        150,
                        150,
                        150,
                        150, 
                        150, 
                        150, 
                        150,
                        100,
                        100
                    ]
        
        self.filters = {
            'ranges': {'date': (self.ui.report_start_date_input, self.ui.report_end_date_input),
                       'width': (self.ui.report_low_width_input, self.ui.report_high_width_input),
                       'length': (self.ui.report_low_length_input, self.ui.report_high_length_input), 
                       'depth': (self.ui.report_low_depth_input, self.ui.report_high_depth_input)
            },
            'booleans': {'torn': self.ui.report_torn_checkBox
            }
        }

        self.filter_checkboxes = {
            'date': self.ui.report_date_checkBox,
            'class': self.ui.report_class_checkBox,
            'width': self.ui.report_width_checkBox,
            'length': self.ui.report_length_checkBox,
            'depth': self.ui.report_depth_checkBox,
            'torn': self.ui.report_torn_checkBox,
        }

        self.filter_frames = {
            'date': self.ui.report_date_filter_frame,
            'class': self.ui.report_class_filter_frame,
            'width': self.ui.report_width_filter_frame,
            'length': self.ui.report_length_filter_frame,
            'depth': self.ui.report_depth_filter_frame,
            'torn': self.ui.report_torn_filter_frame,
        }
        
        self.buttons = {
            'apply': self.ui.report_filter_apply_btn,
            'next': self.ui.report_next_btn,
            'prev': self.ui.report_prev_btn,
            'delete_all': self.ui.delete_selected_defects,
            'reload': self.ui.reload_reports_btn,
            'move_table_hscroll_end': self.ui.move_table_end_btn,
            'move_table_hscroll_start': self.ui.move_table_start_btn
        }

        
        self.table_widget_func = None
        self.pages_number_navigation_button:dict[int,pageNavigationButton] = {}
        self.filter_animation:dict[str,singleAnimation] = {}


        for name in self.filter_frames:
            GUIBackend.checkbox_connector_argument_pass(self.filter_checkboxes[name],
                                                   self.slide_filter,
                                                   (name, )
                                                   )
        
        self.__filter_animation_builder()

        self.button_connector('next', self.table_next_page)
        self.button_connector('prev', self.table_previous_page)
        self.button_connector('move_table_hscroll_start', self.__set_table_scrollbar_to_start)
        self.button_connector('move_table_hscroll_end', self.__set_table_scrollbar_to_end)

        GUIBackend.checkbox_connector(self.ui.select_all_defects_table, self.select_all)

        self.table_current_page = 1
        self.table_total_pages = 0
        self.table_total_contents = []
        self.selected_table_contents = []
        self.handle_next_prev_enablity()

    def startup(self,):
        self.__set_table_scrollbar_to_start()
        GUIBackend.set_table_cheaders(self.ui.report_table, 
                                      [self.TABLE_HEADERS[i]+self.TABLE_HEADERS_UNITS[i] for i in range(len(self.TABLE_HEADERS))]
                                    )
        for c, width in enumerate(self.TABLE_COLLUMN_WIDTH):
            GUIBackend.set_table_cwidth(self.ui.report_table, c, width)
        
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

        for key in self.filters['booleans'].keys():
            if GUIBackend.get_checkbox_value(self.filter_checkboxes[key]):
                value = GUIBackend.get_checkbox_value(self.filters['booleans'][key])
                filters[key] = value
        
        return filters
    
    def table_next_page(self):
        #self.table_current_page += 1
        self.table_page_event(self.table_current_page + 1)
        self.handle_next_prev_enablity()
        self.set_table_contents()

    def table_previous_page(self):
        #self.table_current_page -= 1
        self.table_page_event(self.table_current_page - 1)
        self.handle_next_prev_enablity()
        self.set_table_contents()
        

    def handle_next_prev_enablity(self):
        GUIBackend.set_disable_enable(self.buttons['next'], not(self.table_current_page == self.table_total_pages or self.table_total_pages==0))
        GUIBackend.set_disable_enable(self.buttons['prev'], not(self.table_current_page == 1 or self.table_total_pages==0))

    def show_filter_results(self, results: list[dict]):
        self.table_total_contents = results
        for record in  self.selected_table_contents:
            if record not in results:
                self.selected_table_contents.remove(record)

        self.table_current_page = 1
        self.table_total_pages = math.ceil(len(self.table_total_contents)/ReportTableLimit.REPORT_TABLE_LIMIT)
        self.table_total_pages = max(self.table_total_pages, 1)
        self.setup_page_navigation_buttons(1, self.table_total_pages, self.table_page_event)
        self.handle_next_prev_enablity()
        # self.handle_page_numbers_enablity()
        self.set_table_contents()
    
    def set_table_contents(self):
        table_page_start_idx = ReportTableLimit.REPORT_TABLE_LIMIT*(self.table_current_page-1)
        table_page_end_idx = min(ReportTableLimit.REPORT_TABLE_LIMIT*(self.table_current_page), 
                                 len(self.table_total_contents)
                                 )

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
                
                elif header == ' ':
                    checkbox = tabelCheckbox()
                    GUIBackend.set_table_cell_widget(self.ui.report_table, (i, j), checkbox, layout=True)
                    GUIBackend.checkbox_connector_argument_pass(checkbox, 
                                                                self.checked_table_record, 
                                                                (result,))
                    
                    if result in self.selected_table_contents:
                        GUIBackend.set_checkbox_value(checkbox, True, block_signal=True)
                    
                    #self.table_checkboxes[result['defect_id']] = checkbox

                elif header == 'NO.':
                    GUIBackend.set_table_cell_value(self.ui.report_table, 
                                                    (i, j), 
                                                    value='{}'.format(i+1+table_page_start_idx))
                    

                elif header == 'delete':
                    delete_btn = deleteButton()
                    GUIBackend.button_connector_argument_pass(delete_btn, 
                                                              self.table_widget_func, 
                                                              (result, 'delete'))
                    
                    GUIBackend.set_table_cell_widget(self.ui.report_table, 
                                                     (i, j), 
                                                     delete_btn)

                elif header == 'view':
                    view_btn = viewButton()
                    GUIBackend.button_connector_argument_pass(view_btn, self.table_widget_func, (result, 'view'))
                    GUIBackend.set_table_cell_widget(self.ui.report_table, (i, j), view_btn)

    
    def table_widget_connector(self, func):
        self.table_widget_func = func
    
    def setup_page_navigation_buttons(self, start, end, event_func):
        self.__clear_pages_navigation_buttons()
        layout = self.ui.pages_navigation_frame.layout()

        for number in range(start, end+1):
            btn = pageNavigationButton(number=number)
            GUIBackend.button_connector_argument_pass(btn, event_func, (number,))
            self.pages_number_navigation_button[number] = btn
            layout.addWidget(btn)
        
        first_page = self.pages_number_navigation_button.get(start)
        if first_page is not None:
            first_page.set_selected(True)

    def table_page_event(self, number:int):
        self.pages_number_navigation_button[self.table_current_page].set_selected(False)
        self.table_current_page = number
        self.pages_number_navigation_button[self.table_current_page].set_selected(True)
        self.handle_next_prev_enablity()
        self.set_table_contents()

    def checked_table_record(self,state, record):
        if state:
            self.selected_table_contents.append(record)
        else:
            self.selected_table_contents.remove(record)

    def select_all(self, state):
        state = GUIBackend.get_checkbox_value(self.ui.select_all_defects_table)
        if state:
            self.selected_table_contents = self.table_total_contents.copy()
        else:
            self.selected_table_contents = []
        self.set_table_contents()
    
    def get_selected_defects(self,):
        return self.selected_table_contents
        

    def __clear_pages_navigation_buttons(self):
        for btn in self.pages_number_navigation_button.values():
            btn.deleteLater()
        self.pages_number_navigation_button = {}
        

    def slide_filter(self,state, name):
        if state:
            self.__slide_filter_in(name)
        else:
            self.__slide_filter_out(name)


    def __filter_animation_builder(self,):
        for name in self.filter_frames.keys():
            self.filter_animation[name] = singleAnimation(self.filter_frames[name],
                                               b'maximumHeight',
                                               ReportFiltersAnimation.ANIMATION_DURATION,
                                               ReportFiltersAnimation.HEIGHT_START_VALUE,
                                               ReportFiltersAnimation.HEIGHT_STOP_VALUE,
                                               )
            self.filter_animation[name].reset()
    
    def __slide_filter_in(self, name):
        self.filter_animation[name].forward()
        
    def __slide_filter_out(self, name):
        self.filter_animation[name].backward()

    def __set_table_scrollbar_to_start(self):
        self.ui.report_table.horizontalScrollBar().setValue(0)
        GUIBackend.set_disable_enable(self.buttons['move_table_hscroll_start'], False)
        GUIBackend.set_disable_enable(self.buttons['move_table_hscroll_end'], True)

    def __set_table_scrollbar_to_end(self):
        x = self.ui.report_table.horizontalScrollBar().maximum()
        self.ui.report_table.horizontalScrollBar().setValue(x)

        GUIBackend.set_disable_enable(self.buttons['move_table_hscroll_start'], True)
        GUIBackend.set_disable_enable(self.buttons['move_table_hscroll_end'], False)

