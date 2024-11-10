from collections import deque
import random
from FlightDatabase import FlightDatabase
from Flight import Flight
from datetime import datetime

flightdata = FlightDatabase()

'''
# Dante's test objects
======================================================================================================================
flightdata.add_flight(Flight("ASD", "BOS", "CEE", (3,4), datetime(2024, 10, 31), 12,  30))
flightdata.add_flight(Flight("1TFT02", "ALT", "BOS", (5,9), datetime(2024, 10, 31), 12,  90))
flightdata.add_flight(Flight("TFT", "MIA", "LAX", (10,11), datetime(2024, 10, 31), 12,  123))
flightdata.add_flight(Flight("GG", "LAX", "ALT", (1,6), datetime(2024, 10, 31), 12,  677))
flightdata.add_flight(Flight("GGGJV", "ALT", "LAX", (8,12), datetime(2024, 12, 31), 12,  908))
flightdata.add_flight(Flight("FTY", "BOS", "ALT", (1,2), datetime(2024, 10, 31), 12,  67))
flightdata.add_flight(Flight("UFV", "CEE", "MIA", (2,3), datetime(2024, 10, 31), 12,  350))
flightdata.add_flight(Flight("UGY", "CEE", "LAX", (11,12), datetime(2024, 10, 31), 12,  234))
flightdata.add_flight(Flight("FV", "BOS", "PHX", (4,5), datetime(2024, 11, 29), 12,  234))
flightdata.add_flight(Flight("FVU8", "PHX", "LAX", (11,12), datetime(2024, 11, 30), 12,  234))

print(flightdata.display_direct_flights("BOS", "LAX"))
print(flightdata.display_indirect_flights("BOS", "LAX"))
print(flightdata.select_flight_to_book()) ## WHERE THE RESERVATION OF FLIGHTS SEATS METHOD IS 
======================================================================================================================
'''

'''
# ======================================================================================================================
# Test to display direct flights
# Should Output 2 direct flights
flightdata.add_flight(Flight("DEL", "BOS", "LAX", (3,9), datetime(2024, 10, 31), 12,  360))
flightdata.add_flight(Flight("SPR", "BOS", "LAX", (2,8), datetime(2024, 10, 31), 12,  360))
flightdata.display_direct_flights("BOS", "LAX")
# =====================================================================================================================
'''

'''
# ======================================================================================================================
# Test direct flight overnight. May want to output a warning about overnight flight?
flightdata.add_flight(Flight("AAL", "BOS", "LAX", (11,4), datetime(2024, 10, 31), 12,  360))
flightdata.display_direct_flights("BOS", "LAX")
# =====================================================================================================================
'''

'''
# ======================================================================================================================
# Test to display indirect flights. Should Output 4 different indirect flights
flightdata.add_flight(Flight("JET1", "BOS", "IAH", (2,4), datetime(2024, 10, 31), 12,  250))
flightdata.add_flight(Flight("JET2", "BOS", "IAH", (1,3), datetime(2024, 10, 31), 12,  250))
flightdata.add_flight(Flight("JET3", "IAH", "LAX", (5,9), datetime(2024, 10, 31), 12,  200))
flightdata.add_flight(Flight("JET4", "IAH", "LAX", (6,10), datetime(2024, 10, 31), 12,  200))
flightdata.display_indirect_flights("BOS", "LAX")
# =====================================================================================================================
'''

'''
# ======================================================================================================================
# Test to display indirect flights. Should Output an option for connecting overnight flight
flightdata.add_flight(Flight("AAA", "BOS", "IAH", (21,23), datetime(2024, 10, 31), 12,  250))
flightdata.add_flight(Flight("AAB", "IAH", "LAX", (1,3), datetime(2024, 11, 1), 12,  250))
flightdata.display_indirect_flights("BOS", "LAX")
# =====================================================================================================================
'''



#=====================================================================================================================
# The flights listed below correspond with 5 different airports
# Depending on on the origin and destination, there should be dirrect and connecting flights


