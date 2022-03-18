from flask import *
from project import app, db, bcrypt
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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        visitor = Visitor(first_name=form.first_name.data, last_name=form.last_name.data, zip_code=form.zip_code.data,
                          city=form.city.data, street=form.street.data, house_number=form.house_number.data,
                          landline=form.landline.data, phone_number=form.phone_number.data, email=form.email.data, password=hashed_password)
        db.session.add(visitor)
        db.session.commit()
        flash(f'Registrierung erfolgreich!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registrierung', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@test.com' and form.password.data == 'test1234':
            flash(f'Erfolgreich eingeloggt', 'success')
            return redirect(url_for('home'))
        else:
            flash('Email oder Passwort falsch', 'danger')
    return render_template('login.html', title='Login', form=form)

