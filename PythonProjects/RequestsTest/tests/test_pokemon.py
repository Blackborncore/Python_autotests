import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7b80b1e87d32f380dfd75137455041d1'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '12287'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Jugger'
    print(response_get.text)



@pytest.mark.parametrize('key, value', [('id', f'{TRAINER_ID}'),('trainer_name', 'Jugger')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value
