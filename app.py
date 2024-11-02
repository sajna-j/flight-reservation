from bare_logic import flightdata
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for seat lists
flights["FL123"]["seats"].insert_at_end_status_cost_distrib(1, 100, "Economy")
flights["FL123"]["seats"].insert_at_end_status_cost_distrib(2, 150, "Business")
flights["FL456"]["seats"].insert_at_end_status_cost_distrib(1, 120, "Economy")
flights["FL456"]["seats"].insert_at_end_status_cost_distrib(2, 200, "First Class")

# Endpoint to get a flight by ID
@app.route('/flight/<flight_id>', methods=['GET'])
def get_flight(flight_id):
    flight = flightdata.get_flight()
    if flight:
        return jsonify({"flight_id": flight_id, "route": flight["route"]}), 200
    else:
        return jsonify({"error": "Flight not found"}), 404

# Endpoint to get all flights from route A to B
@app.route('/flights', methods=['GET'])
def get_flights_route():
    origin = request.args.get("origin")
    destination = request.args.get("destination")
    results = {fid: details for fid, details in flights.items() if details["route"] == (origin, destination)}
    return jsonify(results), 200

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

# Run Flask app if executed directly
if __name__ == '__main__':
    app.run(debug=True)
