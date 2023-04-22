import uuid

from . import db


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    distributed_by = db.Column(db.String(128), nullable=False)
    length = db.Column(db.Float)
    rating = db.Column(db.Float)

    def __init__(self, title, release_date, description, distributed_by, length, rating):
        self.title = title
        self.release_date = release_date
        self.uuid = str(uuid.uuid4())
        self.description = description
        self.distributed_by = distributed_by
        self.length = length
        self.rating = rating

    def __repr__(self):
        return f'Film({self.title}, {self.release_date}, {self.uuid}, {self.distributed_by})'

    def to_dict(self):
        return {
            'title': self.title,
            'uuid': self.uuid,
            'release_date': self.release_date.strftime('%Y-%m-%d'),
            'distributed_by': self.distributed_by,
            'description': self.description,
            'length': self.length,
            'rating': self.rating,
        }


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, index=True, nullable=False)
    is_active = db.Column(db.Boolean, unique=False, default=True)

    def __init__(self, name, birthday, is_active):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.birthday = birthday
        self.is_active = is_active

    def __repr__(self):
        return f'Actor({self.name}, {self.birthday}, {self.uuid}, {self.is_active})'

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'name': self.name,
            'birthday': self.birthday.strftime('%Y-%m-%d'),
            'is_active': self.is_active,
        }