# This python file will store our database models
from . import db
# Importing db app from init file

from flask_login import UserMixin
# a custom class that will give our user object some specific things in Flask

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # This is a primary key for our entity
    email = db.Column(db.String(160),unique = True)
    # Our email is a field where the maximum length is 160 and must be unique
    username = db.Column(db.String(100),unique = True)
    password = db.Column(db.String(160))



