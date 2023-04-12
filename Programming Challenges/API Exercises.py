### EXERCISE 1 ###
# """
# This API is called 'Open Notify' http://open-notify.org/
# It gives access to data about the Intrnational Space NASA station!
# This API DOES NOT require authentication,
#
# TASK: Make a call to the API endpoint to get live information about astronauts in space
#
# """

import requests
from pprint import pprint as pp

endpoint1 = 'http://api.open-notify.org/astros.json'  # this endpoint returns data about astronauts currently in space
response = requests.get(endpoint1) # making a call to the API
print(response.status_code)  # make sure that your connection status code is 200, which means success!


# make it look pretty with pp print- formats our output
data = response.json()  # lets see what data about people in space we get back from the API response
pp(data)


# to only get the first names back
for person in data['people']:
    print(person['name']) # if we want osmoenne specific, we ned to add an index [0]


# let's extract data from the response and write it to a file
    # we need section 'people' from json, which is a list of dict, so...
    # we also need to extract name from each dict item in that list
# #
with open('astranouts.txt', 'w') as text_file:
    for item in data['people']:
        text_file.write(item['name'] + '\n') # added new line character, so each name appears on a new line.

#
# ### EXERCISE 2 ###
# """
# TASK: Writing a log file to monitor the movement of ISS
#
# Make a call to the API to get the current location for the International Space Station
# See what data you get back
# Convert the 'timestamp' from the response into readable date and time format
# Write a log to the new file that captures time and ISS's location.



import requests
from datetime import datetime
from pprint import pprint as pp

# this endpoint tells the current location for international space station
endpoint3 = 'http://api.open-notify.org/iss-now.json'
response = requests.get(endpoint3)
# #
data = response.json()
pp(data)
# #
timestamp = data['timestamp']
dt_object = datetime.fromtimestamp(timestamp)

# #
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))
# #
msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
dt = dt_object,
lat = data['iss_position']['latitude'],
lon = data['iss_position']['longitude']
)
# #
# # # Write a log record to a file
with open('space_station_location.txt', 'a') as text_file:
    text_file.write(msg + '\n')


# # # Run the program multiple times to get more records in the log
#
#
# '''EXAMPLE SOLUTION'''
#
import requests
from datetime import datetime
from pprint import pprint as pp
# #
# this endpoint tells the current location for international space station
endpoint3 = 'http://api.open-notify.org/iss-now.json'
response = requests.get(endpoint3)
# #
data = response.json()
pp(data)
# #
timestamp = data['timestamp']
dt_object = datetime.fromtimestamp(timestamp)
# #
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))
# #
msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
     dt = dt_object,
    lat = data['iss_position']['latitude'],
     lon = data['iss_position']['longitude']
# # )
# #
 with open('space_station_location.txt', 'a') as text_file:
# # text_file.write(msg + '\n')
#
#
#
# ### EXERCISE 3 -- DEMO (as requires Authentication key ###
# """
# This API is called 'Open Weather Map' http://api.openweathermap.org
# It gives access to data about weather at different locations in the world and much more!
# This API DOES require authentication! But it is FREE to register.
# In order to get some data back, you need to use a unique 'Authentication Key'
# It is VERY COMMON for many APIs to use authentication, especially in the professional world.
#
#
# Also introduce idea of PAYLOAD and different types of it. For this API the payload is a dictionary consisting of:
#  location q, unit and appid which is your personal API key.
# """
#
import requests
from pprint import pprint as pp
# #
appid = ''  # key to connect to the API --> create a free account and paste your OWN key here
# #
endpoint = 'http://api.openweathermap.org/data/2.5/weather' # see doc to customise your payload
# #
payload = {
     'q': 'London,UK',
     'unit': 'metrics',
     'appid': appid, }
# #
response = requests.get(url=endpoint, params=payload)
# #
data = response.json()
# #
# #
pp(data['name'])
pp(data['weather'])
# #
pp(data)
#
#
#
# ### EXERCISE 4 ###
# """
# This API is called 'Pokéapi' pokeapi.co/
# It gives access to data about Pokémons
# This API is free and does not require any authentication!
#
# Each Pokemon has a number that identifies it
#
# You can retrieve information about different Pokemon from urls
#
#https://pokeapi.co/api/v2/pokemon/6/
# """
#
import requests
from pprint import pprint
# #
pokemon_number = input("What is the Pokemon's ID? ")
# #
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number) # note how we manupulate the url to request data! get pokemon id and add to the space
# #
response = requests.get(url)
print(response)
# #
pokemon = response.json()
pprint(pokemon)
#
#
# ### EXERCISE 5 ###
# """
#  Get the height and weight of a specific Pokemon and print the output
#
# !!! Extension !!!: Print the names of all of a specific Pokemon's moves
# """
# #
import requests
# #
pokemon_number = input("What is the Pokemon's ID? ")
# #
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
# #
response = requests.get(url)
pokemon = response.json()
# #
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])
#
#
# """ EXTENSION - focuss on this part if you have time as it helps the homework  """
# # import requests
# #
# # pokemon_number = input("What is the Pokemon's ID? ")
# #
# # url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
# #
# # response = requests.get(url)
# # pokemon = response.json()
# #
# # moves = pokemon['moves']
# #
# # for move in moves:
# #     print(move['move']['name'])