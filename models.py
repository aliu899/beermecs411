__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy

def create_user(email_address, password):
	print("inserting")
    db.engine.execute("INSERT INTO User (email, password) VALUES (\'?\', \'?\')", email, password)

def list_users():
	print("listing")
    result = db.engine.execute("SELECT * FOM User")
    return result
