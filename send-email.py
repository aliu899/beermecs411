#import smtplib
import models

def email(notification):
    body = "We found a good deal on one of your favorite beers that might interest you.  " + str(notification[4]) + " is selling a " + str(notification[2]) + "oz " + str(notification[3]) + "pk of " + str(notification[0]) + " for $" + str(notification[1]) + "!"
    print body
	update_best_value(notification[5], notification[0], notification[6])

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

