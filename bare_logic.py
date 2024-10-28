
class SeatNode:
    def __init__(self, data=0):
        self.data = data
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
    
def main_menu_catalog():
    # Initialize variables to store the single linked lists for available and booked seating
    aval_seating_list = SingleLinkedSeatingList()
    booked_seating_list = SingleLinkedSeatingList()
    max_seat_in_row = 12

    # Add seats to the available seats in the linked list
    for i in range(max_seat_in_row):
        aval_seating_list.insert_at_end(100 + i)

    while True:
        # Create Menu UI options for user to interact with
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
                booked_seating_list.book_seat(aval_seating_list)
                print()
            case "2":
                print("\nYou selected to Cancel a Seat")
                booked_seating_list.cancel_a_seat(aval_seating_list)
                print()
            case "3":
                print("\nYou selected Display Available Seats. (Booked Seats)")
                booked_seating_list.to_print()
                print()
            case "4":
                print("\nYou selected to terminate the program. Exiting...")
                print()
                exit()
            case "5":
                print("\nYou selected Display All Open Seats")
                aval_seating_list.to_print()
                print()
            case _:
                print("\nYou selected an invalid option. Please reselect your input")
                print()

while True:
    main_menu_catalog()