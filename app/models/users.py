from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email_id = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=datetime.now(), onupdate=datetime.now())

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "password": self.password,
            "email_id": self.email_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
