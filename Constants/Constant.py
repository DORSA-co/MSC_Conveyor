class SideBarAnimation:
    ANIMATION_DURATION = 300
    WIDTH_START_VALUE = 0
    WIDTH_STOP_VALUE = 198

class DemoImage:
    DIR = 'demo imgs/'


class RefreshRates:
    MOUSE_MOVE = 0.01


class User:
    UNLOGIN_USER_ROLE = 'unknown'
    UNLOGIN_USER_ROLE = 'unknown'
    MIN_USERNAME_LENGHT = 4
    MIN_PASS_LENGHT = 5
    USER_ROLES = ['admin', 'user']

    ACCESS = {
    'admin': {
        'pages': 'all',
        'tabs': {
                'users': 'all',
                'settings': 'all'
                },
        
    },

    'user':{
        'pages': ['live', 'users', 'about'],
        'tabs': {'users': ['edit_profile']
                 }
        
    },

    UNLOGIN_USER_ROLE:{
        'pages' : [ 'about'],
        'tabs': dict(),
    },
}

