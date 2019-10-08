import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '9b984978331d6a10855d240366f91d6c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'demotest273@gmail.com'
app.config['MAIL_PASSWORD'] = 'Sakhofam1'

mail = Mail(app)

from flaskges_ecole.users.routes import users
from flaskges_ecole.main.routes import main
from flaskges_ecole.errors.handlers import errors
from flaskges_ecole.classes.routes import classes
from flaskges_ecole.eleves.routes import eleves

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(errors)
app.register_blueprint(classes)
app.register_blueprint(eleves)
