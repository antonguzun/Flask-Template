from celery import Celery
from flask import Flask

from configmodule import get_settings_object
from database import db_session


def make_celery(app):
    celery = Celery(
        app.import_name, backend=app.config["CELERY_RESULT_BACKEND"], broker=app.config["CELERY_BROKER_URL"]
    )
    celery.conf.update(app.config)

    return celery


settings = get_settings_object()

flask_app = Flask(__name__)
flask_app.config.from_object(get_settings_object())

celery = make_celery(flask_app)


@celery.on_after_configure.connect()
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s("hello"), name="add every 10")

    sender.add_periodic_task(30.0, test.s("world"), expires=10)


@celery.task(ignore_result=True)
def test(arg):
    print(arg)
    from myapp.models import User
    from utils.logger import logger

    logger.error(arg)
    user = User.query.get(1)
    user.first_name = arg
    db_session.commit()
    logger.error("Lastname fixed")
