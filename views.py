__author__ = 'Aaron'

from app import app
from models import *
from flask import render_template, request, session, redirect, url_for

@app.route("/", methods=["GET","POST"])
def home_page():
    if 'email' in session:
        return redirect(url_for('settings_page'))
    if request.method == 'POST':
        email = request.form['loginEmail']
        password = request.form['loginPass']
        if verify_user(email, password) == true:
            session['email'] = email
            return redirect(url_for('settings_page'))
    return render_template('index.html')

@app.route("/signup", methods=["GET","POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if '@' in email and password == request.form['password_confirm']:
            create_user(email, password)
    return render_template('signup.html')

@app.route("/settings", methods=["GET","POST"])
def settings_page():
    if 'email' not in session:
        return redirect(url_for('home_page'))
    if request.method == 'POST':
        email = session['email']
        password = request.form['old_password']
        new_password = request.form['new_password']
        if verify_user(email, password) == true and new_password == request.form['password_confirm']:
            change_password(email, new_password)
    return render_template('settings.html')

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('home_page'))

@app.route("/delete_user")
def delete_user():
    delete_user_db(session['email'])
    session.pop('email', None)
    return redirect(url_for('home_page'))

