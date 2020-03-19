import json

from flask import jsonify
from flask.views import View

from myapp.celery import test
from myapp.services import get_all_users
from utils.logger import logger


class Greeting(View):
    def dispatch_request(self):
        test.apply_async(("1245215",),)
        logger.info("View triggered")
        return "<span style='color:red'>I am app 1</span>"


class UserListView(View):
    def dispatch_request(self):
        users = get_all_users()
        users_formatted = []
        response = {"users": users_formatted}
        for user in users:
            users_formatted.append(
                {"id": user.id, "username": user.username, "email": user.email, "first_name": user.first_name}
            )
        return jsonify(json.dumps(response))
