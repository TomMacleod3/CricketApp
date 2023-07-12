from flask import Flask, render_template, request , url_for
import requests

app = Flask(__name__)

@app.route('/')
def player():
    return render_template('index.html')

@app.route('/CricketStats', methods = ['GET', 'POST'])
def api():
    if request.method == 'POST':
        fName = request.form['fName_input']
        sName = request.form['sName_input']
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

        player_data = player_search(player_id, headers)
        return render_template('API.html', player_data = player_data)

def player_search(id, headers):
        url = "https://unofficial-cricbuzz.p.rapidapi.com/players/get-info"
        querystring = {"playerId": id}
        response = requests.get(url, headers=headers, params=querystring)
        response = response.json()

        player_data = [
            response ['image'],
            response['name'],
            response['bat'],
            response['bowl'],
            response['role'],
            response['intlTeam'][0],
            response['bio']
        ]

        return player_data


if __name__ == '__main__':
    app.run()