from FlightDatabase import FlightDatabase
from Flight import Flight, IndirectFlight
from typing import List, Union


# TODO: convert these from bubble sort to quick sort or merge for efficiency!

def sortbyDuration(flights: List[Union[Flight, IndirectFlight]]):
    index = 0
    jindex = 0
    for index in range(len(flights)):
        for jindex in range(len(flights)):
            if(flights[index].duration < flights[jindex].duration):
                temp = flights[index]
                flights[index] =  flights[jindex]
                flights[jindex] = temp
    
    return flights

def sortbyDate(flights: List[Union[Flight, IndirectFlight]]):
    index = 0
    jindex = 0
    for index in range(len(flights)):
        for jindex in range(len(flights)):
            if(flights[index].date < flights[jindex].date):
                temp = flights[index]
                flights[index] =  flights[jindex]
                flights[jindex] = temp
    
    return flights