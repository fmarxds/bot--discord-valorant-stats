import requests
import json


def get_player_uuid(name: str, tag: str):
    response = requests.get(f'https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}?force=false')
    response_json = json.loads(response.text)
    return response_json['data']['puuid']
