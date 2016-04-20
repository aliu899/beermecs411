__author__ = 'Aaron'

from app import app
from models import *
from flask import render_template, request, session, redirect, url_for
import json

@app.route("/", methods=["GET","POST"])
def home_page():
    if 'email' in session:
        return redirect(url_for('user_dashboard'))
    if request.method == 'POST':
        email = request.form['loginEmail']
        password = request.form['loginPass']
        if verify_user(email, password) == true:
            session['email'] = email
            return redirect(url_for('user_dashboard'))
#    count = 0
#    try:
#        with open('output.json', 'r') as dataFile:
#            beer_dir = json.loads(dataFile.read())
#            beer_list = get_beers()
#            print "rating"
#            for beer in beer_list:
#                print beer[0].lower()
#                if beer[0].lower() in beer_dir.keys():
#                    print beer[0].lower()
#                    add_beer_info(beer[0], beer_dir[beer[0].lower()]['rAvg'], beer_dir[beer[0].lower()]['style'], beer_dir[beer[0].lower()]['brewery'].replace("'",""))
#                for key in beer_dir.keys():
#                    if beer[0].lower() in key.replace("'", ""):
#                       print beer[0].lower() + " - - - " + key
#                        count += 1
#                        print count
#                        break
#                    if key.replace("'","") in beer[0].lower():
#                        print beer[0], beer_dir[key]['rAvg'], beer_dir[key]['style'].replace("'",""), beer_dir[key]['brewery'].replace("'","")
#                        add_beer_info(beer[0], beer_dir[key]['rAvg'], beer_dir[key]['styl    e'].replace("'",""), beer_dir[key]['brewery'].replace("'",""))
#                        print "beer3"
#    except TypeError as e:
#        print e
    return render_template('index.html')

@app.route("/signup", methods=["GET","POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if '@' in email and password == request.form['password_confirm']:
            create_user(email, password)
            session['email'] = email
            return redirect(url_for('user_dashboard'))
    return render_template('signup.html')

@app.route("/dashboard", methods=["GET", "POST"])
def user_dashboard():
    if 'email' not in session:
        return redirect(url_for('home_page'))
    search_hits = []
    if request.method == 'POST':
        search_hits = search_results(request.form['x'])
    favorite_style = get_favorite_style(session['email'])
    if (favorite_style != "empty"):
        beers = get_beers_by_style(favorite_style)
        beers_predicted = []
        for beer in beers:
            predicted = get_predicted_rating(session['email'], beer[0])
            beers_predicted.append((beer[0], predicted))
        favorite_style = 'Because you liked ' + favorite_style + ' ...'

    else:
        beers = get_beers_rating()
        beers_predicted = []
        for beer in beers:
            beers_predicted.append((beer[0], beer[1]))
        favorite_style = 'Recommended for you'
    sorted(beers_predicted, key=lambda rating: rating[1])
    top3 = [beers_predicted[0], beers_predicted[1], beers_predicted[2]]
    return render_template('query.html', results = search_hits, based_on = favorite_style, recommended = top3)

@app.route("/detail/<beer_name>", methods=["GET", "POST"])
def detailed_page(beer_name):
    if 'email' not in session:
        return redirect(url_for('home_page'))
    beer_result = get_details(beer_name)
    predictive_rating = get_predicted_rating(session['email'], beer_name)
    remaining = []
    i = 0
    for item in beer_result:
        if i == 0:
            first = item
        else:
            remaining.append(item)
        i += 1
    if request.method == 'POST':
        rate_beer(session['email'], beer_name, request.form['rating'])
    return render_template('detailed-result.html', lowest = first, remaining = remaining, predicted = predictive_rating)


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

