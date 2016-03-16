__author__ = 'Aaron'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.secret_key = 'CS411BEERME'
db = SQLAlchemy(app)
