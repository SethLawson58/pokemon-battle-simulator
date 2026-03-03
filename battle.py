def simulate_battle(pokemon1, pokemon2):
    print(f"\n {pokemon1["name"]} vs {pokemon2["name"]}\n")

    hp1 = pokemon1["hp"]
    hp2 = pokemon2["hp"]

    if pokemon1["speed"] > pokemon2["speed"]:
        first, second = pokemon1, pokemon2
    else:
        first, second = pokemon2, pokemon1
        
    print(f"{first["name"]} goes first!\n")

    while hp1 > 0 and hp2 > 0:
        damage = max(1, first["attack"] - second["defense"] // 2)

        if first == pokemon1:
            hp2 -= damage
            print(f"{first["name"]} hits {second["name"]} for {damage} damage!")
        else:
            hp1 -= damage
            print(f"{first["name"]} hits {second["name"]} for {damage} damage!")
        
        if hp1 <= 0 or hp2 <= 0:
            break

        damage = max(1, second["attack"] - first["defense"] // 2)
        
        if second == pokemon1:
            hp2 -= damage
            print(f"{second["name"]} hits {first["name"]} for {damage} damage!")
        else:
            hp1 -= damage
            print(f"{second['name']} hits {first['name']} for {damage} damage!")
        
    print("\n===== RESULT =====")
    if hp1 > 0:
        print(f"{pokemon1['name']} wins!")
    else:
        print(f"{pokemon2['name']} wins!")