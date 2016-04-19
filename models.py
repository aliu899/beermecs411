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
    try:
        db.engine.execute(execution_str_item)
    except Exception as ex:
        print ex
        try:
            db.engine.execute(execution_str_upd)
        except:
            print execution_str_upd

def rate_beer(email_address, beer, value):
    execution_str = "INSERT INTO \"Rating\" (email, beername, rating, bestValue) VALUES (\'" + email_address + "\', \'" + beer + "\', " + str(value) + ", (SELECT MAX(number*size/price) FROM \"Beer\" AS B, \"ItemListing\" AS L WHERE B.beername=L.beername AND B.beername=\'" + beer + "\' GROUP BY B.beername));"
    print execution_str
    execution_str_upd = "UPDATE \"Rating\" SET rating=" + str(value) + ", bestValue=(SELECT MAX(number*size/price) FROM \"Beer\" AS B, \"ItemListing\" AS L WHERE B.beername=L.beername AND B.beername=\'" + beer + "\' GROUP BY B.beername) WHERE beername=\'" + beer + "\' AND email=\'" + email_address + "\';"
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

def notify():
    execution_str = "SELECT * FROM \"Rating\";"

def add_beer_info(beer, rating, style, brewer):
    execution_str = "UPDATE \"Beer\" SET stylename=\'" + str(style) + "\', brewername=\'" + str(brewer) + "\', rating=\'" + str(rating) + "\' WHERE beername=\'" + beer + "\';"
