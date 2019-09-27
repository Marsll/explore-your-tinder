from . import db


class User(db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    right_swipes = db.Column(db.Integer)
    left_swipes = db.Column(db.Integer)
