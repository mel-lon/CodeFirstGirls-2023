import json

import requests


def display_availability(records):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
        'NAME', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18'))
    print('-' * 105)

    # print each data item.
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
            item['name'], item['12-13'], item['13-14'], item['14-15'], item['15-16'], item['16-17'], item['17-18']
        ))


def add_new_booking(date, stylist, time, customer):
    booking = {
        "_date": date,
        "teamMember": stylist,
        "time": time,
        "customer": customer
    }

    result = requests.put(
        'http://127.0.0.1:5001/booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )
    print(result.status_code)
    return result.json()


def get_availability_date(date):
    results = requests.get(
        f'http://127.0.0.1:5001/availability/{date}',
        headers={'content-type': 'application/json'}
    )
    return results.json()


def run():
    print('############################')
    print('Hello, welcome to our salon')
    print('############################')
    print()
    date = input('What date you would like to book your appointment for (YYYY-MM-DD): ')
    print()
    slots = get_availability_date(date)
    display_availability(slots)
    print('####### AVAILABILITY #######')

    print()
    place_booking = input('Would you like to book an appointment y/n ')

    book = place_booking == 'y'
    if book:
        cust = input("Enter your name: ")
        stylist = input('Choose stylist( Peter, Maddie, Dominic): ')
        time = input('Choose time based on availability (e.g 15-16) : ')
        add_new_booking(date, stylist, time, cust)
        print('Booking is successful')
        print()
        slots = get_availability_date(date)
        display_availability(slots)

    print()
    print('See you soon!')


if __name__ == '__main__':
    run()
