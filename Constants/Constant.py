class DemoImage:
    DIR = 'demo imgs/'


class User:
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

