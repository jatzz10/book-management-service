from flask import Blueprint
from app.controllers.books.reviews import ReviewController
from flask_jwt_extended import jwt_required


reviews_resources = Blueprint("reviews_resources", __name__)
review_controller = ReviewController()


@reviews_resources.route("/<book_id>/reviews", methods=["POST"])
@jwt_required()
def create_review(book_id):
    return review_controller.create_review(book_id)


@reviews_resources.route("/<book_id>/reviews", methods=["GET"])
@jwt_required()
def get_reviews(book_id):
    return review_controller.get_all_reviews(book_id)