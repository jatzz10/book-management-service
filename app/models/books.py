from datetime import datetime
from app import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(20), nullable=True)
    year_published = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "year_published": self.year_published,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }