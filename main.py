from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

pokemons = [
    "Pikachu", "Charizard", "Squirtle", "Jigglypuff", "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"
    ]

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)