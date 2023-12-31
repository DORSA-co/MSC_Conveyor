from uiUtils.guiBackend import GUIBackend
import os
#from UIFiles.edit_user_ui import 


class editUserDialog:
    ui_path = os.path.join('UIFiles', 'edit_user.ui')
    
    def __init__(self) -> None:
        self.ui = GUIBackend.load_ui(self.ui_path)


        self.fields = {
            'username': self.ui.username_input, 
            'password': self.ui.password_input,
            'role': self.ui.role_combobox,
        }

        GUIBackend.set_win_frameless(self.ui)
        GUIBackend.button_connector(self.ui.cancel_btn, self.close)

    def save_button_connector(self, func):
        GUIBackend.button_connector(self.ui.save_btn, func)

    def set_inputs(self, user):
        for field_name, field in self.fields.items():
            GUIBackend.set_input( field, user[field_name])

    def get_inputs(self):
        user_info = {}
        for field_name, field in self.fields.items():
            user_info[field_name] = GUIBackend.get_input( field, )
        return user_info
    
    def set_role_items(self, roles:list[str]):
        GUIBackend.set_combobox_items(self.ui.role_combobox, roles)


    def write_edit_user_error(self, txt:str):
        """Write Errors message in change password

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.ui.error_lbl, True)
            GUIBackend.set_label_text(self.ui.error_lbl, txt)
    
    def close(self,):
        GUIBackend.close_window(self.ui)
        for field_name, field in self.fields.items():
            GUIBackend.set_input( field, "")

    def show(self,user:dict):
        self.set_inputs(user)
        self.write_edit_user_error(None)
        GUIBackend.show_window(self.ui, True)
        
        