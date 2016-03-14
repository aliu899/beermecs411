__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy


def create_user(email_address, password):
    db.engine.execute("INSERT INTO User (email, password) VALUES (?, ?)", (email_address, password))