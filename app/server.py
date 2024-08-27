from flask import jsonify
from app import app
from app.routes.books.books import books_resources
from app.routes.books.reviews import reviews_resources


app.register_blueprint(books_resources, url_prefix='/books')
app.register_blueprint(reviews_resources, url_prefix='/books')


@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Book Management Backend Service..!"})
