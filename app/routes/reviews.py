from flask import jsonify, Blueprint
from app import app
from app.models.reviews import Review
from app.controllers.reviews import ReviewController


reviews_resources = Blueprint("reviews_resources", __name__)


review_controller = ReviewController()


@reviews_resources.route("/<book_id>/reviews", methods=["POST"])
def create_review(book_id):
    return review_controller.create_review(book_id)


@reviews_resources.route("/<book_id>/reviews", methods=["GET"])
def get_reviews(book_id):
    return review_controller.get_all_reviews(book_id)