__author__ = 'Aaron'

from app import app
from flask import render_template

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/signup.html")
def sign_up():
    return render_template('signup.html')

