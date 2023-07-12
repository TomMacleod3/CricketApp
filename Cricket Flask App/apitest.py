import requests
import json
import os

def api(fName, sName):
    url = "https://unofficial-cricbuzz.p.rapidapi.com/players/search"
    querystring = {"plrN": fName + " " + sName}
    headers = {
        "X-RapidAPI-Key": os.getenv('API_KEY'),
        "X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()

    player_list = response['player']
    searched_player = response['category']

    for player in player_list:
        if player['name'] == searched_player:
            player_id = player['id']

    result = player_search(player_id, headers)
    return result


def player_search(id, headers):
    url = "https://unofficial-cricbuzz.p.rapidapi.com/players/get-info"
    querystring = {"playerId": id}
    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    name = response['name']
    bat = response['bat']
    bowl = response['bowl']
    role = response['role']
    intlteam = response['intlTeam']
    image =  response ['image']
    print(bat)



fName = 'Jack'
sName = 'Leach'
api(fName, sName)