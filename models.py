__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy

def create_user(email_address, password):
	txt = "INSERT INTO User (email, password) VALUES (\'" + email + "\', \'"  + password + "\')"
    db.engine.execute(txt)

def list_users():
    result = db.engine.execute("SELECT * FOM User")
    return result
