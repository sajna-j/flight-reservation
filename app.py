from flask import Flask, jsonify, request
from flight_objects import flightdata

app = Flask(__name__)

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
    results = flightdata.get_direct_flights(depart, arrive)
    return jsonify(results), 200

# Endpoint to get all INDIRECT flights from route A to B
@app.route('/indirect-flights', methods=['GET'])
def get_indirect_flights_route():
    depart = request.args.get('depart')
    arrive = request.args.get('arrive')
    results = flightdata.get_indirect_flights(depart, arrive)
    return jsonify(results), 200


# Run Flask app if executed directly
if __name__ == '__main__':
    app.run(debug=True)
