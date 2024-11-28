import datetime as dt
import os
import smtplib
from random import choice

import pandas as pd

MY_EMAIL = 'glesman.python@gmail.com'
PASSWORD = 'zurt hutb uosr luos'
YAHOO_EMAIL = 'pglesman@yahoo.com'

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# 2. Check if today matches a birthday in the birthdays.csv
birthdays_data = pd.DataFrame(pd.read_csv('birthdays.csv'))
birthdays_data_dict = birthdays_data.to_dict(orient='records')

for birthday in birthdays_data_dict:
    if birthday['month'] == month and birthday['day'] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        random_letter = choice(os.listdir('letter_templates'))

        with open(f'letter_templates/{random_letter}', 'r') as file:
            letter = file.read()
            new_letter = letter.replace('[NAME]', birthday['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday['email'],
                msg=f'Subject:Birthday wishes!\n\n{new_letter}'
            )
