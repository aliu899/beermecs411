#import smtplib
from models import get_notify_info

def email(notification):
    print notification

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

