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
    result = db.engine.execute(execution_str)
    for item in result:
        return true
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
    execution_str = "SELECT B.beername, size, number, stylename, store, price, rating, pictureurl FROM \"Beer\" AS B, \"ItemListing\" AS L WHERE B.beername=L.beername AND B.beername=\'" + beer + "\' ORDER BY price ASC;"
    print execution_str
    result = db.engine.execute(execution_str)
    return result

def add_beer(beer, amt, num, price, store):
	execution_str_beer = "INSERT INTO \"Beer\" (beername) VALUES (\'" + beer + "\');"
	try:
		print execution_str_beer
		db.engine.execute(execution_str)
	except Exception as ex:
		print ex
#	execution_str_item = "INSERT INTO \"ItemListing\" (beername, number, size, store, price) VALUES (\'" + str(beer) + "\', \'" + str(num) + "\', \'" + str(amt) + "\', \'" + str(price) + "\', \'" + str(store) + "\');"
#	try:
#		db.engine.execute(execution_str)
#		print execution_str_item
#	except DatabaseError, e:
#		print str(e)
