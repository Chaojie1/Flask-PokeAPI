from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    cats = []
    response = requests.get("https://api.thecatapi.com/v1/images/search?limit=10").json()
    print(response)
    for i in response:
        cats.append({'imageurl': i['url']})
        print(i)
    return render_template("home.html", cats=cats)
@app.route("/cat/<string:id>")
def cat(id):
    response = requests.get(f"https://api.thecatapi.com/v1/images/{id}")
    data = response.json()
    cats = [{'imageurl': data['url']}]
    return render_template("home.html", cats=cats)
if __name__ == '__main__':
    app.run(debug=True)