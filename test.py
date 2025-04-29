from flask import Flask, render_template
import requests

app = Flask(__name__)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
@app.route("/")
def index():
    streamers = []
    response = requests.get("https://api.chess.com/pub/streamers",headers=headers)
    print(response)
    if response.status_code != 200:
        return f"API error: {response.status_code}"

    data = response.json()

    for i in data["streamers"]:
        streamer = {'avatar': i['avatar'], 'user': i['username'],'live':None}
        if i["is_live"] == True:
            streamer['live'] = "Live"
        else:
            streamer['live'] = "Offline"
        streamers.append(streamer)
    return render_template("home.html", streamers=streamers)
if __name__ == '__main__':
    app.run(debug=True)