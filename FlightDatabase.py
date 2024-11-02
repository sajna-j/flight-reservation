from collections import deque
import random

class FlightDatabase():
    
    def __init__(self):
        self.givenFlights = []

    def add_flight(self, givenFlight):
        self.givenFlights.append(givenFlight)
    
    def get_flight(self, userInput):
        index = 0
        for index in range(len(self.givenFlights)):
            if(int(userInput) == self.givenFlights[index].flightNumber):
                return index
        return -1
    
    def display_flight(self):

        if not self.givenFlights:
            return "Throw ERROR: NO Flights Exist"
        else:
            for currentFlight in self.givenFlights:
                print(f'Flight ID Number: {currentFlight.flightNumber}, Departure Location: {currentFlight.departureLocation}, Arrival Location: {currentFlight.arrivalLocation}, Time Interval: {currentFlight.timeInterval}, Time Duration: {currentFlight.duration}')
    
    def checkFlightExistsBasedOnFlightId(self, userInput):
        for curFlight in self.givenFlights:
            if(int(userInput) == int(curFlight.flightNumber)):
                return True
        return False
    
    def flightExists(self, fromSpace, toSpace):
        for curFlight in self.givenFlights:
            if(fromSpace == curFlight.departureLocation and toSpace == curFlight.arrivalLocation):
                return True
        return False
    
    def getFlightNumber(self, fromSpace, toSpace):
        for curFlight in self.givenFlights:
            if(fromSpace == curFlight.departureLocation and toSpace == curFlight.arrivalLocation):
                return curFlight.flightNumber
        return False
    
    def sortbyDuration(self):
        index = 0
        jindex = 0
        for index in range(len(self.givenFlights)):
            for jindex in range(len(self.givenFlights)):
                if(self.givenFlights[index].duration < self.givenFlights[jindex].duration):
                   temp = self.givenFlights[index]
                   temp2 = self.givenFlights[jindex]
                   self.givenFlights[jindex] =  temp
                   self.givenFlights[index] =  temp2
        
        for curFight in self.givenFlights:
            curFight.display_flight()

    def sortbyNonOverlappingActivities(self):
        nonOverlapSced = []

        sortedFlights = sorted(self.givenFlights, key=lambda flight: flight.timeInterval[1])

        known_act = []
        lastKnownEndTime = sortedFlights[0].timeInterval[1]
        known_act.append(sortedFlights[0])
        for i in range(1, len(sortedFlights)):
            curActivityStartTime = sortedFlights[i].timeInterval[0]
            if lastKnownEndTime <= curActivityStartTime:
                
                known_act.append(sortedFlights[i])
                lastKnownEndTime = sortedFlights[i].timeInterval[1]
        
        for flight in known_act:
            flight.display_flight()
    




        """
        sortedFlights = sorted(self.givenFlights, key=lambda flight: flight.timeInterval[1])
        sizeOfFlightLog = len(sortedFlights)

        lastKnownEndTime = -1
        index=1 

        dpArray = [1] * sizeOfFlightLog
        previousIndex = [-1] *sizeOfFlightLog

        for index in range(1, sizeOfFlightLog):
            for jindex in range(index):

                curActivityStartTime = sortedFlights[jindex].timeInterval[0]
                if (sortedFlights[index].timeInterval[1] <= curActivityStartTime):
                    if (dpArray[index] < dpArray[jindex]+1):
                        dpArray[index] = dpArray[jindex]+1
                        previousIndex[index] = jindex
        
        maxIndex = dpArray.index(max(dpArray))
        while -1 != maxIndex:
            nonOverlapSced.append(sortedFlights[maxIndex])
            maxIndex = previousIndex[maxIndex]
        """
        for flight in nonOverlapSced:
            flight.display_flight()


    #Use BFS
    def find_indirect_flights(self, source, dest):
        known_indirect_flights = []
        visitedSet = set()  # To keep track of visited nodes

        departure_map = {}
        for flight in self.givenFlights:
            if flight.departureLocation not in departure_map:
                departure_map[flight.departureLocation] = []
            departure_map[flight.departureLocation].append(flight)
        
        queue = deque([(source, [])])

        while (queue):
            currentFlight, flightPath = queue.popleft()

            if currentFlight not in visitedSet:
                visitedSet.add(currentFlight)
            
                if currentFlight in departure_map:
                    for flight in departure_map[currentFlight]:
                        curpath = flightPath + [flight.flightNumber]

                        if flight.arrivalLocation == dest:
                            known_indirect_flights.append(curpath)

                        if flight.arrivalLocation not in visitedSet:
                            queue.append((flight.arrivalLocation, curpath))


        return known_indirect_flights
    
    def display_indirect_flights(self, sourceLocation, destLocation):
        all_known_indirect_flights = self.find_indirect_flights(sourceLocation, destLocation)

        count = 1

        if all_known_indirect_flights is not None:
            for curOverallFlightPath in all_known_indirect_flights:
                if(len(curOverallFlightPath) > 1):
                    print("Indirect Flight Option: " + str(count))
                    count+=1
                for curIndirectFlight in curOverallFlightPath:
                    if(len(curOverallFlightPath) > 1):
                        self.givenFlights[self.get_flight(curIndirectFlight)].display_flight()
                
                print()

    def display_direct_flights(self, sourceLocation, destLocation):
        count = 1

        if self.givenFlights is not None:
            for cur_flight in self.givenFlights:
                
                
                if((cur_flight.departureLocation == sourceLocation) and (cur_flight.arrivalLocation == destLocation)):
                    print("Direct Flight Option: " + str(count))
                    cur_flight.display_flight()
                    print()
        
        
    def select_flight_to_book(self):
        print("Available Flight List")
        self.display_flight()


        fromDestination = input("Please Select a Flight Depature: " )
        toDestination = input("Please Select a Flight Arrival: " )
        index = input("1 to show avaliability or 2 to book the flight: ")

        if(index == 1):
            self.display_direct_flights(fromDestination, toDestination)
            self.display_indirect_flights(fromDestination, toDestination)
        if(index == 3):
            flightdata.sortbyDuration()
        else:
            if(self.flightExists(fromDestination, toDestination)):

                flight = self.getFlightNumber(fromDestination, toDestination)
                self.givenFlights[self.get_flight(flight)].main_menu_catalog_seating()
            else:
                print("False")
