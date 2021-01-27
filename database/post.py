from dataclasses import dataclass

from .db import db


@dataclass
class Post(db.Model):
    __tablename__ = 'post'

    id: int
    text: str
    user_id: int

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    writer: db.relationship('User', backref='Post', lazy=True)

    @property
    def json(self):
        return {
            'id:': self.id,
            'text': self.text,
            'uesr_id': self.user.id
        }
