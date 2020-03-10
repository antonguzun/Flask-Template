from flask import Blueprint

from myapp.views import Greeting, UserListView


base_bp = Blueprint("base", __name__, url_prefix="/")


base_bp.add_url_rule("users/", view_func=UserListView.as_view("user-list"), methods=["GET"])
base_bp.add_url_rule("/", view_func=Greeting.as_view("Greeting"), methods=["GET"])
