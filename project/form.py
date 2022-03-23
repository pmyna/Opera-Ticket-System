from flask_wtf import *
from wtforms import *
from wtforms.validators import EqualTo, DataRequired, Length, Regexp


class RegistrationForm(FlaskForm):
    first_name = StringField('Vorname', [DataRequired()])
    last_name = StringField('Nachname', [DataRequired()])
    zip_code = StringField('Postleitzahl', validators=[DataRequired(), Length(min=4, max=4), Regexp(regex='^[0-9]{4}$', message='Nur Zahlen erlaubt')])
    city = StringField('Ort', [DataRequired()])
    street = StringField('Straße', [DataRequired()])
    house_number = StringField('Hausnummer', [DataRequired(), Length(min=1, max=7)])
    landline = StringField('Festnetz', [Length(min=0, max=14)])
    phone_number = StringField('Mobiltelefon', [Length(min=0, max=14)])
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Passwort', [DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Passwort bestätigen', [DataRequired(), Length(min=5, max=20), EqualTo('password', message='Passwort stimmt nicht überein')])
    submit = SubmitField('Registrieren')


class LoginForm(FlaskForm):
    email = StringField('E-Mail', [DataRequired()])
    password = PasswordField('Passwort', [DataRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember me')
    login = SubmitField('Login')


class PurchaseForm(FlaskForm):
    show = IntegerField('Reservation')
    purchase = SubmitField('Karten kaufen')
