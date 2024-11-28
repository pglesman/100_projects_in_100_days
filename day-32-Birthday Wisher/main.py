import datetime as dt
import smtplib
from random import choice

MY_EMAIL = 'glesman.python@gmail.com'
PASSWORD = 'zurt hutb uosr luos'
YAHOO_EMAIL = 'pglesman@yahoo.com'

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
# print(now)
# print(year)
# print(month)
# print(day_of_the_week)  # week start from '0' -> Monday

day_of_birth = dt.datetime(year=1986, month=5, day=31)
# print(day_of_birth)

if day_of_the_week == 3:
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
        quote_of_the_day = choice(quotes)
        print(quote_of_the_day)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=YAHOO_EMAIL,
            msg=f'Subject:Quote of the day\n\n{quote_of_the_day}'
        )

