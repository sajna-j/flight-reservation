from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Flightdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model): 
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(256), nullable=False)

    bookingList = db.relationship("BookingList", back_populates = "user")
    seatArrangement = db.relationship("Seat", back_populates = "personArrangement")

class Seat(db.Model): 
    __tablename__ = 'seat'
    address_id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.Integer)
    availabilityStatus = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    bookingList = db.relationship("BookingList", back_populates = "seat")
    personArrangement = db.relationship("User", back_populates = "seatArrangement")

class BookingList(db.Model):
    __tablename__ = 'bookingList'
    trackingList_id = db.Column(db.Integer, primary_key=True)
    
    user_address = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", back_populates = "bookingList")

    seat_address = db.Column(db.Integer, db.ForeignKey('seat.address_id'), nullable=False)
    seat = db.relationship("Seat", back_populates = "bookingList")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        db.session.query(User).delete()
        db.session.query(Seat).delete()
        db.session.commit()
        
        person1 = User(username="Dante", password="esrdtfyguh", role="loser")
        seat1 = Seat(number=101, availabilityStatus=False)
        person2 = User(username="Joe", password="iujhfdsert5", role="Winner")
        seat2 = Seat(number=202, availabilityStatus=False)

        db.session.add(person1)
        db.session.add(person2)
        db.session.add(seat1)
        db.session.add(seat2)

        db.session.commit()

        print('testworked')





        booking1 = BookingList(user_address=person1.id, seat_address=seat1.address_id)

        # Add the booking to the session
        db.session.add(booking1)

        # Commit changes
        db.session.commit()

        # Output success message
        print("Database populated with users, seats, and bookings.")

        # Example of querying and displaying data
        all_users = User.query.all()
        all_seats = Seat.query.all()
        all_bookings = BookingList.query.all()

        print("\nUsers:")
        for user in all_users:
            print(f"ID: {user.id}, Username: {user.username}, Role: {user.role}")

        print("\nSeats:")
        for seat in all_seats:
            print(f"ID: {seat.address_id}, Seat Number: {seat.number}, Availability: {seat.availabilityStatus}")

        print("\nBookings:")
        for booking in all_bookings:
            print(f"Booking ID: {booking.trackingList_id}, User ID: {booking.user_address}, Seat ID: {booking.seat_address}")

        
        