import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#from dotenv import load_dotenv
import os

#load_dotenv()


SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url = URL, headers=header)
content = response.text
soup = BeautifulSoup(content, "html.parser")


titles = [title.getText().strip() for title in soup.select("li ul li h3")]
print(titles)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="ozunlo"))

user_id = sp.current_user()["id"]

sp.user_playlist_create(user="ozunlo", name="eskisehir", public=False, collaborative=False, description='Eskişehire hosgelsin yil 2002')


song_uris=[]
for song in titles:
    result = sp.search(q=song, type="track", limit=1)
    track = result.get('tracks', {}).get('items', [])
    if track:
        uri = track[0]["uri"]
        song_uris.append(uri)
    else:
        print(f"{song} doesn't exist in Spotify")
print(song_uris)

# To find all the playlists' ids you can run the following code or go to your spotify list and copy the id in the url
#PLAYLISTS=sp.current_user_playlists()

# Add your own playlist_id 
sp.playlist_add_items(playlist_id="1vZ6WYLCXs2EIzbcl7JdwR", items=song_uris)
