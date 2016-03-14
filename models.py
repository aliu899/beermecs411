__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy

def create_user(email_address, password):
    db.engine.execute("INSERT INTO User VALUES ('abc@123.com', 'password')")

def list_users():
    result = db.engine.execute("SELECT * FOM User")
    return result
