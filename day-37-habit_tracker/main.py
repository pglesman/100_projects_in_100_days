# https://pixe.la
# https://pixe.la/v1/users/pglesman/graphs/graph1.html

import requests
from datetime import datetime

USER_NAME = 'pglesman'
TOKEN = 'hakhkj1k4h21'
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Programming',
    'unit': 'hours',
    'type': 'float',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph1_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

today = datetime.now()
yesterday = datetime(year=2024, month=11, day=1)

graph_post_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many hours did you programmed today? ')
}

response = requests.post(url=graph1_endpoint, json=graph_post_config, headers=headers)
print(response.text)

graph1_pixel_update_endpoint = f'{graph1_endpoint}/{yesterday.strftime('%Y%m%d')}'

pixel_update_config = {
    'quantity': '4',
}
# response = requests.put(url=graph1_pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)
