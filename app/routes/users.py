from flask import Blueprint
from app.controllers.users import UserController

users_resources = Blueprint('users_resources', __name__)
user_controller = UserController()


@users_resources.route("/register", methods=["POST"])
def register_user():
    """
    Register a new user
    ---
    post:
      summary: Register a new user
      description: Create a new user account with the provided details
      requestBody:
        description: User details
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                email:
                  type: string
                password:
                  type: string
      responses:
        201:
          description: User created successfully
        400:
          description: Invalid request
    """
    return user_controller.register_user()


@users_resources.route("/login", methods=["POST"])
def login():
    """
    Login a user
    ---
    post:
      summary: Login a user
      description: Authenticate a user with the provided credentials
      requestBody:
        description: User credentials
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                password:
                  type: string
      responses:
        200:
          description: User logged in successfully
        401:
          description: Invalid credentials
    """
    return user_controller.login()


@users_resources.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    """
    Get a user by ID
    ---
    get:
      summary: Get a user by ID
      description: Retrieve a user's details by their ID
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
          required: true
          description: ID of the user
      responses:
        200:
          description: User details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        404:
          description: User not found
    """
    return user_controller.get_user(user_id)


