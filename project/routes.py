from flask import *
from project import app, db
from project.form import *
from project.models import *
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/plan")
@login_required
def plan():
    return render_template('plan.html', title='Spielplan & Kartenkauf')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    visitor = Visitor.query.filer_by(email=form.email.data).first()
    if visitor:
        flash('Email bereits registriert', 'danger')
    elif form.validate_on_submit():
        visitor = Visitor(first_name=form.first_name.data, last_name=form.last_name.data, zip_code=form.zip_code.data,
                          city=form.city.data, street=form.street.data, house_number=form.house_number.data,
                          landline=form.landline.data, phone_number=form.phone_number.data, email=form.email.data,
                          password=generate_password_hash(form.password.data), method='sha256')
        db.session.add(visitor)
        db.session.commit()
        login_user(visitor, remember=True)
        flash(f'Registrierung erfolgreich!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registrierung', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     visitor = Visitor.query.filter_by(email=form.email.data).first()
    #     if visitor and (visitor.password is form.password.data):
    #         login_user(visitor, remember=form.remember.data)
    #         return redirect(url_for('home'))
    #     elif visitor.password is not form.password.data: #gleiches passwort wird nicht akzeptiert?!
    #         flash('BUGGGY SHIT', 'danger')
    #     else:
    #         flash('Email oder Passwort falsch', 'danger')
    # return render_template('login.html', title='Login', form=form)
    if request.method == 'POST':
        form = LoginForm()
        email = request.form.get('email')
        password = request.form.get('password')

        visitor = Visitor.query.filer_by(email=email).first()
        if visitor:
            if check_password_hash(visitor.password, password):
                flash('Sie sind nun eingeloggt', 'success')
                login_user(visitor, remember=form.remember.data)
            else:
                flash('Falsches Passwort', 'danger')

        else: flash('Email nicht registriert!', 'danger')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))