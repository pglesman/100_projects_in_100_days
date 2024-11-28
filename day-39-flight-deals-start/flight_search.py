# https://developers.amadeus.com/my-apps/Flight%20Deals?userId=patryk.glesman86@gmail.com

import os

from amadeus import Client, ResponseError
from dotenv import load_dotenv

load_dotenv()

AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')
AMADEUS_BEARER_TOKEN = os.getenv('AMADEUS_BEARER_TOKEN')

AMADEUS_ENDPOINT = 'https://test.api.amadeus.com/v1'
AMADEUS_AUTH_ENDPOINT = f'{AMADEUS_ENDPOINT}/security/oauth2/token'
AMADEUS_FLIGHT_SEARCH_ENDPOINT = f'{AMADEUS_ENDPOINT}/shopping/flight-destinations'
AMADEUS_CITY_SEARCH_ENDPOINT = f'{AMADEUS_ENDPOINT}/reference-data/locations/cities'

ORIGIN_CODE = 'LON'

amadeus = Client(
    client_id=AMADEUS_API_KEY,
    client_secret=AMADEUS_API_SECRET,
)

amadeus_headers = {
    'Authorization': f'Bearer {AMADEUS_BEARER_TOKEN}',
}

# TODO 1 : change everything for amadeus python SDK https://github.com/amadeus4dev/amadeus-python


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = AMADEUS_API_KEY
        self._api_secret = AMADEUS_API_SECRET
        self._token = AMADEUS_BEARER_TOKEN

    @staticmethod
    def get_iata_code(city: str):
        try:
            response = amadeus.reference_data.locations.cities.get(keyword=city)
            data = response.result
            iata_code = data['data'][0]['iataCode']
            return iata_code
        except ResponseError as error:
            print(error)
