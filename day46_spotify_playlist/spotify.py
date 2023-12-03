import base64
import spotipy
import requests
from spotipy import SpotifyOAuth


class apiSpotify:
    def __init__(self):
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                                                 client_id="b79bb6d8fa024cd2bd3c6cc104214450",
                                                                 client_secret="b94c0926dbee4512b994d71cb237654d",
                                                                 redirect_uri="http://example.com",
                                                                 show_dialog=True,
                                                                 cache_path=".cache"))
        self.user_id = self.spotify.current_user()["id"]

    def uri_return(self, name, year):
        uri = self.spotify.search(q=f"track: {name} year: {year}", type='track')
        return uri['tracks']['items'][0]['uri']

    def create_playlist(self, name):
        return self.spotify.user_playlist_create(user=self.user_id, name=name, public=False)

    def add_playlist(self, play_id, item_list):
        self.spotify.playlist_add_items(play_id, item_list)
