
# Create a new application function
# First import the module Flask
from flask import Flask

#Import the db object
from app.extensions import db




def create_app():

    app = Flask(__name__) # Creat the app name and path in the parameter name
    db.init_app(app)



    @app.route('/')  # Add a route and a decorator and the route must be on top of the decorator.
    def index():
        return 'Hello'
    


    return app  # Return the application instance
# Then test whether the application is running.



                     


