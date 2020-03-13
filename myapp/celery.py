from celery import Celery
from flask import Flask

from config.configmodule import get_settings_object
from myapp.app import db


def make_celery(app):
    celery = Celery(
        app.import_name, backend=app.config["CELERY_RESULT_BACKEND"], broker=app.config["CELERY_BROKER_URL"]
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


settings = get_settings_object()

flask_app = Flask(__name__)
flask_app.config.from_object(get_settings_object())
db.init_app(flask_app)

celery = make_celery(flask_app)


@celery.on_after_configure.connect()
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s("hello"), name="add every 10")

    sender.add_periodic_task(30.0, test.s("world"), expires=10)


@celery.task()
def add_together(a, b):
    return a + b


@celery.task()
def test(arg):
    print(arg)
    import logging
    from myapp.models import User

    logging.error(arg)
    user = User.get_by_id(1)
    user.last_name = arg
    user.save()
    logging.error("Lastname fixed")
