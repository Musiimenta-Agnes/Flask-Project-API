
# Create a new application function
# First import the module Flask
from flask import Flask
#Import the db object
from app.extensions import db, migrate
#import migrate





def create_app():

    app = Flask(__name__) # Creat the app name and path in the parameter name
      # Access the app
    app.config.from_object('config.Config')
    db.init_app(app) # Instantiate it
    migrate.init_app(app, db)
  
   

#Register models from the application file.
    from app.models.author_model import Author
    from app.models.book_model import Book
    from app.models.company_model import Company

    @app.route('/')  # Add a route and a decorator and the route must be on top of the decorator.
    def index():
        return 'Hello'
    


    return app  # Return the application instance
# Then test whether the application is running.



                     


