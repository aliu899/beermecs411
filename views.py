__author__ = 'Aaron'

from app import app
from models import *
from flask import render_template, request

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == 'POST':
        print "verifying"
        email = request.form['email']
        password = request.form['password']
        print email, password
        if (verify_user(email, password)):
            print "login accepted"
    return render_template('index.html')

@app.route("/signup.html", methods=["GET","POST"])
def sign_up():
    result = []
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if '@' in email and password == request.form['password_confirm']:
            create_user(email, password)
            list_users()
    return render_template('signup.html')

@app.route("/settings.html")
def settings_page():
    return render_template('settings.html')