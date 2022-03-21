from flask import Flask
from flask_sqlalchemy import *
from flask_login import LoginManager
from os import path


def create_database(app):
    if not path.exists('project/site.db'):
        db.create_all(app=app)
        print('Database created')

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e435f666e9f07eb13be460507c9c12b3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#Setup and Run Database
db = SQLAlchemy()
db.init_app(app)

from project import routes, models, form

create_database(app)

#Login Manager
login_manager = LoginManager()
login_manager.login_view = 'routes.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_visitor(customer_ID):
    return Visitor.query.get(customer_ID)

