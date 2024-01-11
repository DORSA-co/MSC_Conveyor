from UIFiles.main_UI import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6 import QtGui

class Styler:

    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui

        self.shadows_obj: dict[QtWidgets.QWidget] = {
            'save':
                {   
                    'style': {'blur_radius':15,
                              'offset':(3,3),
                              'color':(0,0,0,100),
                              },
                    'objects':[ self.ui.save_camera_settings,
                                self.ui.save_algorithm_settings,
                                ]
                },

            'steps':
                {   
                    'style': {'blur_radius':5,
                              'offset':(0,0),
                              'color':(0,0,0,200),
                              },
                    'objects':[ self.ui.step1_btn,
                                self.ui.step2_btn,
                                self.ui.step3_btn,
                                ]
                },

            
            'frame':
                {   
                    'style': {'blur_radius':10,
                              'offset':(0,0),
                              'color':(0,0,0,50),
                              },
                    'objects':[ self.ui.step1_settings_frame,
                                self.ui.step2_settings_frame,
                                self.ui.step3_settings_frame,

                                self.ui.camera_settings_frame,
                                ]
                },


            # 'groupbox':
            #     {   
            #         'style': {'blur_radius':20,
            #                   'offset':(5,5),
            #                   'color':(0,0,0,50),
            #                   },
            #         'objects':[ self.ui.userpage_editprofile_edit_profile_groupbox,
            #                     self.ui.userpage_editprofile_change_pass_groupbox,
            #                     ]
            #     },

        }

    def render(self,):
        self.__set_shadow()

    
    def __set_shadow(self, ):
        for group_name,group in self.shadows_obj.items():
            style = group['style']
            objects:list[QtWidgets.QWidget] = group['objects']
            for obj in objects:
                shadow  = QtWidgets.QGraphicsDropShadowEffect(obj)
                shadow.setBlurRadius(style['blur_radius'])
                shadow.setOffset(*style['offset'])
                shadow.setColor(QtGui.QColor(*style['color']))
                obj.setGraphicsEffect(shadow)