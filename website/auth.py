# This will handle the authentication information of our python project
# from flask import Blueprint
# # Setting up a blueprint for our application
# views = Blueprint('views', __name__)
# create routes that are login logout and signup

from flask import Blueprint, render_template, request, flash
# Importing Blueprint to help us create reusable instances of my application.
# Importing render_template to render our html template
# Importing request to parse how form requests
# Importing flash to return error and success messages
import re
# Import re for validation
 
auth = Blueprint('auth', __name__)
# Setting up a blueprint for our authentication routes, eg signup and login

# Setting up routes for signup and login with methods GET and POST as we would be sending data to our backend
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        # First check if the request method is POST otherwise even if there was no data sent it would run this 
        username = request.form["uname"]
        password = request.form["pwd"]
        email = request.form["email"]
        # Extracting username,password,email
        if len(email) <= 4:
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
            flash('Account created', category = 'success')
            


        print(username,password,email)
    # Returning the signup html page
    return render_template("signup.html")
 
@auth.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['uname']
        password = request.form['pwd']

        print(username, password)
    return render_template("login.html")
 
 
@auth.route("/logout")
def logout():
    return "<h1>Logged Out</h1>"
