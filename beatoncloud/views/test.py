import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

cid = "193aa245183a47b4846423c5bc22d975"
secret = "ce680cd732c64a8ba9e5d3dcf32d3143"
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search("아이즈원", limit=1, type="album")
pprint.pprint(result)

import urllib.request

urllib.request.urlretrieve(result["albums"]["items"][0]["images"][0]["url"], "18.jpg")
