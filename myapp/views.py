import json

from flask import jsonify
from flask.views import View

from myapp.services import get_all_users


class UserListView(View):
    def dispatch_request(self):
        users = get_all_users()
        users_formatted = []
        response = {"users": users_formatted}
        for user in users:
            users_formatted.append({"id": user.id, "username": user.username, "email": user.email})
        return jsonify(json.dumps(response))
