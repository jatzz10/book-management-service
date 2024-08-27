from flask import jsonify, request
from app import db
from app.models.books import Book
from app.models.reviews import Review


class ReviewController:
    def create_review(self, book_id):
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({"message": "Book not found"}), 404

        data = request.get_json()
        review = Review(book_id=book_id, **data)
        db.session.add(review)
        db.session.commit()
        return jsonify({"message": "Review created successfully!"})

    def get_all_reviews(self, book_id):
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        reviews = Review.query.filter(Review.book_id == book_id).all()
        return jsonify([review.to_dict() for review in reviews])