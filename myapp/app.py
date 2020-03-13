from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config.configmodule import get_settings_object, setup_logger
from myapp.controllers import base_bp


db = SQLAlchemy()
migrate = Migrate()


setup_logger()

app = Flask(__name__)
app.config.from_object(get_settings_object())

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(base_bp)
