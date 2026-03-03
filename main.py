import os
from poke_api import get_pokemon_data
from battle import simulate_battle

running = True

while running:
    print("--------------------------------------------------------------------------")
    print("--------------------------Pokemon Battle Simulator------------------------")
    print("-------------------------Please Select an Option--------------------------")
    print("----------------------------1) Battle Pokemon-----------------------------")
    print("----------------------------2) View Pokemon Stats-------------------------")
    print("----------------------------3) Random Pokemon Battle----------------------")
    print("----------------------------4) End----------------------------------------")
    print("--------------------------------------------------------------------------")

    menu_choice = input("Input option: ")

    # OPTION 1 – Battle Two Pokémon
    if menu_choice == "1":
        os.system('cls')

        name1 = input("Enter first Pokemon: ")
        name2 = input("Enter second Pokemon: ")

        pokemon1 = get_pokemon_data(name1)
        pokemon2 = get_pokemon_data(name2)

        if not pokemon1 or not pokemon2:
            print("Invalid Pokemon name.")
        else:
            simulate_battle(pokemon1, pokemon2)

        keep_going = input("\nBack to Menu? (y/n): ")

        if keep_going == "y":
            os.system('cls')
        elif keep_going == "n":
            running = False
        else:
            os.system('cls')
            print("Invalid choice")

    # OPTION 2 – View Stats Only
    elif menu_choice == "2":
        os.system('cls')

        name = input("Enter Pokemon name: ")
        pokemon = get_pokemon_data(name)

        if not pokemon:
            print("Invalid Pokemon name.")
        else:
            print("\n===== Pokemon Stats =====")
            print("Name:", pokemon["name"])
            print("HP:", pokemon["hp"])
            print("Attack:", pokemon["attack"])
            print("Defense:", pokemon["defense"])
            print("Speed:", pokemon["speed"])

        keep_going = input("\nBack to Menu? (y/n): ")

        if keep_going == "y":
            os.system('cls')
        elif keep_going == "n":
            running = False
        else:
            os.system('cls')
            print("Invalid choice")

    # OPTION 3 – Random Battle
    elif menu_choice == "3":
        os.system('cls')

        import random
        id1 = random.randint(1, 151)
        id2 = random.randint(1, 151)

        pokemon1 = get_pokemon_data(str(id1))
        pokemon2 = get_pokemon_data(str(id2))

        simulate_battle(pokemon1, pokemon2)

        keep_going = input("\nBack to Menu? (y/n): ")

        if keep_going == "y":
            os.system('cls')
        elif keep_going == "n":
            running = False
        else:
            os.system('cls')
            print("Invalid choice")

    # OPTION 4 – Exit
    elif menu_choice == "4":
        running = False

    else:
        os.system('cls')
        print("Invalid option")