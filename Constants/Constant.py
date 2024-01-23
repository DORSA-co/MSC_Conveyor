class SideBarAnimation:
    ANIMATION_DURATION = 300
    WIDTH_START_VALUE = 0
    WIDTH_STOP_VALUE = 198

class MessagesAnimation:
    MESSAGE_DURARTION = 3000
    FADE_IN_DURATION = 1000
    FADE_OUT_DURATION = 2500

class MessageColors:
    SUCCESS = '(17, 110, 62)'
    WARNING = '(255, 193, 7)'
    ERROR = '(244, 79, 90)'
    INFO = '(51, 190, 240)'

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

