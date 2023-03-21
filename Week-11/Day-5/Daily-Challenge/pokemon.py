from flask import Flask,render_template,url_for
import requests
from my_pagination import pagination_class

app = Flask(__name__)

pokemon_type_list = ['Normal', 'Fire', 'Water', 'Grass', 'Flying', 'Fighting', 'Poison', 'Electric', 'Ground', 'Rock', 'Psychic', 'Ice', 'Bug', 'Ghost', 'Steel', 'Dragon', 'Dark' ,'Fairy']

@app.route('/')
def home():
	return render_template('home.html',poke_types = pokemon_type_list)

@app.route('/pokemon/byname/<pokemon_id>')
@app.route('/pokemon/<pokemon_id>')
def pokemon_by_id(pokemon_id):
	r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}', auth=('user', 'pass'))
	if r.status_code == 200:
		pokemon = r.json()
		return render_template('pokemon_id.html',pokemon = pokemon)
	return 'Error, pokemon does not exist'

@app.route('/pokemon/type/<pokemon_type>')
def pokemon_type(pokemon_type):
	r = requests.get(f'https://pokeapi.co/api/v2/type/{pokemon_type}',auth=('user','pass'))
	if r.status_code == 200:
		pokemon_type =  r.json()['pokemon']
		pokemon_list = []
		for pokemon in pokemon_type:
			pokemon = requests.get(pokemon['pokemon']['url']).json()
			pokemon_list.append(pokemon)
		return render_template('pokemon_type.html',pokemons = pokemon_list)
	return 'Error, pokemon type does not exist'

r = requests.get(f'http://pokeapi.co/api/v2/pokemon/?limit=811',auth=('user','pass'))
pokemons =  r.json()
pokelist = []
for index,pokemon in enumerate(pokemons['results']):
	pokelist.append(pokemon)

all_pokemon_pagination = pagination_class(pokelist,7)

@app.route('/pokemon/all/<page_num>')
def all_pokemon(page_num = 0):	
	pokemon_list = []
	for pokemon in all_pokemon_pagination.paginated[page_num]:
		pokemon = requests.get(pokemon['url']).json()
		pokemon_list.append(pokemon)
	return render_template('all_pokemon.html', pokemons = pokemon_list)

if __name__ == '__main__':
	app.run(debug=True)
