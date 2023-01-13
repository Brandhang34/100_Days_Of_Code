from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lxml
import requests
import os

os.environ['SPOTIPY_CLIENT_ID'] = '2bed9b2bbd84439896750601cba79575'
os.environ['SPOTIPY_CLIENT_SECRET'] = '1cd7114ad6aa43dd8c8122cd296e54ce'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://sushamae.com'

user_input_date=input("What year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input_date}/")
web_page=response.text

soup = BeautifulSoup(web_page, "html.parser")
song_titles=soup.select("li ul li h3")
list=[title.getText().strip() for title in song_titles]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", show_dialog=True, cache_path="token.txt"))

user_id = sp.current_user()["id"]

year = user_input_date.split("-")[0]

uri_list=[]
for song in list:
    results = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = results["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except:
        print(f"{song} does not exist and will be skipped")

my_playlist = sp.user_playlist_create(user=f"{user_id}", name=f"{user_input_date} Billboard Top Tracks", public=False, description="Top Tracks from back in the Days")

playlist_id=my_playlist["id"]
for items in uri_list:
    append_song = sp.playlist_add_items(playlist_id, items,position=None)
