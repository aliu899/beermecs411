__author__ = 'Aaron'

from app import app
from models import *
from flask import render_template, request

@app.route("/", methods=["GET","POST"])
def home_page():
    if request.method == 'POST':
        email = request.form['loginEmail']
        password = request.form['loginPass']
        if verify_user(email, password) == true:
            return render_template('dashboard.html')
    return render_template('index.html')

@app.route("/signup.html", methods=["GET","POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if '@' in email and password == request.form['password_confirm']:
            create_user(email, password)
    return render_template('signup.html')

@app.route("/settings.html")
def settings_page():
    return render_template('settings.html')