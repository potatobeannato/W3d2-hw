import requests


def get_pokemon_info_by_name(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if not response.ok:
        return -1
    data = response.json()
    return data


def get_pokemon_info(data):
    return {
        "Name": data['forms'][0]['name'],
        "Ability": data['abilities'][0]['ability']['name'],
        "Base Experience": data['base_experience'],
        "Sprite URL": data['sprites']['front_shiny']
    }

poke_name = input("Please enter a pokemon name: ")

my_data = get_pokemon_info_by_name(poke_name)
my_pokemon_info = get_pokemon_info(my_data)

for key, value in my_pokemon_info.items():
    print(f"{key} : {value}")