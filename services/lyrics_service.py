import requests

LYRICS_API_URL = "https://api.lyrics.ovh/v1/"

def get_lyrics(artist, music):
    url_api = f"{LYRICS_API_URL}{artist}/{music}"


    headers = {
        "Content-Type": "application/json"
    }

    resp =  requests.get(url_api, headers=headers)

    if resp.status_code != 200:
        return None
    
    line_drop = f"Paroles de la chanson {music.capitalize()} par {artist}"
    
    lyrics =  resp.json()["lyrics"].replace(line_drop, "").strip()
    
    return lyrics