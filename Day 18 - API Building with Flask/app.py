from flask import Flask, jsonify, request

from flights_data import flights
from utils import search_flight, get_index


app = Flask(__name__)
#creates an instance of the flask application, something that adds additional functionality to that function


###############GET WILL BE THE DEFAULT METHOD
###############Fucnitons and enpoints must always be different


#without this, it'd be a regular function. now it becomes an endpoint- like a button
@app.route('/')
def hello():
    return {'hi': 'domfe'} #this will be what shows- the main page


# def hello_cfg():
#     #int he url of the flak location in the client side,w e'd add hello_cfg tot he url which would route
#     # the system tot where it is here
#         return {'hello':'CFG'}

@app.route('/flights') #if we type flights,this page will show
#the default endpoint, when not specified is methods=['GET']
def get_flights():
    return jsonify(flights)
#
@app.route('/flights/<int:id>')#this will return the info base don the ID
def get_flights2(id):
    flight = search_flight(id, flights)# the dictionary term will be replaced with the value for the flight ID
    return jsonify(flight)


#
# @app.route('/flights/<string:name>')
# def get_flight_by_id(name):
#     return jsonify(flights_data)

########################################################HOW TO GET RESOURCES


#
######################################### ADDING  A FLIHGT RESOURCE (POST Method)

@app.route('/flights', methods = ['POST'])
def add_flight():
    flight = request.get_json()
    flights.append(flight)

    return jsonify(flight)
########################################## Updating a flight -

@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    flights[index] = flight_to_update #replace the var with what we are updating fromthe request inth e client side
    return jsonify(flights[index])

@app.route('/flights<int:id>', methods=['DELETE'])
def delete_flight(id):
    index = get_index(fid=id, flights=flights)
    deleted = flights.pop(index)#pop returns the item that has been removed
    return jsonify(deleted)





if __name__ == '__main__':
    app.run(debug=True)

