from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(50), unique=True, nullable= False)
    password = db.Column(db.String(200), nullable= False)
    email = db.Column(db.String(50), unique= True, nullable= False)
    role = db.Column(db.String(20), nullable= False)
    