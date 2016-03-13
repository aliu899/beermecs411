__author__ = 'Aaron'

from app import app
from flask import render_template, request
from models import *

@app.route("/")
def hello():
    return "Hello World!!!!!!!!"
