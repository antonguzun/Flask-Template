from flask import Flask

from configmodule import get_settings_object


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_settings_object())

    register_blueprints(app)

    from database import db_session

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app


def register_blueprints(app: Flask):
    from myapp.controllers import base_bp

    app.register_blueprint(base_bp)


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", debug=True)
