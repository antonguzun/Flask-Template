class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:somepass@localhost:5432/flasktemplate'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://verysequrename:pass@notlocalhost:5432/flasktemplate'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:somepass@localhost:5432/test_flasktemplate'
    TESTING = True
