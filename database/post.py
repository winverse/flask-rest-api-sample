from dataclasses import dataclass

from .db import db


@dataclass
class Post(db.Model):
    __tablename__ = 'post'

    id: int
    text: str

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id

    @property
    def serialize(self):
        return {
            'id:': self.id,
            'text': self.text,
            'uesr_id': self.user_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
