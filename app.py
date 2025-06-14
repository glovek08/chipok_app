from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Chinese Pokedex</h1><small>Cheap ass pokedex from the ghetto.</small>"

@app.route("/about")
def about():
    return "<h1>About Page</h1><small>Scrappy About</small>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)