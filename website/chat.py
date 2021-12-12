from flask import Blueprint, render_template,request

# Setting up a blueprint for chats
chat = Blueprint('chats', __name__)


from flask_login import login_required,current_user

# When the join code is not given return chat.html
@chat.route('/')
@login_required
def chat_home():
    return render_template("chat.html")


# Making a route for our join codes.
@chat.route('/<id>')
@login_required
def chat_room(id):
    return render_template("chat_room.html", user=current_user,id=id)