__author__ = 'Aaron'
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

def create_user(email_address, password):
    execution_str = "INSERT INTO \"User\" (email, password) VALUES (\'" + email_address + "\', \'" + password + "\');"
    db.engine.execute(execution_str)

def list_users():
    result = db.engine.execute("SELECT * FROM \"User\";")
    return result

def verify_user(email_address, password):
    execution_str = "SELECT * FROM \"User\" WHERE email=\'" + email_address +"\' AND password=\'" + password + "\';"
    try:
        result = db.engine.execute(execution_str)
        for item in result:
            return true
        return false
    except:
        return false

def change_password(email_address, new_password):
    execution_str = "UPDATE \"User\" SET password=\'" + new_password + "\' WHERE email=\'" + email_address + "\';"
    db.engine.execute(execution_str)

def delete_user_db(email_address):
    execution_str = "DELETE FROM \"User\" WHERE email=\'" + email_address + "\';"
    db.engine.execute(execution_str)

def search_results(term):
    execution_str = "SELECT B.beername, rating, pictureurl, MIN(price) FROM \"Beer\" AS B, \"ItemListing\" AS L WHERE B.beername=L.beername AND (UPPER(B.beername) LIKE UPPER(\'%%" + term + "%%\') OR UPPER(B.stylename) LIKE UPPER(\'%%" + term + "%%\')) GROUP BY B.beername;"
    result = db.engine.execute(execution_str)
    return result

def get_details(beer):
    execution_str = "SELECT B.beername, size, number, stylename, store, price, rating, pictureurl FROM \"Beer\" AS B, \"ItemListing\" AS L WHERE B.beername=L.beername AND B.beername=\'" + beer + "\' ORDER BY B.beername, number*size/price DESC;"
    #print execution_str
    result = db.engine.execute(execution_str)
    return result

def add_beer(beer, pic, amt, num, price, store):
    execution_str_beer = "INSERT INTO \"Beer\" (beername, pictureurl) VALUES (\'" + beer + "\', \'" + pic + "\');"
    try:
        db.engine.execute(execution_str_beer)
    except Exception as ex:
        print "error adding beer"
    execution_str_item = "INSERT INTO \"ItemListing\" (beername, number, size, store, price) VALUES (\'" + str(beer) + "\', " + str(num) + ", " + str(amt) + ", \'" + str(store) + "\', " + str(price) + ");"
    execution_str_upd = "UPDATE \"ItemListing\" SET price=" + str(price) + " WHERE beername=\'" + beer + "\' AND number=" + str(num) +" AND size=" + str(amt) + " AND store=\'" + str(store) + "\';"
    execution_str_upd_rate = "UPDATE \"Rating\" SET bestValue=(SELECT MAX(number*size/price) FROM \"ItemListing\" AS L WHERE L.beername=\'" + beer + "\' GROUP BY L.beername) WHERE beername=\'" + beer + "\' AND bestValue > (SELECT MAX(number*size/price) FROM \"ItemListing\" AS L WHERE L.beername=\'" + beer + "\' GROUP BY L.beername);"
    try:
        db.engine.execute(execution_str_item)
        db.engine.execute(execution_str_upd_rate)
    except Exception as ex:
        print ex
        try:
            db.engine.execute(execution_str_upd)
            db.engine.execute(execution_str_upd_rate)
        except Exception as ex:
            print ex

def rate_beer(email_address, beer, rating):
    execution_str = "INSERT INTO \"Rating\" (email, beername, rating, bestValue) VALUES (\'" + email_address + "\', \'" + beer + "\', " + str(rating) + ", (SELECT MAX(number*size/price) FROM \"ItemListing\" WHERE beername=\'" + beer + "\' GROUP BY beername));"
    print execution_str
    execution_str_upd = "UPDATE \"Rating\" SET rating=" + str(rating) + " WHERE beername=\'" + beer + "\' AND email=\'" + email_address + "\';"
    print execution_str_upd
    try:
        db.engine.execute(execution_str)
    except:
        try:
            db.engine.execute(execution_str_upd)
        except:
            print execution_str

