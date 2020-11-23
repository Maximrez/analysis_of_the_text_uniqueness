import urllib
import requests


def search_rapid(query, num=15):
    headers = {
        "x-rapidapi-key": "10572f8cc5msh4b3d78a2b575aebp1b330bjsn409ce92f1100",
        "x-rapidapi-host": "google-search3.p.rapidapi.com"
    }

    query = {
        "q": query,
        "num": num
    }

    resp = requests.get("https://rapidapi.p.rapidapi.com/api/v1/search/" + urllib.parse.urlencode(query),
                        headers=headers)

    results = resp.json()
    return results
