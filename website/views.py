# This will store all the main views or URL endpoints for the website.

from flask import Blueprint, render_template
# Setting up a blueprint for our application
views = Blueprint('views', __name__)

## Note to self, do the same for auth.py

# Defining the route for my homepage
# This is a decorator that would run all the functions below it
@views.route('/')
def home():
    return render_template("index.html")