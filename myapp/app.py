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

if RUN_MODE == "PROD":
    CONFIG_OBJ = configmodule.ProductionConfig
elif RUN_MODE == "DEV":
    CONFIG_OBJ = configmodule.DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(CONFIG_OBJ)

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    from myapp.controllers import base_bp

    app.register_blueprint(base_bp)


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", debug=True)
