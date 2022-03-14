from flask import *
from form import *
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e435f666e9f07eb13be460507c9c12b3'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/plan")
def about():
    return render_template('plan.html', title='Spielplan & Kartenkauf')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Erfolgreich registriert!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registrierung', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Registrierung', form=form)


if __name__ == '__main__':
    app.run(debug=True)
