__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import text

def create_user(email_address, password):
	txt = "INSERT INTO User (email, password) VALUES (\'" + email + "\', \'"  + password + "\')"
	#sql = text(txt)
    db.engine.execute(txt)

def list_users():
    result = db.engine.execute("SELECT * FOM User")
    return result
