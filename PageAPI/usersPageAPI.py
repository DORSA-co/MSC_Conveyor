
from PageUI.users_UI import usersPageUI, RegisterUserTabUI, AllUserTabUI, EditUserTabUI,LoginUserUI
from Database.users_DB import usersDB
from backend.UserManager.userLoginRegister import passwordManager, regiterUtils
from Constants import Constant
#from main_UI import routerUI


class dataPasser:
    def __init__(self) -> None:
        self.login_flag = False
        self.logined_user = {}
        #self.logined_user = {'role':'admin'}

    def get_logined_user_role(self,):
        return self.logined_user.get('role', Constant.User.UNLOGIN_USER_ROLE)
    
    def get_logined_user_password(self,):
        return self.logined_user.get('password', Constant.User.UNLOGIN_USER_PASSWORD)
    
    def get_logined_user_username(self,):
        return self.logined_user.get('username', Constant.User.UNLOGIN_USER_USERNAME)

class usersPageAPI:

    def __init__(self, ui:usersPageUI,database:usersDB, ):
        self.uiHandeler = ui
        self.database = database
        self.data_passer = dataPasser()
        #self.router = router
        
        
        self.external_login_func_event = None

        self.registerUser = RegisterUserTabAPI(ui.registerTab, database, self.data_passer)
        self.allUser = AllUserTabAPI(ui.allUserTab, database, self.data_passer)
        self.loginUser = LoginUserAPI(ui.LoginUser, database, self.data_passer)
        self.editUser = EditUserTabAPI(self.uiHandeler.editUserTab, self.database, self.data_passer)

        self.registerUser.set_register_event(self.new_user_register_event)
        self.loginUser.set_login_event_func(self.user_login_event)
        self.editUser.set_user_edit_event_func(self.user_edited_event)

    def startup(self,):
        self.allUser.startup()
        #self.loginUser.startup()
    
    def endup(self,):
        return True
        

    def set_login_event(self, func):
        self.external_login_func_event = func
    
    def new_user_register_event(self,):
        self.allUser.load_users()
    
    def user_login_event(self,):
        self.editUser.refresh()
        if self.external_login_func_event is not None:
            self.external_login_func_event()
    
    def user_edited_event(self):
        self.loginUser.update_logedin_user()
        self.allUser.load_users()


class RegisterUserTabAPI:

    def __init__(self, ui:RegisterUserTabUI ,database: usersDB, data_passer: dataPasser):
        self.uiHandeler = ui
        self.database = database
        self.data_passer = data_passer

        self.register_event_func = None
        self.uiHandeler.register_button_connector(self.register)
        self.uiHandeler.set_user_roles_items( Constant.User.USER_ROLES )
        


    def register(self,):
        user_inputs = self.uiHandeler.get_register_fields()

        if len(user_inputs['username']) < Constant.User.MIN_USERNAME_LENGHT:
            self.uiHandeler.write_register_error(f'Username is Should be at least {Constant.User.MIN_USERNAME_LENGHT} character')
            return
        
        if self.database.is_exist(user_inputs['username']):
            self.uiHandeler.write_register_error('Username is already exist!')
            return
        
        if not regiterUtils.is_pass_lenght_ok(user_inputs['password']):
            self.uiHandeler.write_register_error("Password should be at least {}".format(Constant.User.MIN_PASS_LENGHT))
            return

        if not user_inputs['password'] == user_inputs['password_confirm']:
            self.uiHandeler.write_register_error("Password and password confirm aren't same")
            return
        
        #make password hash
        user_inputs['password'] = passwordManager.hash_password(user_inputs['password'])
        #remove password_confirm for save in database
        user_inputs.pop('password_confirm')
        #save in database
        self.database.save(user_inputs)
        self.uiHandeler.reset()
        self.uiHandeler.show_success_msg('Success Register')

        if self.register_event_func is not None:
            self.register_event_func()


    def set_register_event(self, func):
        self.register_event_func = func


