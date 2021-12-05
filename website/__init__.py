# This __init__ file will make the website a Python package. 
# This means we can import this file and everything here would run automatically


from flask import Flask

from flask_sqlalchemy import SQLAlchemy
# Importing our database library

from os import path
# Importing path so we can check database exists


db = SQLAlchemy()
# Creating the database object first and then configuring it in create_app()
DB_NAME = "database.db"
# The file name of our database

# Using this module we can tell our flask app how we actually login in our user.
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    # Initializing the Flask App
    # __name__ denotes the name of the file that was ran
    app.config['SECRET_KEY'] = 'SHARIFISCOOL'
    # We have to configure the secret key which could be a random key used to encrypt your cookies 
    # and save send them to the browser
    # Normally in production we would never want to share our secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # The database URI that should be used for the connection.

    db.init_app(app)
    # Initalizing our database with the app
    from .views import views
    # Importing the variable views


    app.register_blueprint(views, url_prefix='/')
    # url prefix so url for homepage would be https://127.0.0.1:5000/


    # Register auth blueprint
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User
    create_db(app)

    # Managing how the user is logged in
    login_manager = LoginManager()
    # Creating the application
    #This is the file where the app would redirect us if were not logged in
    login_manager.login_view = 'views.home'
    login_manager.init_app(app)

    # This callback is used to reload the user object from the user ID stored in the session.
    # Telling the app how to load a user.
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app


def create_db(app):
    # Checks if database exists, if not it creates it
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database created.')