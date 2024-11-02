from Seats import SingleLinkedSeatingList
from collections import deque
import random

class Flight(SingleLinkedSeatingList):
    def __init__(self, flightNumber, departureLocation, arrivalLocation, timeInterval, amountSeats=30, duration=30):
        super().__init__()
        self.flightNumber = flightNumber
        self.departureLocation = departureLocation
        self.arrivalLocation = arrivalLocation

        aval_seating_list = SingleLinkedSeatingList()
        booked_seating_list = SingleLinkedSeatingList()

        first_class_count = int(amountSeats * 0.2)
        business_class_count = int(amountSeats * 0.25)
        economy_class_count = amountSeats - (first_class_count + business_class_count)

        # Add seats to the available seats in the linked list
        for i in range(amountSeats):
            if(i % 2 == 0):
                seatNumber = (i // 2 + 1) * 100 + 1
            else:
                seatNumber = (i // 2 + 1) * 100 + 2    
            
            if(i < first_class_count):

                costSeat = round(20*first_class_count + random.uniform(8, 10)*duration + random.uniform(1, 10), 2)
                classStatus = "First"
            elif(first_class_count <= i < (first_class_count + business_class_count)):

                costSeat = round(0*business_class_count + random.uniform(5, 6)*duration + random.uniform(1, 10), 2)
                classStatus = "Business"
            else:

                costSeat = round(2*economy_class_count + random.uniform(1, 2)*duration + random.uniform(1, 10), 2)
                classStatus = "Economy"
            
            aval_seating_list.insert_at_end_status_cost_distrib(seatNumber, classStatus, costSeat)

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
            print("5. Show All Open Seats:")
            print("6. Sort By Seats Cost:")
            print("7. Sort By Seat Num:")

            user_input = input("Insert Operation Number: ")
            print()

            match user_input:
                case "1":
                    print("\nYou selected to Book a Seat")
                    self.aval_seating_list.sortBySeatNum()
                    self.booked_seating_list.book_seat(self.aval_seating_list)
                    print()
                case "2":
                    print("\nYou selected to Cancel a Seat")
                    self.aval_seating_list.sortBySeatNum()
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
                case "6":
                    print("\nYou selected Sort Seat by Cost")
                    self.aval_seating_list.sortBySeatCost()
                    self.aval_seating_list.to_print()
                    print()
                case "7":
                    print("\nYou selected Sort Seat by Num")
                    self.aval_seating_list.sortBySeatNum()
                    self.aval_seating_list.to_print()
                    print()
                case _:
                    print("\nYou selected an invalid option. Please reselect your input")
                    print()
