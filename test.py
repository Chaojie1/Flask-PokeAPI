from flask import Flask, render_template
import requests

app = Flask(__name__)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}


@app.route("/")
def index():
    response = requests.get("https://api.chess.com/pub/streamers",headers=headers)
    data = response.json()
    streamers = {}
    for i in data["streamers"]:
        streamers[i['username']] = {'avatar': i['avatar'], 'user': i['username'],'live':None}
        if i["is_live"] == True:
             streamers[i['username']]['live'] = "Live"
        else:
             streamers[i['username']]['live'] = "Offline"
    return render_template("home.html", streamers=streamers)
@app.route("/streamer/<id>")
def stre(id):
    response = requests.get("https://api.chess.com/pub/streamers",headers=headers)
    morereponse = requests.get(f"https://api.chess.com/pub/player/{id}",headers=headers)
    if morereponse.status_code != 200:
        return f"Failed to fetch player data for {id}", 404
    
    try:
        data = response.json()
        moredata = morereponse.json()
    except ValueError:
        return "Invalid JSON response from API", 500
    streamer = None
    available = True
    for i in data["streamers"]:
        if i["username"] == id:
            streamer = i
            break
    if streamer == None:
        available = False
    return render_template("specific.html", streamer=streamer, realuser=available,moredata=moredata)
if __name__ == '__main__':
    app.run(debug=True)