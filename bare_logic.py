from collections import deque

class SeatNode:
    def __init__(self, data=0, cost=100, status= "Economy"):
        self.data = data
        self.status = status
        self.cost = cost
        self.next = None

class SingleLinkedSeatingList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = SeatNode(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = SeatNode(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def book_seat(self, available_seat_list):
        user_seat_input = int(input("Please enter a seat number to book: "))

        curr_available_seat_node = available_seat_list.head
        index_count = 0

        while curr_available_seat_node.next is not None and curr_available_seat_node.data != user_seat_input:
            index_count += 1
            curr_available_seat_node = curr_available_seat_node.next

        if user_seat_input == curr_available_seat_node.data:
            self.insert_at_end(user_seat_input)
            print(f"Seat {user_seat_input} has been booked")
            print()

            print(f"Seat {user_seat_input} has been added to the BOOKED LIST")
            self.to_print()

            print()
            print(f"Delete Seat: {user_seat_input} from the AVAILABLE LIST")
            available_seat_list.delete_node_at_position(index_count)
            print()
        else:
            print("Sorry the seat you entered can't be booked")
            self.to_print()
            print()


    def cancel_a_seat(self, available_seat_list):
        user_seat_input = int(input("Please enter a seat number to cancel: "))

        if self.head is None:
            print("You can't cancel the seat. ERROR No Seats in Booked List to cancel")
            return

        curr_booked_seat_node = self.head
        index_count = 0

        while curr_booked_seat_node.next is not None and curr_booked_seat_node.data != user_seat_input:
            index_count += 1
            curr_booked_seat_node = curr_booked_seat_node.next

        if curr_booked_seat_node.data == user_seat_input:
            curr_aval_seat_node = available_seat_list.head
            index_count_aval = 0

            print(f"Seat {user_seat_input} has been cancelled")
            print()
            print(f"Delete Seat: {user_seat_input} from the BOOKED LIST")
            self.delete_node_at_position(index_count)

            while curr_aval_seat_node.next is not None and user_seat_input > curr_aval_seat_node.data:
                curr_aval_seat_node = curr_aval_seat_node.next
                index_count_aval += 1

            print()
            print(f"Add Seat: {user_seat_input} to the AVAILABLE LIST")
            available_seat_list.add_node_at_position(index_count_aval, user_seat_input)
        else:
            print("Sorry this seat cannot be cancelled")

    def delete_node_at_position(self, position_index):
        count = 0

        if self.head is None:
            print("The list is empty")
            return

        if position_index == 0:
            temp = self.head
            self.head = temp.next
            return

        curr_node = self.head
        while curr_node.next is not None and position_index - 1 != count:
            count += 1
            curr_node = curr_node.next

        temp_node = curr_node.next

        print(f"Deleting Seat: {temp_node.data}, Address: {curr_node.next}")

        curr_node.next = temp_node.next

    def add_node_at_position(self, position_index, data):
        new_node = SeatNode(data)
        count = 0

        if self.head is None:
            print("The list is empty")
            return

        if position_index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next is not None and position_index - 1 != count:
            count += 1
            curr_node = curr_node.next

        print(f"Add Data: {new_node.data}, Address: {curr_node.next}")

        new_node.next = curr_node.next
        curr_node.next = new_node
    
    def to_print(self):
        # Initialize the temp node to hold the current node
        temp = self.head

        # Check to see if there are no elements in the list
        if self.head is None:
            print("There are no seats in the list")
            return

        # Iterate over each node and print each node's data and pointer address
        while temp is not None:
            print(f"Seat: {temp.data} Address: {temp.next}", end="  |  ")

            # This is how you iterate to the next node in the list
            temp = temp.next

        print()  # Print a newline at the end

class Flight(SingleLinkedSeatingList):
    def __init__(self, flightNumber, departureLocation, arrivalLocation, timeInterval, amountSeats=30, duration=30):
        super().__init__()
        self.flightNumber = flightNumber
        self.departureLocation = departureLocation
        self.arrivalLocation = arrivalLocation

        aval_seating_list = SingleLinkedSeatingList()
        booked_seating_list = SingleLinkedSeatingList()

        # Add seats to the available seats in the linked list
        for i in range(amountSeats):
            if(i % 2 == 0):
                seatNumber = (i // 2 + 1) * 100 + 1
            else:
                seatNumber = (i // 2 + 1) * 100 + 2            
            aval_seating_list.insert_at_end(seatNumber)

        self.aval_seating_list  = aval_seating_list
        self.booked_seating_list = booked_seating_list
        self.timeInterval =timeInterval
        self.duration = duration
    
    def display_flight(self):
        print(f'Flight ID Number: {self.flightNumber}, Departure Location: {self.departureLocation}, Arrival Location: {self.arrivalLocation}, Time Interval: {self.timeInterval}, Time Duration: {self.duration}')

    def main_menu_catalog_seating(self):
        # Initialize variables to store the single linked lists for available and booked seating
        # aval_seating_list = SingleLinkedSeatingList()
        # booked_seating_list = SingleLinkedSeatingList()
        if self is None:
            print("Null Point")
            return 
        
        while True:
            # Create Menu UI options for user to interact with
            print("Flight Reservation Options for Flight: " + str(self.flightNumber))
            print("Departure: " + self.departureLocation)
            print("Arrival: " + self.arrivalLocation)
            print("Time Duration: " + str(self.duration))
            print("")
            print("Event Ticket Booking System: MAIN MENU")
            print("Please Select an Option:")
            print("1. Book a Seat")
            print("2. Cancel a Seat")
            print("3. Show Available Seats (All Booked Seats List)")
            print("4. Exit")
            print("5. Show All Open Seats")

            user_input = input("Insert Operation Number: ")
            print()

            match user_input:
                case "1":
                    print("\nYou selected to Book a Seat")
                    self.booked_seating_list.book_seat(self.aval_seating_list)
                    print()
                case "2":
                    print("\nYou selected to Cancel a Seat")
                    self.booked_seating_list.cancel_a_seat(self.aval_seating_list)
                    print()
                case "3":
                    print("\nYou selected Display Available Seats. (Booked Seats)")
                    self.booked_seating_list.to_print()
                    print()
                case "4":
                    print("\nYou selected to terminate the program. Exiting...")
                    print()
                    exit()
                case "5":
                    print("\nYou selected Display All Open Seats")
                    self.aval_seating_list.to_print()
                    print()
                case _:
                    print("\nYou selected an invalid option. Please reselect your input")
                    print()

    

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
        sizeOfFlightLog = len(self.givenFlights)

        lastKnownEndTime = -1
        index=1 

        dpArray = [1] * sizeOfFlightLog
        previousIndex = [-1] *sizeOfFlightLog

        for index in range(1, sizeOfFlightLog):
            for jindex in range(index):

                curActivityStartTime = self.givenFlights[jindex].timeInterval[0]
                if (self.givenFlights[index].timeInterval[1] <= curActivityStartTime):
                    if (dpArray[index] < dpArray[jindex]+1):
                        dpArray[index] = dpArray[jindex]+1
                        previousIndex[index] = jindex
        
        maxIndex = dpArray.index(max(dpArray))
        while -1 != maxIndex:
            nonOverlapSced.append(sortedFlights[maxIndex])
            maxIndex = previousIndex[maxIndex]
        
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
    

if __name__ == "__main__":
    flightdata = FlightDatabase()
    flightdata.add_flight(Flight(101, "BOS", "CEE", (3,4), 12,  30))
    flightdata.add_flight(Flight(102, "ALT", "BOS", (5,9), 12,  90))
    flightdata.add_flight(Flight(103, "MIA", "LAX", (10,12), 12,  123))
    flightdata.add_flight(Flight(104, "LAX", "ALT", (1,6), 12,  677))
    flightdata.add_flight(Flight(105, "ALT", "LAX", (8,12), 12,  908))
    flightdata.add_flight(Flight(106, "BOS", "ALT", (3,6), 12,  67))
    flightdata.add_flight(Flight(107, "CEE", "MIA", (3,4), 12,  350))
    flightdata.add_flight(Flight(108, "CEE", "LAX", (2,5), 12,  234))
    
    print(flightdata.select_flight_to_book())
   
