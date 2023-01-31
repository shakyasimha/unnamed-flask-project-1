from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

pokemons = [
    {
        'index': '0001',
        'name': 'Bulbasaur',
        'type1': 'Grass',
        'type2': 'Poison'
    },
    {
        'index': '0002',
        'name': 'Ivysaur',
        'type1': 'Grass',
        'type2': 'Poison'
    },
    {
        'index': '0003',
        'name': 'Venusaur',
        'type1': 'Grass',
        'type2': 'Poison'
    },
    {
        'index': '0004',
        'name': 'Charmander',
        'type1': 'Fire',
        'type2': ''
    },
    {
        'index': '0005',
        'name': 'Charmeleon',
        'type1': 'Fire',
        'type2': ''
    },
    {
        'index': '0006',
        'name': 'Charizard',
        'type1': 'Fire',
        'type2': 'Flying'
    },
    {
        'index': '0007',
        'name': 'Squirtle',
        'type1': 'Water',
        'type2': ''
    },
    {
        'index': '0008',
        'name': 'Wartotle',
        'type1': 'Water',
        'type2': ''
    },
    {
        'index': '0009',
        'name': 'Blastoise',
        'type1': 'Water',
        'type2': ''
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Homepage')

@app.route('/about')
def about():
    return render_template('about.html', title='About Me')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/pokedex')
def pokelist():
    return render_template('pokedex.html', title="Pokedex", pokemons=pokemons)

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)