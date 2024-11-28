import datetime
import os
import pprint

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://example.com'
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SCOPE,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Patryk Glesman',
    )
)

user_id = sp.current_user()["id"]

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_top_100 = 'https://www.billboard.com/charts/hot-100/'


def validate(date_text):
    try:
        datetime.date.fromisoformat(date_text)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


song_names = []
song_uris = []

date = input('Which year you want to travel to? Type the date to this format YYYY-MM-DD: ')
validate(date)
year = date.split('-')[0]

content = requests.get(f'{billboard_top_100}{date}', headers=header)
soup = BeautifulSoup(content.text, 'html.parser')

result = soup.find_all('div', class_='o-chart-results-list-row-container')
for res in result:
    song_name = res.find('h3').text.strip()
    song_names.append(song_name)
    # artist = res.find('h3').find_next('span').text.strip()
    # print("song: " + song_name)
    # print("artist: " + artist)
    # print("___________________________________________________")

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# pprint.pp(song_uris)

playlist = sp.user_playlist_create(user=user_id,
                                   name=f'{date} Billboard 100',
                                   public=False,
                                   description=f'Top songs from year {year}',
                                   )

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("Playlist created and added to Spotify account")
