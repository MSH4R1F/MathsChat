from website import create_app, socketio
from flask_socketio import SocketIO
# Creating an instance of our flask app
app = create_app()









# Using this to protect users from accidentally invoking the script when they don't intend to.
if __name__ == "__main__":
    socketio.run(app,debug=True)
    # Running the app in development mode will show an 
    # interactive traceback and console in the browser when there is an error. 


