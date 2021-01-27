from dataclasses import dataclass

from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


@dataclass
class User(db.Model):
    __tablename__ = 'user'

    id: int
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256))
    password = db.Column(db.String(256))

    @property
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
        }

    def __init__(self, username, password):
        self.username = username
        self.password = self.password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def password_hash(password):
        return generate_password_hash(password).decode('utf8')
