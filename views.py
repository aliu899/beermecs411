__author__ = 'Aaron'

from app import app
from flask import render_template

@app.route("/")
def hello():
    return render_template('index.html')
