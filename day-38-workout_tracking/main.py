# https://dashboard.sheety.co/
# https://developer.nutritionix.com/
# https://replit.com/~

from datetime import datetime
import requests
import os

now = datetime.now()
year_now = now.strftime('%Y')
date_now = now.strftime('%d/%m/%Y')
time_now = now.strftime('%H:%M:%S')

APP_ID = os.environ.get('APP_ID', 'APP_ID does not exist')
API_KEY = os.environ.get('API_KEY', 'APP_KEY does not exist')
SHEETY_BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN', 'SHEETY_BEARER_TOKEN does not exist')
WEIGHT = 80
HEIGHT = 180
AGE = int(year_now) - 1986
GENDER = 'male'

nutrition_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/9afce188724a8a0b754c9fab810ae810/workoutTracking/arkusz1'

nut_headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

nut_parameters = {
    'query': input('Tell me which exercise you did: '),
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE,
    'gender': GENDER,
}

sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {SHEETY_BEARER_TOKEN}',
}

response = requests.post(url=nutrition_endpoint, json=nut_parameters, headers=nut_headers)
data = response.json()

for sport in data['exercises']:
    exercise: str = sport['name'].title()
    duration = sport['duration_min']
    calories = sport['nf_calories']

    sheety_parameters = {
        'arkusz1': {
            'date': date_now,
            'time': time_now,
            'exercise': exercise,
            'duration': duration,
            'calories': calories,
        }
    }

    adding_rows = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
    print(sheety_parameters)
