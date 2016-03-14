__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

def create_user(email_address, password):
    print "insert"
    execution_str = "INSERT INTO \"User\" (email, password) VALUES (\'" + email_address + "\', \'" + password + "\');"
    db.engine.execute(execution_str)

def list_users():
    result = db.engine.execute("SELECT * FROM \"User\";")
    return result

def verify_user(email_address, password):
    print "verifying"
    execution_str = "SELECT * FROM \"User\" WHERE email=\'" + email_address +"\';"
    print execution_str
    result = db.engine.execute(execution_str)
    for item in result:
        print item
        if item['password'] == password:
            return true
    return false