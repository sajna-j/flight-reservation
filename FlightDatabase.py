from collections import deque
import random
from Flight import Flight, IndirectFlight
# class to represent a flight
class FlightDatabase():
    
    # constructor to allow multiple flight objects to be added
    def __init__(self):
        self.givenFlights = []

    # add a flight
    def add_flight(self, givenFlight):
        self.givenFlights.append(givenFlight)
    
    # remove flight based on flight number
    def remove_flight(self, givenFlight, remove_flightNumber):
        self.givenFlights = [flight for flight in self.givenFlights if givenFlight.flightNumber != remove_flightNumber]

    # get the flight index seen in list 
    def get_flight(self, userInput):
        index = 0

        # iterate over list to see if the flight exists
        for index in range(len(self.givenFlights)):
            if(userInput == self.givenFlights[index].flightNumber):
                return index
        return -1
    
    # to display all the flights in the database
    def display_flight(self):

        if not self.givenFlights:
            return "Throw ERROR: NO Flights Exist"
        else:
            for currentFlight in self.givenFlights:
                print(f'Flight ID Number: {currentFlight.flightNumber}, Departure Location: {currentFlight.departureLocation}, Arrival Location: {currentFlight.arrivalLocation}, Date: {currentFlight.date.month}/{currentFlight.date.day}/{currentFlight.date.year}, Time Interval: {currentFlight.timeInterval}, Time Duration: {currentFlight.duration}')
    
    # check a check a Fligh Exists Based On FlightId
    def checkFlightExistsBasedOnFlightId(self, userInput):
        for curFlight in self.givenFlights:
            if(userInput == curFlight.flightNumber):
                return True
        return False
    
    # check if a flight exists
    def flightExists(self, fromSpace, toSpace):
        for curFlight in self.givenFlights:
            if(fromSpace == curFlight.departureLocation and toSpace == curFlight.arrivalLocation):
                return True
        return False
    
    # get a flight number 
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

    def sortbyDate(self):
        index = 0
        jindex = 0
        for index in range(len(self.givenFlights)):
            for jindex in range(len(self.givenFlights)):
                if(self.givenFlights[index].date < self.givenFlights[jindex].date):
                   temp = self.givenFlights[index]
                   temp2 = self.givenFlights[jindex]
                   self.givenFlights[jindex] =  temp
                   self.givenFlights[index] =  temp2
        
        for curFight in self.givenFlights:
            curFight.display_flight()
    
    def sortbyDepartureAirport(self, source):
        for curFight in self.givenFlights:
            if(source == curFight.departureLocation):
                curFight.display_flight()

    def sortbyArrivalAirport(self, arrival):
        for curFight in self.givenFlights:
            if(arrival == curFight.arrivalLocation):
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
    


    def is_overnight_flight(self, start_time, end_time):
        return end_time < start_time

    # FOUND
    def find_indirect_flights_NonOverlap(self, source, dest):
       
        known_indirect_flights = []
        departure_map = {}
        
        # Create a map of departure locations to their flights
        for flight in self.givenFlights:
            if flight.departureLocation not in departure_map:
                departure_map[flight.departureLocation] = []
            departure_map[flight.departureLocation].append(flight)
        
        # Queue for BFS (location, path, last end time, last date)
        queue = deque([(source, [], None, None)])  # last end time and date initialized as None

        # Track visited combinations to avoid loops
        visitedSet = set()


        while queue:
            current_location, flight_path, last_end_time, last_date = queue.popleft()

            if current_location == dest:
                # Complete path from source to destination found
                flight_numbers = [flight.flightNumber for flight in flight_path]
                if flight_numbers not in known_indirect_flights:
                    known_indirect_flights.append(flight_numbers)
                continue

            if current_location in departure_map:
                for next_flight in departure_map[current_location]:
                    
                    # Skip if we've already visited this specific path
                    visit_key = (next_flight.flightNumber, next_flight.timeInterval, next_flight.date)
                    if visit_key in visitedSet:
                        continue
                    visitedSet.add(visit_key)

                    # Initial path setup
                    if not flight_path:
                        new_flight_path = [next_flight]
                        queue.append((next_flight.arrivalLocation, new_flight_path, next_flight.timeInterval[1], next_flight.date))
                    else:
                        
                        # Apply non-overlapping and date constraints
                        last_flight = flight_path[-1]
                        last_end_time = last_flight.timeInterval[1]
                        next_start_time = next_flight.timeInterval[0]
                        is_overnight = self.is_overnight_flight(last_end_time, next_start_time)
                        difference_dates_times = (next_flight.date - last_flight.date).days
                        
                        if ((last_end_time <= next_start_time or is_overnight) and
                            last_flight.date <= next_flight.date and
                            difference_dates_times <= 2):
                            new_flight_path = flight_path + [next_flight]
                            queue.append((next_flight.arrivalLocation, new_flight_path, next_flight.timeInterval[1], next_flight.date))

        return known_indirect_flights 

    #MADE CHANGE
    def display_indirect_flights(self, sourceLocation, destLocation):
        all_known_indirect_flights = self.find_indirect_flights_NonOverlap(sourceLocation, destLocation)

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
        else:
            print("No indirect flights available.")


    #MADE CHANGE
    def display_direct_flights(self, sourceLocation, destLocation):
        count = 1
        printErrorFlag = True
        if self.givenFlights is not None:
            for cur_flight in self.givenFlights:
                
                if((cur_flight.departureLocation == sourceLocation) and (cur_flight.arrivalLocation == destLocation)):
                    print("Direct Flight Option: " + str(count))
                    count+=1
                    cur_flight.display_flight()
                    printErrorFlag = False
                    print()
        if(printErrorFlag):
            print("No direct flights available.")
            print()
        
    
    # MADE CHANGE C                          
    def select_flight_to_book(self):

        while True: 
            print("\n--- Flight Booking Menu ---")
            print("1. View Available Flights")
            print("2. Show Availability for a Specific Route")
            print("3. Book a Flight")
            print("4. Sort and View Flights by Duration")
            print("5. Exit")
            user_input = input("Please choose an option (1-5): ")

            match user_input:
                case "1":
                    print("\n --- Available Flights ---")
                    self.display_flight()
                    print()
                case "2":
                    print("\n --- Check Flight Availability Flights ---")
                    fromDestination = input("Please Select a Flight Depature: " )
                    toDestination = input("Please Select a Flight Arrival: " )

                    print("\n --- Direct Flights ---")
                    print(self.display_direct_flights(fromDestination, toDestination))
                    print()
                    print("\n --- Indirect Flights ---")
                    print(self.display_indirect_flights(fromDestination, toDestination))                        
                    print()
                case "3":
                    fromDestination = input("Please Select a Flight Depature: " )
                    toDestination = input("Please Select a Flight Arrival: " )

                    if(self.flightExists(fromDestination, toDestination)):
                        flight_number = input("\nPlease Enter the Flight Number you want to book: ")
                        flight_index = self.get_flight(flight_number)
                        if flight_index is not None:
                            self.givenFlights[flight_index].main_menu_catalog_seating()
                        else:
                            print("ERROR: Flight Number not Found")
                    else:
                        print("There are no flights present")
                    print()
                case "4":
                    print("\n --- Flights Sorted by Duration ---")
                    self.sortbyDuration()
                    self.display_flight()
                case "5":
                    print("\nLeaving Flight Booking Menu")
                    print()
                    exit()
                case "6":
                    print("\n --- Flights Sorted by Duration ---")
                    self.sortbyDuration()
                    self.display_flight()
                case _:
                    print("Invalid Input: Please Try Again")
