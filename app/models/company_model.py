from app.extensions import db
from datetime import datetime




class Company(db.model):
    #Adding the name of the table
    __tablename__  = 'company'

    # Adding a constructor
    
    id = db.column(db.Integer, primary_key = True, nullable = False)
    origin = db.column(db.String(20), nullable = False)
    description = db.column(db.String(200), nullable = False)
    created_at= db.column(db.Datetime, defalut = datetime.now())
    updated_at = db.column(db.Datetime, default = datetime.now())
    

    def __init__(self,name, id, origin, description,created_at, updated_at):
        self.name = name
        self.id = id
        self.origin = origin
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        

 