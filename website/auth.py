# This will handle the authentication information of our python project
# from flask import Blueprint
# # Setting up a blueprint for our application
# views = Blueprint('views', __name__)
# create routes that are login logout and signup

from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template("signup.html")


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<h1>Logged Out</h1>"
