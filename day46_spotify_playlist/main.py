import datetime as dt
import requests
from bs4 import BeautifulSoup
from spotify import apiSpotify

now = dt.datetime.now()
spotify = apiSpotify()
# date_to_travel = input("Which date you want to travel to? Type the date in YYYY-MM-DD: ")
date_to_travel = "2013-08-19"
year = date_to_travel.split("-")[0]
URL = "https://www.billboard.com/charts/hot-100/" + date_to_travel
response = requests.get(URL)
response.raise_for_status()

website_text = response.text
soup = BeautifulSoup(website_text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
uri = []
for song in song_names:
    try:
        uri.append(spotify.uri_return(song, year))
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist_id = spotify.create_playlist(f"Hit songs from {year}")["id"]
spotify.add_playlist(playlist_id, uri)
