# This __init__ file will make the website a Python package. 
# This means we can import this file and everything here would run automatically


from flask import Flask

def create_app():
    app = Flask(__name__)
    # Initializing the Flask App
    # __name__ denotes the name of the file that was ran
    app.config['SECRET_KEY'] = 'SHARIFISCOOL'
    # We have to configure the secret key which could be a random key used to encrypt your cookies 
    # and save send them to the browser
    # Normally in production we would never want to share our secret key

    from .views import views
    # Importing the variable views

    app.register_blueprint(views, url_prefix='/')
    # url prefix so url for homepage would be https://127.0.0.1:5000/


    # Note to self register auth blueprint
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    return app

