import requests

BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_data(name):
    response = requests.get(f"{BASE_URL}/pokemon/{name.lower()}")

    if response.status_code != 200:
        return None
    
    data = response.json()

    stats = {}
    for stat in data["stats"]:
        stats[stat["stat"]["name"]] = stat["base_stat"]
    
    return {
        "name": data["name"].title(),
        "hp": stats["hp"],
        "attack": stats["attack"],
        "defense": stats["defense"],
        "speed": stats["speed"]
    }