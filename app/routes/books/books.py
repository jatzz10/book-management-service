from flask import Blueprint
from app.controllers.books.books import BookController
from flask_jwt_extended import jwt_required


books_resources = Blueprint("books_resources", __name__)
book_controller = BookController()


@books_resources.route("/", methods=["POST"])
@jwt_required()
def create_book():
    """
    Create a new book
    ---
    post:
      summary: Create a new book
      description: Create a new book with the provided details
      security:
        - bearerAuth: []
      requestBody:
        description: Book details
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                author:
                  type: string
      responses:
        201:
          description: Book created successfully
        400:
          description: Invalid request
    """
    return book_controller.create_book()


@books_resources.route("/", methods=["GET"])
@jwt_required()
def get_all_books():
    """
    Get all books
    ---
    get:
      summary: Get all books
      description: Retrieve a list of all books
      security:
        - bearerAuth: []
      responses:
        200:
          description: List of books
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Book'
        401:
          description: Unauthorized
    """
    return book_controller.get_all_books()


@books_resources.route("/<book_id>", methods=["GET"])
@jwt_required()
def get_book(book_id):
    """
    Get a book by ID
    ---
    get:
      summary: Get a book by ID
      description: Retrieve a book by its ID
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
          description: Book details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Book'
        404:
          description: Book not found
    """
    return book_controller.get_book(book_id)


@books_resources.route("/<book_id>", methods=["PUT"])
@jwt_required()
def put_book(book_id):
    """
    Update a book
    ---
    put:
      summary: Update a book
      description: Update a book with the provided details
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
        description: Book details
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                author:
                  type: string
      responses:
        200:
          description: Book updated successfully
        400:
          description: Invalid request
    """
    return book_controller.update_book(book_id)


@books_resources.route("/<book_id>", methods=["DELETE"])
@jwt_required()
def delete_book(book_id):
    """
    Delete a book
    ---
    delete:
      summary: Delete a book
      description: Delete a book by its ID
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
        204:
          description: Book deleted successfully
        404:
          description: Book not found
    """
    return book_controller.delete_book(book_id)
