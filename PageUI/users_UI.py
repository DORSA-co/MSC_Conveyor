from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents
from Constants import IconsPath
from Constants import Constant

from PageUI.Common_Function_UI import Common_Function_UI
from UIFiles.main_UI import Ui_MainWindow
from PageUI.DialogWindows.editUserDialog import editUserDialog
from PageUI.DialogWindows.loginUserDialog import loginUserDialog

class usersPageUI:
    def __init__(self, ui:Ui_MainWindow):
        #self.login_ui = login_ui
        self.registerTab = RegisterUserTabUI(ui)
        self.allUserTab = AllUserTabUI(ui)
        self.editUserTab = EditUserTabUI(ui)
        self.LoginUser = LoginUserUI(ui)

class RegisterUserTabUI(Common_Function_UI):
    
    def __init__(self, ui:Ui_MainWindow) -> None:
        super(RegisterUserTabUI,self).__init__()

        self.ui = ui

        self.register_users_field = {
            'username' : self.ui.userpage_username_inpt,
            'password' : self.ui.userpage_password_inpt,
            'password_confirm': self.ui.userpage_confirm_password_inpt,
            'role': self.ui.userpage_user_role_combobox
        }

        self.register_eye_buttons = {
            'password': self.ui.userpage_password_eye,
            'password_confirm': self.ui.userpage_confirm_password_eye
        }

        self.register_eye_flags = {
            'password': False,
            'password_confirm': False
        }

        
        #set input type as password to show password as *
        for name in ['password', 'password_confirm']:
            GUIBackend.set_input_password(self.register_users_field[name])
            self.eye_buttons_connector(name)
        
        # self.show_success_msg(None)
        self.reset()

    def eye_buttons_connector(self, name):
        self.register_eye_buttons[name].clicked.connect(lambda: self.show_hide_password(name))

    def show_hide_password(self, name):
        self.register_eye_flags[name] = not self.register_eye_flags[name]
        if self.register_eye_flags[name]:
            GUIBackend.set_input_normal(self.register_users_field[name])
            GUIBackend.set_button_icon(self.register_eye_buttons[name], IconsPath.IconsPath.BLACK_HIDE_PASSWORD)
        else:
            GUIBackend.set_input_password(self.register_users_field[name])
            GUIBackend.set_button_icon(self.register_eye_buttons[name], IconsPath.IconsPath.BLACK_SHOW_PASSWORD)

    def reset(self):
        """reset ui to default
        """
        self.set_register_fields( {
            'username' : "",
            'password' : "",
            'password_confirm': "",
        })
        # self.write_register_error(None)

    
    def set_user_roles_items(self, items: list[str]):
        GUIBackend.set_combobox_items(self.register_users_field['role'], items)

    def register_button_connector(self, func):
        """connect function into register button clicked event
        """
        GUIBackend.button_connector(self.ui.register_user, func)
    
    def get_register_fields(self)-> dict:
        """returns register fields in dictionary type

        Returns:
            dict: infos in format {
            'username':xxxx,
            'password':xxxx,
            'password_confirm':xxxx,
            'role':xxxx,}
        """
        infos = {}
        for name, field in self.register_users_field.items():
            infos[name] = GUIBackend.get_input(field)
        
        infos['username'] = infos['username'].lower()
        return infos
    

    def set_register_fields(self, data:dict):
        """set register fields

        data (dict):
            input datas informat like {
                'username':xxxx,
                'password':xxxx,
                'password_confirm':xxxx,
        """
        for name, value in data.items():
            GUIBackend.set_input(self.register_users_field[name], value)
        
    
    
    def write_register_error(self, txt:str):
        """Write Errors message in Register

        Args:
            txt (str): error message
        """
        message = GUIComponents.ErrorMessage(parent=self.ui.register_message_frame, text=txt)
        message.show_message()

    def show_success_msg(self, txt):
        message = GUIComponents.SuccessMessage(parent=self.ui.register_message_frame, text=txt)
        message.show_message()

class AllUserTabUI(Common_Function_UI):

    def __init__(self, ui:Ui_MainWindow) -> None:
        super(AllUserTabUI,self).__init__()

        self.ui = ui
        self.editUserDialog = editUserDialog()

        self.users_table = self.ui.userpage_all_users_table
        self.__table_external_event_function__ = None

        

        self.users_table_headers = ['id', 'username', 'password', 'role', 'edit', 'delete']
        GUIBackend.set_table_dim(self.users_table, row=10, col=len(self.users_table_headers))
        GUIBackend.set_table_cheaders(self.users_table, self.users_table_headers)


    def table_external_event_connector(self, func):
        """connect edit and delete button of each record in users tabel to a function

        Args:
            func (_type_): function should have foure arguments,  ( row idx, user info dic, 'edit' or 'delete' flag, button )
        """
        self.__table_external_event_function__ = func
    

    def set_users_table(self,users:list[dict]):
        """insert users info into table
        Args:
            datas (list[list]): list of users info
        """
        
        assert self.__table_external_event_function__ is not None, "ERROR: First determine an event Function for edit and delete button by 'AllUserTab.__table_event_connector__' method "
        
        #set row count
        users_count = len(users)
        GUIBackend.set_table_dim(self.users_table, row=users_count, col=None)

        if users_count == 0:
            return
        
        info_count = len(users[0])

        for row, user in enumerate(users):
            for info_name in user.keys():
                col = self.users_table_headers.index(info_name)
                value = user[info_name]
                if info_name == 'password':
                    value = '•'*8
                GUIBackend.set_table_cell_value(self.users_table, (row, col), value=value)

            #define edit and delete button
            edit_btn = GUIComponents.editButton()
            del_btn = GUIComponents.deleteButton()

            #connect buttons to event function 
            GUIBackend.button_connector_argument_pass( edit_btn, self.__table_external_event_function__, args=(row, user, 'edit',  edit_btn) )
            GUIBackend.button_connector_argument_pass( del_btn, self.__table_external_event_function__, args = (row, user, 'delete',  del_btn ) )

            #insert buttons into table
            GUIBackend.set_table_cell_widget(self.users_table, (row, info_count), edit_btn)

            # if user['id'] != 1:
            #     #we shouldn't remove main user
            GUIBackend.set_table_cell_widget(self.users_table, (row, info_count+1), del_btn)

            if user['id'] == 1:
                GUIBackend.set_disable_enable(del_btn, status=False)

