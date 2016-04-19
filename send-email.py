#import smtplib
from models import get_notify_info

def email(notification):
    body = "We found a good deal on one of your favorite beers that might interest you.  " + notification[4] + " is selling a " + notification[2] + "oz " + notification[3] + "pk of " + notification[0] + " for $" + notification[1]
    print body

#	content = """From: Beer Me <beer.me.application@gmail.com>
#	Subject: Beer Me Price Update
#
#	We found some changes in beer prices that might interest you. """
#	mail = smtplib.SMTP('smtp.gmail.com', 587)
#	mail.ehlo()
#
#	mail.starttls()
#	mail.login('beer.me.application@gmail.com','beerme411')
#	mail.sendmail('beer.me.application@gmail.com','lauren.taylor.marshall@gmail.com', content)
#	mail.close()

notifications = get_notify_info()
for n in notifications:
    email(n)

