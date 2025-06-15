from flask import Flask, render_template, url_for


app = Flask(__name__)

pokemon_data = [
    {
        "name": "Bulbasaur",
        "abilities": 'overgrow, chloropyll'
    },
    {
        'name': 'Pikachu',
        'abilities': 'static, lightning-rod'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pokemon_data = pokemon_data, title="Home")

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)