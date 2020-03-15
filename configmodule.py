import os

from dotenv import load_dotenv


load_dotenv()
env = os.getenv

ENV = env("ENV")


class Config(object):
    ENV = ENV
    DEBUG = False
    TESTING = False

    CELERY_BROKER_URL = env("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")

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
    TESTING = True
    POSTGRES_DB = f'test_{env("POSTGRES_DB")}'
    POSTGRES_HOST = env("POSTGRES_HOST")
    POSTGRES_PORT = env("POSTGRES_PORT")
    POSTGRES_USER = env("POSTGRES_USER")
    POSTGRES_PASSWORD = env("POSTGRES_PASSWORD")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )


def get_settings_object():
    if ENV == "development":
        return DevelopmentConfig
    elif ENV == "production":
        return ProductionConfig
    elif ENV == "TEST":
        return TestingConfig
