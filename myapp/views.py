from flask import jsonify
from flask.views import View


class UserListView(View):
    def dispatch_request(self):
        return jsonify('{"user1": 1, "user2": 2}')
