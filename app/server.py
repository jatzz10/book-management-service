from flask import jsonify
from app import app
from app.routes.books.books import books_resources
from app.routes.books.reviews import reviews_resources
from app.routes.users import users_resources


app.register_blueprint(books_resources, url_prefix='/api/v1/books')
app.register_blueprint(reviews_resources, url_prefix='/api/v1/books')
app.register_blueprint(users_resources, url_prefix='/api/v1/users')


@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Book Management Backend Service..!"})
