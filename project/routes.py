from flask import *
from sqlalchemy import *
from project import app, db
from project.form import *
from project.models import *
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', user=current_user)


@app.route("/plan", methods=['GET', 'POST'])
def plan():
    opera = Opera.query.all()
    show = Show.query.all()
    reservation = Reservation.query.all()
    # Make Pretty
    # Add Ticket Kaufen Buttons
    return render_template('plan.html', title='Spielplan & Kartenkauf', opera=opera, show=show, reservation=reservation, user=current_user)


@app.route("/ticket", methods=['GET', 'POST'])
@login_required
def ticket():
    # Render Template from Selection in /plan
    # Select Loge/Parkett for Price
    # Select Amount Tickets
    # Calculate Price - from DB
    # "Kaufen" Button + Bestätigung der Reservierung [Show Reservation Number - from DB]
    return render_template('ticket.html', title='Ticketkauf', user=current_user)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():

        first = request.form.get('first_name')
        last = request.form.get('last_name')
        email = request.form.get('email')
        zip = request.form.get('zip_code')
        city = request.form.get('city')
        street = request.form.get('street')
        house = request.form.get('house_number')
        land = request.form.get('landline')
        phone = request.form.get('phone_number')
        pwd = request.form.get('password')

        new_user = User(first_name=first, last_name=last, email=email, zip_code=zip, city=city, street=street, house_number=house,
                        landline=land, phone_number=phone, password=generate_password_hash(pwd, method='sha256'))

        validate_mail = User.query.filter_by(email=email).first()
        if validate_mail:
            flash('Email bereits registriert', 'danger')
        else:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash(f'Registrierung erfolgreich!', 'success')
            return redirect(url_for('home'))
    return render_template('register.html', title='Registrierung', form=form, user=current_user)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Sie sind nun eingeloggt', 'success')
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))
            else:
                flash('Falsches Passwort', 'danger')
        else:
            flash('Email nicht registriert!', 'danger')

    return render_template('login.html', form=form, title='Login', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))