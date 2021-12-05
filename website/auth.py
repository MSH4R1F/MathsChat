# This will handle the authentication information of our python project
# from flask import Blueprint
# # Setting up a blueprint for our application
# views = Blueprint('views', __name__)
# create routes that are login logout and signup

from flask import Blueprint, render_template, request, flash,redirect
# Importing Blueprint to help us create reusable instances of my application.
# Importing render_template to render our html template
# Importing request to parse how form requests
# Importing flash to return error and success messages
import re


from flask.helpers import url_for
# Import re for validation

#Import our database 
from . import db

# Import our database models such as User
from .models import *
auth = Blueprint('auth', __name__)
# Setting up a blueprint for our authentication routes, eg signup and login

# Setting up routes for signup and login with methods GET and POST as we would be sending data to our backend
# Importing hashlib for password
import hashlib

class HashPassword:
    def __init__(self,value):
        self.value = value
        # Value stores the value of the password.
    def Hash(self):
        encoded_info = self.value.encode()
        # encodes the string, using UTF-8
        hasher = hashlib.sha256(encoded_info)
        # Hashes the password
        hex_dig = hasher.hexdigest()
        # Returns the encoded data in hexadecimal format.
        return hex_dig
    # Method takes in both user password and database passwords and return True if they are the same
    def checkHashes(self, hashed_password):
        user = self.Hash()
        print(user,hashed_password)
        if user == hashed_password:
            return True
        else:
            return False
        




@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        # First check if the request method is POST otherwise even if there was no data sent it would run this 
        username = request.form["uname"]
        password = request.form["pwd"]
        email = request.form["email"]
        # Extracting username,password,email
        # Checking if exising username or email
        user_email = User.query.filter_by(email = email).first()
        user_username = User.query.filter_by(username = username).first()
        # Check if theres anything in database with those usernames or emails
        if user_email:
            flash('Already used email', category = 'error')
        elif user_username:
            flash('Already used username', category = 'error')
        elif len(email) <= 4:
            # Validating email is longer than 4
            flash('Email must be longer than 4 characters.', category = 'error')
        elif len(password) < 8:
            # Validation password length is longer than 8
            flash('Password must be longer than 8 characters.', category = 'error')
        elif not bool(re.search(r'\d',password)):
            # Validation password must contain a number
            flash('Password must contain at least one number', category = 'error')
        elif not any(c.isupper() for c in password):
            # Validation checking that the password contains an uppercase letter
            flash('Password must contain at least one uppercase letter', category= 'error')
        elif not any(c.islower() for c in password):
            flash('Password must contain at least one lowercase letter', category= 'error')
        elif not any(not c.isalnum() for c in password):
            # Checking that password contains at least one symbol
            flash('Password must contain at leats one symbol', category = 'error')
        else:
            hash_class = HashPassword(password)
            hashed_password = hash_class.Hash()
            print(hashed_password)

            # Hash our password
            new_user = User(email = email, username = username,password = hashed_password)
            db.session.add(new_user)
            # issue an INSERT statement for the database
            db.session.commit()
            # Commits it so the user has an id
            flash('Account created', category = 'success')
            return redirect(url_for('views.home'))
            


        print(username,password,email)
    # Returning the signup html page
    return render_template("signup.html")
 
@auth.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['uname']
        password = request.form['pwd']
        print(username, password)


        user = User.query.filter_by(username=username).first()
        print(user.username,user.password)
        UserPasswordClass = HashPassword(password)
        if user:
            if UserPasswordClass.checkHashes(user.password):
                flash('Logged in successfully! :)', category = 'success')
                # Redirects user to homepage.
                return redirect(url_for('views.home')) 
            else:
                flash('Incorrect password, Try Again :(', category = 'error')
        else:
            flash('Unknown User :0. Signup now', category = 'error')


    return render_template("login.html")
 
 
@auth.route("/logout")
def logout():
    return "<h1>Logged Out</h1>"
