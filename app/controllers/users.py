from flask import jsonify, request
from app.models.users import User
from app import db

from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256


class UserController:
    def register_user(self):
        data = request.get_json()

        if User.query.filter(User.email_id == data["email_id"]).first():
            return jsonify({"message": "User with same email_id already exist."}), 409

        new_user = User(**data)
        # Hash the password
        new_user.password = pbkdf2_sha256.hash(data["password"])

        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201

    def login(self):
        user_data = request.get_json()
        user = User.query.filter(User.email_id == user_data["email_id"]).first()

        if user is None:
            return jsonify({"message": "User not found. Please register user."}), 404

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return jsonify({"access_token": access_token}), 200

        return jsonify({"message": "Invalid credentials."}), 401

    def get_user(self, user_id):
        user = User.query.get(user_id)
        if user is None:
            return jsonify({"message": "User not found."}), 404
        return jsonify(user.to_dict()), 200
