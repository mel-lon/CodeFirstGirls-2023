# TASK 4 (API)
# In the API session you used the Pokémon API to retrieve a single Pokémon.
# Now use a list to store 6 Pokémon IDs.
# In a for loop call the API to retrieve the data for each Pokémon.
# Save their names, height and weight into a file called 'pokemon.txt'

import requests


for x in range(6)
    url = https://pokeapi.co/api/v2/pokemon/{x}/.format(x)
    response = requests.get(url)
    pokemon = response.json()
    print(pokemon['name'])
    print(pokemon['height'])
    print(pokemon['weight'])

 with open('pokemon.txt', 'w') as text_file:
