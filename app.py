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


# Run Flask app if executed directly
if __name__ == '__main__':
    app.run(debug=True)
