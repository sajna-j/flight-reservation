from flask import Flask, jsonify, request
from flight_objects import flightdata
from enum import Enum
from FlightDatabase import FlightDatabase
from helpers import sortbyDate, sortbyDuration
from Flight import Flight
from Seats import SingleLinkedSeatingList

"""
DONE GET flight by ID
DONE GET direct and indirect flights for src & dest
DONE GET flights sorted by time, depart date etc
DONE GET seats of a flight sorted by cost, status, id (class)
DONE GET available seats of a flight
DONE GET a single seat of a flight ?

DONE POST a flight's seat as booked 
DONE POST a flight's seat as cancelled (unbooked)
"""
app = Flask(__name__)

class FlightSortOptions(Enum):
    DURATION: str = "duration"
    DATE: str = "date"

class SeatSortOptions(Enum):
    COST: str = "cost"
    ID: str = "id"
    STATUS: str = "status"
    
    @classmethod
    def _missing_(cls, value):
        return cls.ID  # Default to ID sort if value not found

SORT_MAPPING = {
    FlightSortOptions.DURATION: sortbyDuration,
    FlightSortOptions.DATE: sortbyDate,
    SeatSortOptions.COST: SingleLinkedSeatingList.sortBySeatCost,
    SeatSortOptions.ID: SingleLinkedSeatingList.sortBySeatNum,
    SeatSortOptions.STATUS: SingleLinkedSeatingList.sortBySeatStatus
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
    jsonable_flights = []
    for flight in results:
        jsonable_flights.append(flight.as_dict())
    return jsonify(jsonable_flights), 200

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


# Endpoint to get all seats in a flight
@app.route('/flights/<flight_id>/seats', methods=['GET'])
def get_seats(flight_id):
    sort_by = request.args.get('sort_by')

    flight_ind = flightdata.get_flight(flight_id)
    if flight_ind != -1:
        flight = flightdata.givenFlights[flight_ind]
        
        if sort_by and (sort_by := SeatSortOptions(sort_by)):
            SORT_MAPPING[sort_by](flight.aval_seating_list)
        else:
            # by default, the seats should just show by seat number
            SingleLinkedSeatingList.sortBySeatNum(flight.aval_seating_list)

        seats = flight.aval_seating_list.as_list()
        return jsonify(seats), 200
    return jsonify({"error": "Flight not found"}), 404


# Endpoint to get a specific seat by ID in a flight
@app.route('/flights/<flight_id>/seats/<int:seat_id>', methods=['GET'])
def get_seat(flight_id, seat_id):
    flight_ind = flightdata.get_flight(flight_id)
    if flight_ind == -1:
        return jsonify({"error": "Flight not found"}), 404
    flight = flightdata.givenFlights[flight_ind]
    
    seat = flight.get_seat(seat_id)
    if seat:
        return jsonify(seat.as_dict()), 200
    return jsonify({"error": "Seat not found"}), 404
    

# Endpoint to book a seat in a flight
@app.route('/flights/<flight_id>/seats/<int:seat_id>/book', methods=['POST'])
def book_seat(flight_id, seat_id):
    flight_ind = flightdata.get_flight(flight_id)
    if flight_ind == -1:
        return jsonify({"error": "Flight not found"}), 404
    flight = flightdata.givenFlights[flight_ind]
    
    seat = flight.get_seat(seat_id)
    if seat:
        flight.aval_seating_list.sortBySeatNum()
        flight.booked_seating_list.book_seat(flight.aval_seating_list, seat_id)
        seat = flight.get_booked_seat(seat_id)
        return jsonify(seat.as_dict()), 200
    else:
        return jsonify({"error": "Seat not found or is not available"}), 404   

        if curr_booked_seat_node == None:
            return None
    
# Endpoint to cancel a seat in a flight
@app.route('/flights/<flight_id>/seats/<int:seat_id>/cancel', methods=['POST'])
def cancel_seat(flight_id, seat_id):
    flight_ind = flightdata.get_flight(flight_id)
    if flight_ind == -1:
        return jsonify({"error": "Flight not found"}), 404
    flight = flightdata.givenFlights[flight_ind]
    
    seat = flight.get_booked_seat(seat_id)
    if seat:
        flight.aval_seating_list.sortBySeatNum()
        flight.booked_seating_list.cancel_a_seat(flight.aval_seating_list, seat_id)
        seat = flight.get_seat(seat_id)
        return jsonify(seat.as_dict()), 200
    else:
        return jsonify({"error": "Seat does not exist or is either available and cannot be cancelled"}), 404   


# Run Flask app if executed directly
if __name__ == '__main__':
    app.run(debug=True)
