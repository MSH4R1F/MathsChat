# This will store all the main views or URL endpoints for the website.

from flask import Blueprint, render_template,request, redirect
# Setting up a blueprint for our application
views = Blueprint('views', __name__)

from flask.helpers import url_for
from flask_login import login_required,current_user
# Defining the route for my homepage
# This is a decorator that would run all the functions below it
@views.route('/')
def index():
    return render_template("index.html",user=current_user)


@views.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    # Get the join code from home.html
    if request.method == "POST":
        code = request.form["code"]
        return redirect('/chat/'+code)
    return render_template("home.html",user=current_user)