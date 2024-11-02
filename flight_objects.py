from collections import deque
import random
from FlightDatabase import FlightDatabase
from Flight import Flight
from datetime import datetime

flightdata = FlightDatabase()
flightdata.add_flight(Flight("ASD", "BOS", "CEE", (3,4), datetime(2024, 10, 30), 12,  30))
flightdata.add_flight(Flight("ASD", "BOS", "CEE", (3,4), datetime(2024, 11, 5), 12,  50))
flightdata.add_flight(Flight("ASD", "BOS", "CEE", (3,4), datetime(2024, 10, 31), 12,  20))
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
# print(flightdata.select_flight_to_book()) ## WHERE THE RESERVATION OF FLIGHTS SEATS METHOD IS 

