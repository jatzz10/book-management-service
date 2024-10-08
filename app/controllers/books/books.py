from flask import jsonify, request
from app import db
from app.models.books import Book


class BookController:
    def get_all_books(self) -> [Book]:
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books]), 200

    def get_book(self, book_id):
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        return jsonify(book.to_dict()), 200

    def create_book(self):
        # To Do: Add validations
        data = request.get_json()
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book created successfully!"}), 201

    def update_book(self, book_id):
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        data = request.get_json()
        if "title" in data:
            book.title = data["title"]
        if "author" in data:
            book.author = data["author"]
        if "genre" in data:
            book.genre = data["genre"]
        if "year_published" in data:
            book.year_published = data["year_published"]
        db.session.commit()
        return jsonify({"message": "Book updated successfully!"}), 200

    def delete_book(self, book_id):
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"}), 200