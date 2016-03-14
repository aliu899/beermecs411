__author__ = 'Aaron'
from app import db
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


def create_user(email_address, password):
    eng = create_engine()
    db.session.execute("INSERT INTO User (email, password) VALUES (?, ?)", (email_address, password))

def list_users():
    result = db.engine.execute("SELECT * FROM User")
    print result