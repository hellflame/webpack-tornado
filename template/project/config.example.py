import os
from .service.base import NormalBase

PWD = os.path.dirname(__file__)
DEBUG = False

if DEBUG:
    settings = {
        'debug': True,
        'autoreload': True,
        'serve_traceback': True,
        'cookie_secret': 'SECRET DEBUG',
        'template_path': PWD + '/templates',
        'static': PWD + '/static',
        "public": PWD + '/public',
        'domain': None,
        'default_handler_class': NormalBase
    }
else:
    settings = {
        'debug': False,
        'autoreload': True,
        'serve_traceback': False,
        'cookie_secret': 'SECRET PRO',
        'template_path': PWD + '/templates',
        'static': PWD + '/static',
        "public": PWD + '/public',
        'domain': None,
        'default_handler_class': NormalBase
    }


