from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
db = SQLAlchemy(app)

# Models
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20), unique=True, nullable=False)
    departure = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    seats = db.relationship('Seat', backref='flight', lazy=True)

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String(10), nullable=False)
    is_booked = db.Column(db.Boolean, default=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)

# Routes
@app.route('/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([{
        'id': flight.id,
        'flight_number': flight.flight_number,
        'departure': flight.departure,
        'destination': flight.destination,
        'departure_time': flight.departure_time.isoformat(),
        'total_seats': flight.total_seats
    } for flight in flights])

@app.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    return jsonify({
        'id': flight.id,
        'flight_number': flight.flight_number,
        'departure': flight.departure,
        'destination': flight.destination,
        'departure_time': flight.departure_time.isoformat(),
        'total_seats': flight.total_seats
    })

@app.route('/flights', methods=['POST'])
def create_flight():
    data = request.json
    new_flight = Flight(
        flight_number=data['flight_number'],
        departure=data['departure'],
        destination=data['destination'],
        departure_time=datetime.fromisoformat(data['departure_time']),
        total_seats=data['total_seats']
    )
    db.session.add(new_flight)
    db.session.commit()

    # Create seats for the flight
    for i in range(1, new_flight.total_seats + 1):
        seat = Seat(seat_number=f"{i:03d}", flight_id=new_flight.id)
        db.session.add(seat)
    db.session.commit()

    return jsonify({'message': 'Flight created successfully', 'id': new_flight.id}), 201

@app.route('/flights/<int:flight_id>', methods=['PATCH'])
def update_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    data = request.json

    if 'flight_number' in data:
        flight.flight_number = data['flight_number']
    if 'departure' in data:
        flight.departure = data['departure']
    if 'destination' in data:
        flight.destination = data['destination']
    if 'departure_time' in data:
        flight.departure_time = datetime.fromisoformat(data['departure_time'])
    if 'total_seats' in data:
        flight.total_seats = data['total_seats']

    db.session.commit()
    return jsonify({'message': 'Flight updated successfully'})

@app.route('/flights/<int:flight_id>/seats', methods=['GET'])
def get_flight_seats(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    return jsonify([{
        'id': seat.id,
        'seat_number': seat.seat_number,
        'is_booked': seat.is_booked
    } for seat in flight.seats])

@app.route('/seats/<int:seat_id>/book', methods=['POST'])
def book_seat(seat_id):
    seat = Seat.query.get_or_404(seat_id)
    if seat.is_booked:
        return jsonify({'error': 'Seat is already booked'}), 400
    seat.is_booked = True
    db.session.commit()
    return jsonify({'message': 'Seat booked successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)