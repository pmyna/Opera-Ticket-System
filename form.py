from flask_wtf import *
from wtforms import *
from wtforms.validators import *


class RegistrationForm(FlaskForm):
    first_name = StringField('Vorname', [DataRequired()])
    last_name = StringField('Nachname', [DataRequired()])
    zip_code = StringField('Postleitzahl', validators=[DataRequired(), Length(min=4, max=4), Regexp(regex='^[0-9]$')])
    city = StringField('Ort', [DataRequired()])
    street = StringField('Straße', [DataRequired()])
    house_number = StringField('Hausnummer', [DataRequired(), Length(min=1, max=7), Regexp(regex='^[0-9]$')])
    landline = StringField('Festnetz', [Length(min=8, max=14), Regexp(regex='^[0-9]$')])
    phone_number = StringField('Handy', [Length(min=8, max=14), Regexp(regex='^[0-9]$')])
    password = PasswordField('Passwort', [DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Passwort Wiederholen', [DataRequired(), Length(min=5, max=20), EqualTo('password')])

    submit = SubmitField('Registrieren')


class LoginForm(FlaskForm):
    customer_ID = StringField('Kundennummer', [DataRequired(), Length(min=3, max=3), Regexp(regex='^[0-9]$')])
    password = PasswordField('Passwort', [DataRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember me')

    login = SubmitField('Login')
