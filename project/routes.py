from flask import *
from project import app
from project.form import *
from project.models import *


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/plan")
def plan():
    return render_template('plan.html', title='Spielplan & Kartenkauf')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Registrierung erfolgreich! \n Ihre Kundennummer für den Login ist 123', 'success') #Kundennummer-Anzeige mit DB verbinden
        return redirect(url_for('home'))
    return render_template('register.html', title='Registrierung', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.customer_ID.data == '123' and form.password.data == 'test1234':
            flash(f'Erfolgreich eingeloggt', 'success')
            return redirect(url_for('home'))
        else:
            flash('Kundennummer oder Passwort falsch', 'danger')
    return render_template('login.html', title='Login', form=form)

