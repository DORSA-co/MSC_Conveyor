from uiUtils.guiBackend import GUIBackend
#from UIFiles.edit_user_ui import 




class loginUserDialog:
    ui_path = 'UIFiles\\login.ui'
    
    def __init__(self) -> None:
        self.ui = GUIBackend.load_ui(self.ui_path)

        GUIBackend.set_input_password(self.ui.password_input)
        GUIBackend.set_win_frameless(self.ui)
        GUIBackend.button_connector(self.ui.close_btn, self.close)

    
    def close(self,):
        self.ui.close()
        self.clear_inputs()


    def login_button_connector(self, func):
        GUIBackend.button_connector(self.ui.login_btn, func)

    #def register_button_connector(self, func):
    #    GUIBackend.button_connector(self.ui.register_btn, func)

    def show(self):
        self.write_error(None)
        GUIBackend.show_window(self.ui, always_on_top=True)

    def close(self):
        GUIBackend.close_window(self.ui)


    def get_inputs(self):
        username = GUIBackend.get_input(self.ui.username_input)
        password = GUIBackend.get_input(self.ui.password_input)
        return {'username':username.lower(), 'password':password}

    def clear_inputs(self):
        GUIBackend.set_input(self.ui.username_input, "")
        GUIBackend.set_input(self.ui.password_input, "")

    def write_error(self, txt:str):
        """Write Errors message in Logun

        Args:
            txt (str): error message
        """
        if txt is None:
            GUIBackend.set_wgt_visible(self.ui.login_error_lbl, False)
        else:
            GUIBackend.set_wgt_visible(self.ui.login_error_lbl, True)
            GUIBackend.set_label_text( self.ui.login_error_lbl, txt)




            

