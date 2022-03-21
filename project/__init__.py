from flask import Flask
from flask_sqlalchemy import *
from flask_login import LoginManager
from os import path
from flask import url_for


# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e435f666e9f07eb13be460507c9c12b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Setup and Run Database
db = SQLAlchemy()
db.init_app(app)

from . import routes, models, form
from .models import User


def create_database(app):
    if not path.exists('project/site.db'):
        db.create_all(app=app)

create_database(app)

# Login Manager
login_manager = LoginManager()
login_manager.login_view = 'home'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
