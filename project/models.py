from project import db
import datetime


class Visitor(db.Model):
    customer_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    landline = db.Column(db.Integer)
    phone_number = db.Column(db.Integer)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Visitor('{self.customer_ID}', {self.first_name}, {self.last_name}, {self.zip_code}, {self.city}, {self.street}, {self.house_number})"


class Opera(db.Model):
    opera_ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text)
    show_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    language = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Opera %r>' % self.title