class AllUserTabAPI:

    def __init__(self, ui:AllUserTabUI ,database: usersDB, data_passer:dataPasser):
        self.uiHandeler = ui
        self.database = database
        self.data_passer = data_passer

        self.uiHandeler.table_external_event_connector(self.modify_users)
        self.uiHandeler.editUserDialog.set_role_items(Constant.User.USER_ROLES)
        self.uiHandeler.editUserDialog.save_button_connector(self.update_user) 

        self.startup()
        

    
    def startup(self,):
        self.load_users()

    

    def load_users(self,):
        users = self.database.load_all()
        self.uiHandeler.set_users_table(users)
        self.selected_user_for_edit = {}



    def modify_users(self,idx, user, flag, btn):
        if flag == 'delete':
            response = self.uiHandeler.show_confirm_box("Delete User",
                                                "Are you sure you want to delete '{}' ?".format(user['username']),
                                                  buttons=['yes', 'cancel'],
                                                  icon_type='question')
            if response == 'cancel':
                return
            
            self.database.remove(user['username'])
            self.load_users()

        if flag == 'edit':    
            self.selected_user_for_edit = user
            self.uiHandeler.editUserDialog.show_win(user)
    

    def update_user(self,):
        new_info = self.uiHandeler.editUserDialog.get_inputs()
        #check if password change, hash new password
        if self.selected_user_for_edit['password'] != new_info['password']:
            #check new password has enough lengh
            if len(new_info['password']) < Constant.User.MIN_PASS_LENGHT:
                self.uiHandeler.editUserDialog.write_edit_user_error(
                    "Password should be at least {} character".format(Constant.User.MIN_PASS_LENGHT)
                    )
                return
            
            new_info['password'] = passwordManager.hash_password(new_info['password'])

        #check if username change, remove previous in database
        if self.selected_user_for_edit['username'] != new_info['username']:
            #check new username not taken befor bu another
            if self.database.is_exist(new_info['username']):
                self.uiHandeler.editUserDialog.write_edit_user_error(
                    "This User name is already exist"
                    )
                return
        
        #remove previous record
        #self.database.remove(self.selected_user_for_edit['username'])
        new_info['id'] = self.selected_user_for_edit['id']
        self.database.update(new_info)
        self.load_users()
        self.uiHandeler.editUserDialog.close()



class EditUserTabAPI:

    def __init__(self, ui:EditUserTabUI ,database: usersDB, data_passer:dataPasser):
        self.uiHandeler = ui
        self.database = database
        self.data_passer = data_passer

        self.user = {}
        self.user_edit_event_func = None

        self.uiHandeler.button_connector('change_username', self.change_username)
        self.uiHandeler.button_connector('change_password', self.change_password)


    def set_user_edit_event_func(self, func):
        self.user_edit_event_func = func

    def refresh(self,):
        self.uiHandeler.set_edit_profile_fields(self.data_passer.logined_user)

    def change_username(self):
        login_flag = self.data_passer.login_flag
        logined_user = self.data_passer.logined_user

        if not login_flag:
            self.uiHandeler.write_error('change_username',
                                        "Please login first")
            return

        new_info = self.uiHandeler.get_edit_profile_fields()

        if len(new_info['username']) < Constant.User.MIN_USERNAME_LENGHT:
            self.uiHandeler.write_error('change_username',
                                        f"Username should be at least {Constant.User.MIN_USERNAME_LENGHT} character!")
            return

        if new_info['username'] != logined_user['username']:
            if self.database.is_exist(new_info['username']):
                self.uiHandeler.write_error('change_username',
                                            "This Username is already exist!")
                return 
            
        #update information
        for key , value in new_info.items():
            logined_user[key] = value
        
        #updated logined user information
        self.data_passer.logined_user = logined_user
        #save new logined user information into database
        self.database.update(logined_user)
        
        self.uiHandeler.show_success_msg("change_username", "User Information Updated")
        if self.user_edit_event_func is not None:
            self.user_edit_event_func()
        self.refresh()
    

    def change_password(self):
        info = self.uiHandeler.get_change_password_fields()


        if len(info['old_password']) == 0 or len(info['new_password']) == 0 or len(info['confirm_new_password']) == 0:
            self.uiHandeler.write_error('change_password',
                                        'Please Complete all fields')
            return

        if not passwordManager.check_password(info['old_password'], self.data_passer.logined_user['password']):
            self.uiHandeler.write_error('change_password',
                                        'Old password is Incorect')
            return
        
        if len(info['new_password']) < Constant.User.MIN_PASS_LENGHT:
            self.uiHandeler.write_error('change_password',
                                        "Password should be at least {} character".format(Constant.User.MIN_PASS_LENGHT))
            return

        
        if info['new_password'] != info['confirm_new_password']:
            self.uiHandeler.write_error('change_password', 
                                        "New password and it's confirm aren't same")
            return
        
        
        new_password = info['new_password']
        hashed_new_password = passwordManager.hash_password(new_password)
        self.data_passer.logined_user['password'] = hashed_new_password
        self.database.save(self.data_passer.logined_user)
        
        self.uiHandeler.write_error('change_password', None)
        self.uiHandeler.clear_change_password_fields()
        self.uiHandeler.show_success_msg("change_password", "password changed")

        if self.user_edit_event_func is not None:
            self.user_edit_event_func()


