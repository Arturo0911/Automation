#!/usr/bin/python3

from application.const import contants
import spotipy
from spotipy.oauth2 import SpotifyOAuth


"""class Automation:

    def __init__(self):
        self.spotify = spotipy.Spotify(auth_manager = SpotifyOAuth(
                                        client_id = contants.CLIENT_ID,
                                        client_secret = contants.CLIENT_SECRET,
                                        redirect_uri = "www.google.com",
                                        scope = "user-library-read"
        ))

        self.results = self.spotify.current_user_saved_tracks()


    def test(self):

        for idx, item in enumerate(self.results['items']):

            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])


if __name__ == '__main__':

    automation = Automation()
    automation.test()
"""