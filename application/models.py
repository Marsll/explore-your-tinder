from . import db


class User(db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    url = db.Column(db.String(60))
    create_date = db.Column(db.String(60))
    gender = db.Column(db.String(1)),
    gender_filter = db.Column(db.String(1))
