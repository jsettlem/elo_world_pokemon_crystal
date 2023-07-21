import json
import os


def main():
    species_types = {}

    files = [f for f in os.listdir("./data_files/pokemon_stats/base_stats") if f.endswith(".asm")]

    for file in files:
        with open(f"./data_files/pokemon_stats/base_stats/{file}", 'r') as f:
            lines = f.readlines()

            species = lines[0].split()[1].strip()
            types = lines[5].replace(",", "").split()[1:3]

            print(f"{species} {types}")

            species_types[species] = types

    with open("./data_files/species_types.json", 'w') as f:
        json.dump(species_types, f, indent=2)

if __name__ == '__main__':
    main()