# Flights from BOS
flightdata.add_flight(Flight("AA11", "BOS", "DEN", (8, 10), datetime(2024, 11, 18), 20, 180))
flightdata.add_flight(Flight("AA12", "BOS", "JFK", (7, 9), datetime(2024, 11, 19), 25, 120))
flightdata.add_flight(Flight("AA13", "BOS", "LAX", (6, 9), datetime(2024, 11, 20), 30, 300))
flightdata.add_flight(Flight("AA14", "BOS", "ORD", (5, 8), datetime(2024, 11, 21), 20, 180))
flightdata.add_flight(Flight("AA15", "BOS", "DEN", (7, 9), datetime(2024, 11, 22), 30, 180))
flightdata.add_flight(Flight("AA16", "BOS", "JFK", (6, 8), datetime(2024, 11, 23), 25, 120))

#Flights from LAX
flightdata.add_flight(Flight("BB11", "LAX", "ORD", (15, 18), datetime(2024, 11, 18), 20, 180))
flightdata.add_flight(Flight("BB12", "LAX", "BOS", (21, 23), datetime(2024, 11, 19), 25, 300))
flightdata.add_flight(Flight("BB13", "LAX", "DEN", (10, 13), datetime(2024, 11, 20), 30, 180))
flightdata.add_flight(Flight("BB14", "LAX", "BOS", (20, 23), datetime(2024, 11, 21), 20, 300))
flightdata.add_flight(Flight("BB15", "LAX", "BOS", (19, 22), datetime(2024, 11, 22), 25, 300))
flightdata.add_flight(Flight("BB16", "LAX", "ORD", (18, 21), datetime(2024, 11, 23), 30, 180))

# Flights from JFK
flightdata.add_flight(Flight("CC11", "JFK", "BOS", (22, 23), datetime(2024, 11, 18), 20, 60))
flightdata.add_flight(Flight("CC12", "JFK", "DEN", (10, 13), datetime(2024, 11, 19), 25, 180))
flightdata.add_flight(Flight("CC13", "JFK", "ORD", (18, 20), datetime(2024, 11, 20), 30, 120))
flightdata.add_flight(Flight("CC14", "JFK", "LAX", (16, 19), datetime(2024, 11, 21), 20, 300))
flightdata.add_flight(Flight("CC15", "JFK", "ORD", (9, 12), datetime(2024, 11, 22), 25, 180))
flightdata.add_flight(Flight("CC16", "JFK", "LAX", (14, 17), datetime(2024, 11, 23), 30, 300))


# Flights from DEN
flightdata.add_flight(Flight("DD11", "DEN", "LAX", (11, 14), datetime(2024, 11, 18), 20, 180))
flightdata.add_flight(Flight("DD12", "DEN", "ORD", (14, 16), datetime(2024, 11, 19), 25, 120))
flightdata.add_flight(Flight("DD13", "DEN", "JFK", (14, 17), datetime(2024, 11, 20), 30, 180))
flightdata.add_flight(Flight("DD14", "DEN", "JFK", (12, 15), datetime(2024, 11, 21), 20, 180))
flightdata.add_flight(Flight("DD15", "DEN", "LAX", (16, 18), datetime(2024, 11, 22), 25, 180))
flightdata.add_flight(Flight("DD16", "DEN", "JFK", (10, 13), datetime(2024, 11, 23), 30, 180))

# Flights from ORD
flightdata.add_flight(Flight("EE11", "ORD", "JFK", (19, 21), datetime(2024, 11, 18), 20, 120))
flightdata.add_flight(Flight("EE12", "ORD", "LAX", (17, 20), datetime(2024, 11, 19), 25, 180))
flightdata.add_flight(Flight("EE13", "ORD", "BOS", (21, 23), datetime(2024, 11, 20), 30, 180))
flightdata.add_flight(Flight("EE14", "ORD", "DEN", (9, 11), datetime(2024, 11, 21), 20, 120))
flightdata.add_flight(Flight("EE15", "ORD", "DEN", (13, 15), datetime(2024, 11, 22), 25, 120))
flightdata.add_flight(Flight("EE16", "ORD", "BOS", (22, 23), datetime(2024, 11, 23), 30, 120))

flightdata.display_indirect_flights("BOS", "LAX")

#=====================================================================================================================
