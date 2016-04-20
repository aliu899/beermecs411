import smtplib
from email.mime.text import MIMEText
from models import get_notify_info, update_best_value

def email(notification):
    msg = MIMEText("We found a good deal on one of your favorite beers that might interest you.  " + str(notification[4]) + " is selling a " + str(notification[2]) + "oz " + str(notification[3]) + "pk of " + str(notification[0]) + " for $" + str(notification[1]) + "!")
    update_best_value(notification[5], notification[0], notification[6])
    msg['Subject'] = Beer Me Price Update
    msg['To'] = notification[5]
    msg['From'] = 'beer.me.application@gmail.com'

	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()

	mail.starttls()
	mail.login('beer.me.application@gmail.com','beerme411')
	mail.sendmail('beer.me.application@gmail.com', notification[5], msg.as_string())
	mail.close()

notifications = get_notify_info()
for n in notifications:
    email(n)

