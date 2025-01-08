import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7b80b1e87d32f380dfd75137455041d1'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Kairon",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "178185",
    "name": "Aranar",
    "photo_id": 2
}
body_catch = {
    "pokemon_id": "178185"
}
body_knockout = {
    "pokemon_id": "178185"
}

response_knock = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knock.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.json())

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.json())
