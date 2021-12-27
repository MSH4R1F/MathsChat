from flask import Blueprint, render_template,request, session   

# Setting up a blueprint for chats
chat = Blueprint('chat', __name__)


# Importing datetime to send time of messages
from datetime import datetime

from . import socketio
from flask_login import login_required,current_user

# Importing all the modules required for socketIO on my chat platform
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

# When the join code is not given return chat.html


@chat.route('/')
@login_required
def chat_home():
    return render_template("chat.html")


# Making a route for our join codes.
@chat.route('/<id>')
@login_required
def chat_room(id):
    # Adding parametrs the current user and the id or the room code.
    session['room'] = id
    session['name'] = current_user.username
    print(session)
    return render_template("chat_room.html", name=current_user.username,room = id)


@socketio.event
def my_event(message):
    """
    Test session dictionary
    Using this to keep count of all the sessions, we are just incremeneting session[receive_count]
    """
    session['receive_count'] = session.get('receive_count',0+1)
    emit('my_response', {'data': message['data'],
                        'count': session['receive_count']}, broadcast = True)



@socketio.on('joined')
def joined(message):
    """
    Sent by clients when they enter the room.
    A status message has to be broadcasted to the entire room
    """
    room = session.get('room')
    # Get room code
    join_room(room)
    now = datetime.now()
    current_time  = now.strftime("%H:%M:%S")
    emit('status', {'msg': session.get('name') + 'has joined!', 'time' : current_time}, room=room)
    
    

@socketio.on('text')
def text(message):
    """Sent by the client when the user sends a message
        This is then sent to all the people in the room
    """
    print(message)
    room = session.get('room')
    
    now = datetime.now()
    current_time  = now.strftime("%H:%M:%S")
    
    # Emit the message with name
    # Send to sender only
    emit('message', {'msg':message['msg'], 'name': session.get('name'), 'time': current_time, 'sender': 'false'}, room = room,include_self= False)
    emit('message', {'msg':message['msg'], 'name': session.get('name'), 'time': current_time, 'sender': 'true'}, broadcast = False)


@socketio.on('leave')
def leave(message):
    """Sent by clients when the user leaves the room
        A status message is sent to all users.
    """
    room = session.get('room')
    leave_room(room)
    now = datetime.now()
    current_time  = now.strftime("%H:%M:%S")
    # Emit message to leave room to all users.
    emit('status', {'msg': session.get('name') + 'has left!', 'time': current_time}, room =room)
  

