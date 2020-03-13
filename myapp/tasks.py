from myapp.celery import celery


# @celery.on_after_configure.connect()
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
#
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
#
# @celery.task()
# def test(arg):
#     print(arg)
#     from flask import current_app
#     with current_app():
#         import logging
#         logging.error(arg)
#         from myapp.models import User
#         from uuid import uuid1
#         user = User.get_by_id(1)
#         user.last_name = str(uuid1())[1:7]
#         user.save()
