import requests
import os

SHEETY_BEARER_TOKEN = os.getenv('SHEETY_BEARER_TOKEN')

sheety_endpoint = 'https://api.sheety.co/9afce188724a8a0b754c9fab810ae810/flightDeals/prices'

sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {SHEETY_BEARER_TOKEN}',
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.url = sheety_endpoint
        self.headers = sheety_headers

    def get_sheet_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        data = response.json()
        return data

    def update_sheet_data(self, row, parameters):
        response = requests.put(url=f'{self.url}/{row}', headers=self.headers, json=parameters)
        print(response.status_code)
