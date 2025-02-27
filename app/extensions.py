from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Create an instance and assign it
db = SQLAlchemy()

#Create an instance and assign it
migrate = Migrate()

#Configure the db class