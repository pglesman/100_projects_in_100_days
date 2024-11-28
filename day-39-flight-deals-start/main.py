# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

import os
from datetime import datetime

from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()

tomorrow = datetime.today() + relativedelta(days=+1)
half_year = tomorrow + relativedelta(months=+6)

sheety_google_sheet = DataManager()
sheet_data: list[dict[str:str, str:str, str:int, str:int]] = sheety_google_sheet.get_sheet_data()['prices']

for destination in sheet_data:
    if destination['iataCode'] == '':
        destination['iataCode'] = FlightSearch.get_iata_code(destination['city'])
        sheety_parameters = {
            'price': {
                'iataCode': destination['iataCode'],
            }
        }
        sheety_google_sheet.update_sheet_data(destination['id'], sheety_parameters)
