from project import db
from datetime import *
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    landline = db.Column(db.Integer, nullable=True)
    phone_number = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    @property
    def __repr__(self):
        return f"User('{self.id}', '{self.first_name}', '{self.last_name}', '{self.email}', '{self.password}')"

    def get_id(self):
        return self.id


class Opera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text)
    show_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    language = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Opera %r>' % self.title
