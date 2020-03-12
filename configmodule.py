import os

from dotenv import load_dotenv


load_dotenv()
env = os.getenv

ENV = env("ENV")


class Config(object):
    ENV = ENV
    DEBUG = False
    TESTING = False
    POSTGRES_DB = env("POSTGRES_DB")
    POSTGRES_HOST = env("POSTGRES_HOST")
    POSTGRES_PORT = env("POSTGRES_PORT")
    POSTGRES_USER = env("POSTGRES_USER")
    POSTGRES_PASSWORD = env("POSTGRES_PASSWORD")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = env("PRODUCTION_DATABASE")


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQL_DB_NAME = f'test_{env("DB_NAME")}'
    TESTING = True


def get_settings_object():
    if ENV == "development":
        return DevelopmentConfig
    elif ENV == "production":
        return ProductionConfig


def get_test_settings_object():
    return TestingConfig
