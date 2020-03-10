import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import configmodule


db = SQLAlchemy()
migrate = Migrate()

load_dotenv()

RUN_MODE = os.getenv("RUN_MODE")  # PROD/DEV/TEST
CONFIG_OBJ = configmodule.DevelopmentConfig

if RUN_MODE == "PROD":
    CONFIG_OBJ = configmodule.ProductionConfig
elif RUN_MODE == "TEST":
    CONFIG_OBJ = configmodule.TestingConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(CONFIG_OBJ)

    from .views import UserListView

    app.add_url_rule("/", view_func=UserListView.as_view("users"))

    db.init_app(app)
    migrate.init_app(app, db)

    return app
