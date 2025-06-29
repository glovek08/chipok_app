from flask import Flask, render_template, url_for
import requests
import random

app = Flask(__name__)


def get_pokemon_data():
    """Fetch Pokemon data from PokeAPI"""
    pokemon_list = []
    # Generate 20 random pokemons (in series).
    # We'll leave 700 as the maximum pokemon entry till i figure out how to get a count of pokemon entires.
    poke_rand = random.randint(20, 700)
    pokemon_ids = list(range((poke_rand - 20), poke_rand))

    for pokemon_id in pokemon_ids:
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
            if response.status_code == 200:
                data = response.json()
                abilities = [
                    ability["ability"]["name"] for ability in data["abilities"]
                ]
                types = [type_info["type"]["name"] for type_info in data["types"]]
                pokemon_info = {
                    "name": data["name"].capitalize(),
                    "id": data["id"],
                    "height": data["height"],
                    "weight": data["weight"],
                    "abilities": ", ".join(abilities),
                    "types": ", ".join(types),
                    "sprite": data["sprites"]["front_default"],
                }
                pokemon_list.append(pokemon_info)
        except Exception as e:
            print(f"Error fetching Pokemon {pokemon_id}: {e}")
            continue

    return pokemon_list


@app.route("/")
@app.route("/home")
def home():
    pokemon_data = get_pokemon_data()
    return render_template("home.html", pokemon_data=pokemon_data, title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
