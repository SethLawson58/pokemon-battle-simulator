# Pokemon Battle Simulator
CSCI 2910 – Lab 4  
Using PokeAPI

## Project Description
This project is a Python-based Pokémon Battle Simulator that retrieves real-time Pokémon data using the PokeAPI. Users can:

- Battle two Pokémon
- View Pokémon stats
- Run a random battle simulation

The program makes live API calls to retrieve HP, Attack, Defense, and Speed stats.

## Technologies Used
- Python 3.9+
- requests library
- PokeAPI
- GitHub for version control

## API Used
https://pokeapi.co/

## Issues

### Issue #1 – KeyError on stats
Initially attempted to access stats incorrectly from JSON response. Fixed by looping through "stats" list and matching stat names.

### Issue #2 – Module Import Errors
Resolved by ensuring files were in same project directory and selecting correct Python interpreter in VS Code.

### Issue #3 – Handling Invalid Pokemon Names
Added error checking for response status codes to prevent crashes.
