__author__ = 'Aaron'

from app import app
from models import *
from flask import render_template, request

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/signup.html")
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if '@' in email and password == request.form['password_confirm']:
            create_user(email, password)
    return render_template('signup.html')

