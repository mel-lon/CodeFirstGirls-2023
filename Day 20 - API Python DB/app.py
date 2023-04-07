from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability, add_booking

app = Flask(__name__)


# Get availability - /availability/<string:date>
@app.route('/availability/<string:date>')
def get_bookings(date):
    result = get_all_booking_availability(date)
    return jsonify(result) # this endpoint is incomplete without this





@app.route('/booking', methods=['PUT'])
def book_appt():
    booking = request.get_json()  # _date, teamMember, time, customer
    add_booking(
        _date=booking['_date'],
        teamMember=booking['teamMember'],
        time=booking['time'],
        customer=booking['customer']
    )

    return booking


if __name__ == '__main__':
    app.run(debug=True, port=5001)
