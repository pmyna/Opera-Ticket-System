from flask import *
from project import app, db, bcrypt
from project.form import *
from project.models import *
from flask_login import login_user, current_user


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/plan")
def plan():
    return render_template('plan.html', title='Spielplan & Kartenkauf')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        visitor = Visitor.query.filter_by(email=form.email.data).first()
        if visitor and bcrypt.check_password_hash(visitor.password, form.password.data):
            login_user(visitor, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Email oder Passwort falsch', 'danger')
    return render_template('login.html', title='Login', form=form)

