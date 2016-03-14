__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

def create_user(email_address, password):
	txt = "INSERT INTO User (email, password) VALUES (" + email_address + ", " + password + ")"
	print(txt)

	sql = text(txt)
    db.engine.execute("INSERT INTO User (email, password) VALUES (?, ?)", (email_address, password))

def list_users():
	print("listing")
    result = db.engine.execute("SELECT * FOM User")
    return result
