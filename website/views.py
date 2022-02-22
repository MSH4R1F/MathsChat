# This will store all the main views or URL endpoints for the website.

from flask import Blueprint, render_template,request, redirect
# Setting up a blueprint for our application
views = Blueprint('views', __name__)


# Importing the database
from . import db
from .models import Rooms

from flask.helpers import url_for
from flask_login import login_required,current_user
# Defining the route for my homepage
# This is a decorator that would run all the functions below it
@views.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return render_template("index.html",user=current_user)


@views.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    # Get the join code from home.html
    if request.method == "POST":
        print(len(request.form))
        if len(request.form) != 3:
            code = request.form["code"]
            return redirect('/chat/'+code)
        else:
            code = request.form["create-code"]
            name = request.form["name"]
            description = request.form["description"]
            print(description)
            # Creating our room and adding it to our database
            new_room = Rooms(code,name,description)
            db.session.add(new_room)
            db.session.commit() 
            return redirect('/chat/'+code)
    return render_template("home.html",user=current_user)