# This will store all the main views or URL endpoints for the website.

from flask import Blueprint, render_template
# Setting up a blueprint for our application
views = Blueprint('views', __name__)

from flask_login import login_required,current_user
# Defining the route for my homepage
# This is a decorator that would run all the functions below it
@views.route('/')
def index():
    return render_template("index.html",user=current_user)


@views.route('/home')
@login_required
def home():
    return render_template("home.html",user=current_user)