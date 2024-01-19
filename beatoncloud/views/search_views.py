from flask import Blueprint, render_template, request, redirect, session
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import spotipy
import json

CLIENT = json.load(open("beatoncloud\conf.json", "r+"))

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT["id"], client_secret=CLIENT["secret"]
)

bp = Blueprint("search", __name__, url_prefix="/")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@bp.route("/search/", methods=["GET"])
def search_results():
    query = request.args.get("query")
    if query:
        # 사용자의 쿼리로 Spotify API 검색 수행
        data = sp.search(q=query, limit=1, type="artist")
        print(data)
        artists = data.get("artists", {}).get("items", [])
        artist_id = artists[0].get("id")

        albums = sp.artist_albums(artist_id)
        top_tracks = sp.artist_top_tracks(artist_id, country="KR")

        artist_albums = [
            {
                "id": album["id"],
                "name": album["name"],
                "release_date": album["release_date"],
                "images": album.get("images", []),
            }
            for album in albums["items"]
        ]

        artist_info = {
            "albums": artist_albums,
            "top_tracks": [
                {
                    "id": track["id"],
                    "name": track["name"],
                    "preview_url": track.get("preview_url", None),
                }
                for track in top_tracks["tracks"]
            ],
        }

        return render_template(
            "result.html",
            query=query,
            artists=artists,
            artist_albums=artist_albums,
            artist_info=artist_info,
            token=session.get("token", None),
        )
    else:
        return render_template("index.html")
