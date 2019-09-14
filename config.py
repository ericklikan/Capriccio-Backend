import os


class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = set(['bmp','jpg'])

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True