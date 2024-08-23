from app import db
from enum import Enum
from datetime import datetime


class RatingEnum(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.String(50), default='', nullable=False)
    review_text = db.Column(db.Text, default='', nullable=False)
    rating = db.Column(db.Enum(RatingEnum), nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f"Review('{self.id}', '{self.review_text}', '{self.rating}')"

    def to_dict(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "review_text": self.review_text,
            "rating": self.rating.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
