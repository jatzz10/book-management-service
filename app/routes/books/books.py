from flask import Blueprint
from app.controllers.books.books import BookController
from flask_jwt_extended import jwt_required


books_resources = Blueprint("books_resources", __name__)
book_controller = BookController()


@books_resources.route("/", methods=["POST"])
@jwt_required()
def create_book():
    return book_controller.create_book()


@books_resources.route("/", methods=["GET"])
@jwt_required()
def get_all_books():
    return book_controller.get_all_books()


@books_resources.route("/<book_id>", methods=["GET"])
@jwt_required()
def get_book(book_id):
    return book_controller.get_book(book_id)


@books_resources.route("/<book_id>", methods=["PUT"])
@jwt_required()
def put_book(book_id):
    return book_controller.update_book(book_id)


@books_resources.route("/<book_id>", methods=["DELETE"])
@jwt_required()
def delete_book(book_id):
    return book_controller.delete_book(book_id)
