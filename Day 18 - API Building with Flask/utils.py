from flights_data import flights

def search_flight(fid, flights):
    return [element for element in flights if element['flight_id'] == fid]
# this function to search the API for the flight based on the ID, it returns the dictionary

def get_index(fid, flights):
    for i, flight in enumerate(flights):
        if flight['flight_id'] == fid:
            return i
    return -1

#this given the id of the flight, and it will return the index of the flight (0 or 1 as there's two flights)
# print(get_index(1818,flights))

