from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    cats = []
    response = requests.get("https://api.thecatapi.com/v1/images/search?limit=10").json()

    for i in response:
        cats.append({'imageurl': i['url'],'id':i['id']})
    return render_template("home.html", cats=cats)
@app.route("/cat/<string:id>")
def thiscat(id):
    print(id)
    response = requests.get(f"https://api.thecatapi.com/v1/images/{id}")
    data = response.json()
    cats = [{'imageurl': data['url']}]
    return render_template("home.html", cats=cats)
if __name__ == '__main__':
    app.run(debug=True)