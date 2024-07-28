import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '356a9c93bfe6c8b8842898a2a3eae68a'
HEADER ={'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_pokemons = {
    "name": "NUGGETS",
    "photo_id": 14
}

body_change = {
    "pokemon_id": "42423",
    "name": "CAXAPOK",
    "photo_id": 24
}

body_addpokeb = {
    "pokemon_id": "45546"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)

pokemon_id = response.json()["id"]
print(pokemon_id)'''

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_addpokeb = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeb)
print(response_addpokeb.text)

