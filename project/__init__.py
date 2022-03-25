import datetime
from flask import Flask
from flask_sqlalchemy import *
from flask_login import LoginManager
from os import path
from flask import url_for

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e435f666e9f07eb13be460507c9c12b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oper.db'

# Setup and Run Database
db = SQLAlchemy()
db.init_app(app)

from . import routes, models, form
from .models import *

# Start with empty Database
with app.app_context():
    db.drop_all()
    db.create_all(app=app)

# Login Manager
login_manager = LoginManager()
login_manager.login_view = 'plan'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# Example Data
opera1 = Opera(title='Zauberflöte', body='Eine deutsche Oper in zwei Aufzügen KV 620 (1791)\nLibretto von Emanuel Schikaneder')
opera2 = Opera(title='Carmen', body='Opéra comique in vier Akten\nMusik - Georges Bizet \n Text - Henri Meilhac & Ludovic Halévy nach Prosper Mérimée')
opera3 = Opera(title='Aida', body='Oper in vier Akten (1871)\nLibretto von Antonio Ghislanzoni nach einem Szenarium von Auguste Mariette')
show1 = Show(opera=1, show_date=datetime(2022, 4, 12, 20, 15), language='English')
show4 = Show(opera=1, show_date=datetime(2022, 4, 12, 18, 30), language='Deutsch')
show2 = Show(opera=2, show_date=datetime(2022, 4, 18, 19, 00), language='Français')
show3 = Show(opera=2, show_date=datetime(2022, 4, 15, 22, 15), language='Deutsch')
show5 = Show(opera=3, show_date=datetime(2022, 5, 1, 19, 00), language='Italiano')

with app.app_context():
    db.session.add(opera1)
    db.session.add(opera2)
    db.session.add(opera3)
    db.session.add(show1)
    db.session.add(show2)
    db.session.add(show3)
    db.session.add(show4)
    db.session.add(show5)
    db.session.commit()