class LoginUserAPI:

    def __init__(self, ui:LoginUserUI, database:usersDB, data_passer:dataPasser) -> None:
        self.uiHandeler = ui
        self.database = database
        self.data_passer = data_passer

        self.login_event_func = None

        #this button is login button on top of software
        self.uiHandeler.login_button_connector(self.login_logout)
        #this button is login button on login dialog box
        self.uiHandeler.loginDialog.login_button_connector(self.login)
        self.uiHandeler.set_logedin_username(None)

    def startup(self):
        pass

    def set_login_event_func(self, func):
        self.login_event_func = func
    
    def login_logout(self):
        """this function called when loging_logout button in top of wofrware pressed
        """
        if not self.data_passer.login_flag:
            self.uiHandeler.loginDialog.show_win()
        
        else :
            flag = self.uiHandeler.show_logout(self.data_passer.logined_user['username'])
            if flag:
                self.logout()


    def login(self):
        """this function call when login button on dialogbox pressed
        """
        input_user = self.uiHandeler.loginDialog.get_inputs()
        username = input_user['username']
        password = input_user['password']

        if len(password) == 0 or len(username) == 0:
            self.uiHandeler.loginDialog.write_error('Please enter all fields')
            return
        
        if not self.database.is_exist(username):
            self.uiHandeler.loginDialog.write_error("Username dosen't exist")
            return
        
        user_db = self.database.load(username)
        if not passwordManager.check_password(password, user_db['password']):
            self.uiHandeler.loginDialog.write_error("Password is wrong")
            return
        #this flag shows a user is login or not
        self.data_passer.login_flag = True
        #store logedin user
        self.data_passer.logined_user = user_db
        #show logedin username on top of sofrware
        self.uiHandeler.set_logedin_username(user_db['username'])
        #clear username and password from input fields
        self.uiHandeler.loginDialog.close_win()
        self.uiHandeler.set_toolbar_login_button_icon('logout')

        if self.login_event_func is not None:
            self.login_event_func()



    def logout(self):
        #this flag shows a user is login or not
        self.data_passer.login_flag = False
        #clear logedin user info
        self.data_passer.logined_user = {}
        #clear logedin username on top of sofrware
        self.uiHandeler.set_logedin_username(None)
        self.uiHandeler.set_toolbar_login_button_icon('login')

        if self.login_event_func is not None:
            self.login_event_func()

    

    def update_logedin_user(self) :
        self.uiHandeler.set_logedin_username(self.data_passer.logined_user['username'])



        
    

        