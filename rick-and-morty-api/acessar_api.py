import requests

base_url = "https://rickandmortyapi.com/api"

def get_rick_and_morty_info(character_id):
    url = f"{base_url}/character/{character_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data {response.status_code}")


character_id = "1"
rick_and_morty_info = get_rick_and_morty_info(character_id)

if rick_and_morty_info: # se for True
    print(f'{rick_and_morty_info["name"]}')
    