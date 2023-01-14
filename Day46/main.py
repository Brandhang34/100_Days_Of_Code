from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lxml
import requests
import os

#Set the environment variables from spotify

# os.environ['SPOTIPY_CLIENT_ID'] = ''
# os.environ['SPOTIPY_CLIENT_SECRET'] = ''
# os.environ['SPOTIPY_REDIRECT_URI'] = ''

user_input_date=input("What year do you want to travel to? Type the date in this format YYYY-MM-DD:")


#Web scrape and obtain the list of top 100 songs from the certain date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input_date}/")
web_page=response.text

soup = BeautifulSoup(web_page, "html.parser")
song_titles=soup.select("li ul li h3")
list=[title.getText().strip() for title in song_titles]

#Obtain the spotify userID
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", show_dialog=True, cache_path="token.txt"))

user_id = sp.current_user()["id"]

year = user_input_date.split("-")[0]

#Append the URIs from each of the song
uri_list=[]
for song in list:
    results = sp.search(q=f"track:{song} year:{year}", type="track")
    #Ignore the songs that do not exist in spotify
    try:
        uri = results["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except:
        print(f"{song} does not exist and will be skipped")


#Create the playlist and add all of the songs that were appended to the URI list
my_playlist = sp.user_playlist_create(user=f"{user_id}", name=f"{user_input_date} Billboard Top Tracks", public=False, description="Top Tracks from back in the Days")

playlist_id=my_playlist["id"]
print(playlist_id)


sp.playlist_add_items(playlist_id, uri_list,position=None)
