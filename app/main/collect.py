import requests

def get_match_data(api_key):
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data