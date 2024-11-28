# https://openweathermap.org/current#data

import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

LUBLIN_LAT = 41.878113  # # Longitude where it rains now
# LUBLIN_LAT = 49.492590  # Home latitude
LUBLIN_LONG = -87.629799  # Longitude where it rains now
# LUBLIN_LONG = 0.106500  # Home longitude

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
YAHOO_EMAIL = os.environ["YAHOO_EMAIL"]

OPEN_WEATHER_API_KEY = os.environ["OPEN_WEATHER_API_KEY"]
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

weather_parameters = {
    'lat': LUBLIN_LAT,
    'lon': LUBLIN_LONG,
    'appid': OPEN_WEATHER_API_KEY,
    'units': 'metric',
    'cnt': 4,
}

# Twilio account patryk.glesman86@gmail.com
TWILIO_RECOVERY_CODE = os.environ["TWILIO_RECOVERY_CODE"]
twilio_account_sid = os.environ["twilio_account_sid"]
twilio_auth_token = os.environ["twilio_auth_token"]
client = Client(twilio_account_sid, twilio_auth_token)

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain: bool = False

for weather_cond in weather_data['list']:
    if weather_cond['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+48664993575"
    )
    print(message.status)
else:
    print('There is no need for umbrella.')
