from flask import Blueprint
from app.controllers.users import UserController

users_resources = Blueprint('users_resources', __name__)
user_controller = UserController()


@users_resources.route("/register", methods=["POST"])
def register_user():
    return user_controller.register_user()


@users_resources.route("/login", methods=["POST"])
def login():
    return user_controller.login()


@users_resources.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    return user_controller.get_user(user_id)


