from flask import *
from form import *
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e435f666e9f07eb13be460507c9c12b3'

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


if __name__ == '__main__':
    app.run(debug=True)
