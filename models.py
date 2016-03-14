__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

def create_user(email_address, password):
	print "insert"

def list_users():
    result = db.engine.execute("SELECT * FROM \"User\";")
    return result
