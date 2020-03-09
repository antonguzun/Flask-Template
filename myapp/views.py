from flask.views import View
from flask import jsonify


class UserListView(View):
    def dispatch_request(self):
        return jsonify('{"user1": 1, "user2": 2}')
