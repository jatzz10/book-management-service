from flask import Blueprint
from app.controllers.books.reviews import ReviewController
from flask_jwt_extended import jwt_required


reviews_resources = Blueprint("reviews_resources", __name__)
review_controller = ReviewController()


@reviews_resources.route("/<book_id>/reviews", methods=["POST"])
@jwt_required()
def create_review(book_id):
    """
    Create a review for a book
    ---
    post:
      summary: Create a review for a book
      description: Create a new review for a book with the provided details
      security:
        - bearerAuth: []
      parameters:
        - in: path
          name: book_id
          schema:
            type: integer
          required: true
          description: ID of the book
      requestBody:
        description: Review details
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                rating:
                  type: integer
                text:
                  type: string
      responses:
        201:
          description: Review created successfully
        400:
          description: Invalid request
    """
    return review_controller.create_review(book_id)


@reviews_resources.route("/<book_id>/reviews", methods=["GET"])
@jwt_required()
def get_reviews(book_id):
    """
    Get all reviews for a book
    ---
    get:
      summary: Get all reviews for a book
      description: Retrieve a list of all reviews for a book
      security:
        - bearerAuth: []
      parameters:
        - in: path
          name: book_id
          schema:
            type: integer
          required: true
          description: ID of the book
      responses:
        200:
          description: List of reviews
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Review'
        404:
          description: Book not found
    """
    return review_controller.get_all_reviews(book_id)