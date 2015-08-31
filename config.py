import os

_basedir = os.path.abspath(os.path.dirname(__file__))

class Default:
    PORT = 5000

class Development(Default):
    DEBUG = True
    MONGODB_HOST = '192.168.99.101'
    MONGODB_PORT = 27017
    MONGODB_UNAME = 'user'
    MONGODB_PASS = 'password'
    DBS_NAME = 'devdb'

class Production(Default):
    MONGODB_HOST = 'my.prod.ip.address'
    MONGODB_PORT = 27017
    MONGODB_UNAME = 'user'
    MONGODB_PASS = 'password'
    DBS_NAME = 'prodb'

class Testing(Default):
    TESTING = True

config = {
    'DEFAULT': Default,
    'DEVELOPMENT': Development,
    'PRODUCTION': Production,
    'TESTING': Testing
}
