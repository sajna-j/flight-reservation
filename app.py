from flask import Flask, jsonify, request
from flight_objects import flightdata
from enum import Enum
from FlightDatabase import FlightDatabase
from helpers import sortbyDate, sortbyDuration
"""
DONE GET flight by ID
DONE GET direct and indirect flights for src & dest
GET flights sorted by time, cost, etc
GET seats of a flight sorted by cost (class)
GET available seats of a flight
GET a single seat of a flight ?

POST a flight's seat as booked 
POST a flight's seat as cancelled (unbooked)

"""
app = Flask(__name__)

class FlightSortOptions(Enum):
    DURATION: str = "duration"
    DATE: str = "date"

SORT_MAPPING = {
    FlightSortOptions.DURATION: sortbyDuration,
    FlightSortOptions.DATE: sortbyDate
}

# Endpoint to get a flight by ID
@app.route('/flights/<flight_id>', methods=['GET'])
def get_flight(flight_id):
    flight_ind = flightdata.get_flight(flight_id)
    if flight := flightdata.givenFlights[flight_ind]:
        return jsonify(flight.as_dict()), 200
    else:
        return jsonify({"error": "Flight not found"}), 404


# Endpoint to get all DIRECT flights from route A to B
@app.route('/direct-flights', methods=['GET'])
def get_direct_flights_route():
    depart = request.args.get('depart')
    arrive = request.args.get('arrive')
    sort_by = request.args.get('sort_by')
    results = flightdata.get_direct_flights(depart, arrive)
    if sort_by and (sort_by := FlightSortOptions(sort_by)):
        results = SORT_MAPPING[sort_by](results)
    return jsonify(results), 200

# Endpoint to get all INDIRECT flights from route A to B
@app.route('/indirect-flights', methods=['GET'])
def get_indirect_flights_route():
    depart = request.args.get('depart')
    arrive = request.args.get('arrive')
    sort_by = request.args.get('sort_by')
    flights_results = flightdata.get_indirect_flights(depart, arrive)
    if sort_by and (sort_by := FlightSortOptions(sort_by)):
        flights_results = SORT_MAPPING[sort_by](flights_results)

    jsonable_results = []
    for indirect_flight in flights_results:
        jsonable_results.append(indirect_flight.as_list())
    return jsonify(jsonable_results), 200


"""
# Endpoint to get flights by field (example assumes field is 'route')
@app.route('/flights/search', methods=['GET'])
def get_flights_by_field():
    field = request.args.get("field")
    value = request.args.get("value")
    if field == "route":
        results = {fid: details for fid, details in flights.items() if details["route"] == tuple(value.split(","))}
        return jsonify(results), 200
    return jsonify({"error": "Invalid field"}), 400

# Endpoint to get all seats in a flight
@app.route('/flight/<flight_id>/seats', methods=['GET'])
def get_seats(flight_id):
    flight = flights.get(flight_id)
    if flight:
        seats = []
        current_seat = flight["seats"].head
        while current_seat:
            seats.append({"seat_num": current_seat.data, "status": current_seat.status, "cost": current_seat.cost})
            current_seat = current_seat.next
        return jsonify(seats), 200
    else:
        return jsonify({"error": "Flight not found"}), 404

# Endpoint to get a specific seat by ID in a flight
@app.route('/flight/<flight_id>/seat/<int:seat_id>', methods=['GET'])
def get_seat(flight_id, seat_id):
    flight = flights.get(flight_id)
    if flight:
        current_seat = flight["seats"].head
        while current_seat:
            if current_seat.data == seat_id:
                return jsonify({"seat_num": current_seat.data, "status": current_seat.status, "cost": current_seat.cost}), 200
            current_seat = current_seat.next
        return jsonify({"error": "Seat not found"}), 404
    else:
        return jsonify({"error": "Flight not found"}), 404

# Endpoint to book a seat in a flight
@app.route('/flight/<flight_id>/seat/<int:seat_id>/book', methods=['POST'])
def book_seat(flight_id, seat_id):
    flight = flights.get(flight_id)
    if flight:
        current_seat = flight["seats"].head
        while current_seat:
            if current_seat.data == seat_id:
                if current_seat.status == "Booked":
                    return jsonify({"error": "Seat already booked"}), 400
                current_seat.status = "Booked"
                return jsonify({"message": f"Seat {seat_id} booked successfully"}), 200
            current_seat = current_seat.next
        return jsonify({"error": "Seat not found"}), 404
    else:
        return jsonify({"error": "Flight not found"}), 404
"""

# Run Flask app if executed directly
if __name__ == '__main__':
    app.run(debug=True)