def get_beers():
    execution_str = "SELECT beername FROM \"Beer\";"
    result = db.engine.execute(execution_str)
    return result

def get_beers_rating():
    execution_str = "SELECT beername, rating FROM \"Beer\";"
    result = db.engine.execute(execution_str)
    return result

def get_notify_info():
    execution_str = "SELECT DISTINCT ON(R.beername) R.beername, price, size, number, store, email, L.number*L.size/L.price FROM \"ItemListing\" AS L, \"Rating\" AS R WHERE L.beername = R.beername AND R.bestValue+0.001 < (L.number*L.size/L.price) AND R.rating >= 4 ORDER BY R.beername, (L.number*L.size/L.price) DESC;"
    result = db.engine.execute(execution_str)
    return result

def add_beer_info(beer, rating, style, brewer):
    print beer, rating, style, brewer
    execution_str = "UPDATE \"Beer\" SET stylename=\'" + str(style) + "\', brewername=\'" + str(brewer) + "\', rating=\'" + str(rating) + "\' WHERE beername=\'" + beer + "\';"
    try:
        db.engine.execute(execution_str)
    except Exception as ex:
        print ex

def update_best_value(email_address, beer, value):
    execution_str = "UPDATE \"Rating\" SET bestValue=" + str(value) + " WHERE beername=\'" + str(beer) + "\' AND email=\'" + email_address + "\';"
    try:
        db.engine.execute(execution_str)
    except Exception as ex:
        print ex

def get_predicted_rating(email_address, beer):
    execution_str_avg = "SELECT AVG(R.rating) FROM \"Rating\" AS R, \"Beer\" AS B WHERE R.beername = B.beername AND R.email=\'" + email_address + "\' AND B.stylename = (SELECT stylename FROM \"Beer\" WHERE beername=\'" + beer + "\') GROUP BY B.stylename;"
    avg = db.engine.execute(execution_str_avg)
    execution_str_count = "SELECT COUNT(R.rating) FROM \"Rating\" AS R, \"Beer\" AS B WHERE R.beername = B.beername AND R.email=\'" + email_address + "\' AND B.stylename = (SELECT stylename FROM \"Beer\" WHERE beername=\'" + beer + "\') GROUP BY B.stylename;"
    number_ratings = db.engine.execute(execution_str_count)
    execution_str_rat = "SELECT rating FROM \"Beer\" WHERE beername=\'" + beer + "\';"
    default_rating = db.engine.execute(execution_str_rat)
    for d in default_rating:
        for c in number_ratings:
            for a in avg:
                if c[0] == 1:
                    return 0.25 * float(a[0]) + 0.75 * float(d[0])
                if c[0] == 2:
                    return 0.33 * float(a[0]) + 0.67 * float(d[0])
                if c[0] == 3:
                    return 0.5 * float(a[0]) + 0.5 * float(d[0])
                if c[0] == 4:
                    return 0.67 * float(a[0]) + 0.33 * float(d[0])
                if c[0] >= 5:
                    return 0.75 * float(a[0]) + 0.25 * float(d[0])
        return d[0]

def get_favorite_style(email_address):
    execution_str = "SELECT DISTINCT ON(s.style) s.style, avg_rating FROM (SELECT B.stylename AS style, AVG(R.rating) AS avg_rating FROM \"Beer\" AS B, \"Rating\" AS R WHERE B.beername=R.beername AND R.email=\'" + email_address + "\' GROUP BY B. stylename) AS s ORDER BY s.style, avg_rating DESC;"
    result = db.engine.execute(execution_str)
    for r in result:
        return r[0]
    return "empty"

def get_beers_by_style(style):
    execution_str = "SELECT beername FROM \"Beer\" WHERE stylename=\'" + style + "\';"
    result = db.engine.execute(execution_str)
    return result
