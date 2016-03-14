__author__ = 'Aaron'
from app import db
from sqlalchemy import text


def create_user(email_address, password):
    print "start"
    db.session.execute(text("INSERT INTO User (email, password) VALUES (:email, :password)"), {"email": email_address, "password": password})
    print "end"

def list_users():
    print "start1"
    result = db.session.execute("SELECT * FROM User")
    print result
    print "end1"