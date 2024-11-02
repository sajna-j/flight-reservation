from collections import deque
import random
from FlightDatabase import FlightDatabase
from Flight import Flight

flightdata = FlightDatabase()
flightdata.add_flight(Flight(101, "BOS", "CEE", (3,4), 12,  30))
flightdata.add_flight(Flight(102, "ALT", "BOS", (5,9), 12,  90))
flightdata.add_flight(Flight(103, "MIA", "LAX", (10,11), 12,  123))
flightdata.add_flight(Flight(104, "LAX", "ALT", (1,6), 12,  677))
flightdata.add_flight(Flight(105, "ALT", "LAX", (8,12), 12,  908))
flightdata.add_flight(Flight(106, "BOS", "ALT", (1,2), 12,  67))
flightdata.add_flight(Flight(107, "CEE", "MIA", (2,3), 12,  350))
flightdata.add_flight(Flight(108, "CEE", "LAX", (11,12), 12,  234))

print(flightdata.sortbyNonOverlappingActivities())

