from app.extensions import db
from datetime import datetime  # The extension for updating the date
class Author(db.Model):
        __tablename__ = 'authors'
   

        id = db.Column(db.Integer, primary_key=True, nullable = False)
        first_name = db.Column(db.String(),nullabel = False)
        last_name = db.Column(db.String(),nullable = False, unique = True)
        author_contact = db.Column(db.String(), nullable = False)
        email_addresss = db.Column(db.String(),nullable = False, unique = True)
        password = db.Column(db.String(), nullable = False, unique = True)
        image = db.Column(db.String(), nullable = True)
        biography = db.Column(db.String(), nullable = False)
        created_at = db.Column(db.DateTime,default = datetime.now())   # This is a time stamp
        updated_at = db.Column(db.DateTime,onupdate = datetime.now())  # This is a time stamp
        
        def __init__(self,id,first_name,last_name, author_contact,email_addresss, password, image, biography, created_at,updated_at ):
         self.id = id
         self.first_name = first_name
         self.last_name = last_name
         self.author_contact = author_contact
         self.email_addresss = email_addresss
         self.password = password
         self.image = image
         self.biography = biography
         self.created_at = created_at
         self.updated_at = updated_at


         
              
        