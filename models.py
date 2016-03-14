__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

def create_user(email_address, password):
	print "insert"
	statement = "INSERT INTO User (email, password) VALUES (abc@123.com, password)"
	newstate = text(statement)
	db.engine.execute(newstate)

def list_users():
    result = db.engine.execute("SELECT * FROM User")
    return result
