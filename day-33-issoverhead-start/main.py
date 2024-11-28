import smtplib
from datetime import datetime

import requests

LUBLIN_LAT = 51.248509  # Your latitude
LUBLIN_LONG = 22.568493  # Your longitude

MY_EMAIL = 'glesman.python@gmail.com'
PASSWORD = 'zurt hutb uosr luos'
YAHOO_EMAIL = 'pglesman@yahoo.com'


def is_iss_above_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    latitude_ok = LUBLIN_LAT - 5 <= iss_latitude <= LUBLIN_LAT + 5
    longitude_ok = LUBLIN_LONG - 5 <= iss_longitude <= LUBLIN_LONG + 5
    return latitude_ok and longitude_ok


def is_dark_now():
    parameters = {
        "lat": LUBLIN_LAT,
        "lng": LUBLIN_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = int(datetime.now().hour)

    return hour_now >= sunset or hour_now <= sunrise


# If the ISS is close to my current position,
# and it is currently dark
if is_iss_above_me() and is_dark_now():
    # Email me to tell me to look up.
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=YAHOO_EMAIL,
            msg=f'Subject:ISS position above!\n\nYou can see an ISS above right now!'
        )
else:
    print('You can\'t see ISS right now.')

# BONUS: run the code every 60 seconds.
# As you tough, use while loop and sleep module for 60s - nothing new here.
