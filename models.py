__author__ = 'Aaron'
from app import db
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


def create_user(email_address, password):
    print "start"
    db.session.execute("INSERT INTO User (email, password) VALUES (:email, :password)", {"email": email_address, "password": password})
    print "end"

def list_users():
    print "start1"
    result = db.session.execute("SELECT * FROM User")
    print result
    print "end1"