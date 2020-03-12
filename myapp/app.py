from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from configmodule import get_settings_object


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_settings_object())

    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    from myapp.controllers import base_bp

    app.register_blueprint(base_bp)


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", debug=True)