class EditUserTabUI:

    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui

        self.buttons = {
            'change_username': self.ui.userpage_editprofile_change_username_btn,
            'change_password': self.ui.userpage_editprofile_change_password_btn
        }

        self.message_labels = {
            'change_password':self.ui.change_password_message_frame,
            'change_username':self.ui.change_username_message_frame
        }

        self.change_password_fields = {
            'old_password': self.ui.userpage_editprofile_old_password_inpt,
            'new_password': self.ui.userpage_editprofile_new_password_inpt,
            'confirm_new_password': self.ui.userpage_editprofile_confirm_new_password_inpt,
        }

        self.change_password_eye_buttons = {
            'old_password': self.ui.userpage_editprofile_old_password_eye,
            'new_password': self.ui.userpage_editprofile_new_password_eye,
            'confirm_new_password': self.ui.userpage_editprofile_confirm_new_password_eye,
        }

        self.change_password_eye_flags = {
            'old_password': False,
            'new_password': False,
            'confirm_new_password': False,
        }

        self.edit_profile_fields = {
            'username': self.ui.userpage_editprofile_username_inpt,
            'new_username': self.ui.userpage_editprofile_new_username_inpt,
        }

        
        for name in ['old_password', 'new_password', 'confirm_new_password']:
            GUIBackend.set_input_password(self.change_password_fields[name])
            self.eye_buttons_connector(name)
        

        # self.write_error('change_username', None)
        # self.write_error('change_password', None)
        # self.show_success_msg('change_username', None)
        # self.show_success_msg('change_password', None)


    def button_connector(self, name, func):
        GUIBackend.button_connector(self.buttons[name], func)

    def eye_buttons_connector(self, name):
        self.change_password_eye_buttons[name].clicked.connect(lambda: self.show_hide_password(name))

    def show_hide_password(self, name):
        self.change_password_eye_flags[name] = not self.change_password_eye_flags[name]
        if self.change_password_eye_flags[name]:
            GUIBackend.set_input_normal(self.change_password_fields[name])
            GUIBackend.set_button_icon(self.change_password_eye_buttons[name], IconsPath.IconsPath.BLACK_HIDE_PASSWORD)
        else:
            GUIBackend.set_input_password(self.change_password_fields[name])
            GUIBackend.set_button_icon(self.change_password_eye_buttons[name], IconsPath.IconsPath.BLACK_SHOW_PASSWORD)

    def get_change_password_fields(self,):
        data = {}
        for name, filed in self.change_password_fields.items():
            data[name] = GUIBackend.get_input(filed)

        return data
    
    def clear_change_password_fields(self,):
        for name, filed in self.change_password_fields.items():
            GUIBackend.set_input(filed, "")

    def get_edit_profile_fields(self,):
        data = {}
        for name, field in self.edit_profile_fields.items():
            data[name] = GUIBackend.get_input(field)
        
        data['username'] = data['new_username'].lower()
        data.pop('new_username')
        return data


    def set_edit_profile_fields(self, data:dict):
        for name, field in self.edit_profile_fields.items():
            GUIBackend.set_input(field, data.get(name, ""))

    def write_error(self, name:str, txt:str):
        """Write Errors message in change password

        Args:
            txt (str): error message
        """
        
        message = GUIComponents.ErrorMessage(parent=self.message_labels[name], text=txt)
        message.show_message()

    def show_success_msg(self, name: str, txt:str):
        message = GUIComponents.SuccessMessage(parent=self.message_labels[name], text=txt)
        message.show_message()

class LoginUserUI(Common_Function_UI):
    
    def __init__(self, ui:Ui_MainWindow) -> None:
        super(LoginUserUI,self).__init__()

        self.ui = ui
        self.loginDialog = loginUserDialog()


    def login_button_connector(self, func):
        GUIBackend.button_connector(self.ui.login_logout_btn, func)
    
    def set_logedin_username(self, username):
        if username is None:
            #GUIBackend.set_wgt_visible(self.logined_username_lbl, False)
            GUIBackend.set_label_text( self.ui.logined_username_lbl, 'Login')
        else:
            #GUIBackend.set_wgt_visible(self.logined_username_lbl, True)
            GUIBackend.set_label_text( self.ui.logined_username_lbl, username)

    def show_logout(Self, username):
        cmb = GUIComponents.confirmMessageBox('logout', 
                                              "{} do you want logout?".format(username), buttons = ['yes', 'no'])
        btn = cmb.render() 
        return btn == 'yes'
            

    def set_toolbar_login_button_icon(self, state:str):
        """change icon of login_logout button in toolbar of top of software

        Args:
            state (str): flags that determine icon. it could be 'login' or 'logout'
        """
        if state == 'login':
            GUIBackend.set_button_icon(self.ui.login_logout_btn, IconsPath.IconsPath.LOGIN_ICON)
        
        elif state == 'logout':
            GUIBackend.set_button_icon(self.ui.login_logout_btn, IconsPath.IconsPath.LOGOUT_ICON)
            
