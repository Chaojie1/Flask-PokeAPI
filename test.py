from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    foxes = []
    for _ in range(10):
        response = requests.get("https://randomfox.ca/floof/").json()
        foxes.append({'imageurl': response['image']})
    return render_template("home.html", foxes=foxes)
if __name__ == '__main__':
    app.run(debug=True)