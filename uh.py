from bare_logic import flightdata

app = Flask(__name__)

"""
GET a flight by flight ID
GET a list of list of flights (all routes from A to B)
GET a list of flights by field
GET a list of seats in a flight
GET a seat by ID in a flight
POST a seat as booked
"""

@app.route('/flights/<int:flight_id>', methods=['GET'])
def get_flight():
