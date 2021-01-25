from .db import db


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    uesrname = db.Column(db.String(256))
    password = db.Column(db.String(256))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'uesrname': self.username,
        }
