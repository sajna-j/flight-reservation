from collections import deque
import random

class SeatNode:
    def __init__(self, data=0, status= "Economy", cost=100):
        self.data = data
        self.status = status
        self.cost = cost
        self.next = None
    
    def as_dict(self):
        return {
            "seat_number": self.data,
            "status": self.status,
            "cost": self.cost
        }

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
    
    def insert_at_end_status_cost_distrib(self, seatNum, cost, stat):
        new_node = SeatNode(seatNum, cost, stat)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        
    def swap(self, a, b):
        #check if both nodes exist
        if(a is None or b is None):
            print("Null pointer throw error")
            return

        # check if it is a duplicate case
        if(a == b):
            return
        

        # initialize variables to store to determine the current place for each node in the list
        # I have to do this since there are no index in linked list
        prevNodeA = None
        prevNodeB = None
        curNode = self.head

        # iterate throughout the whole list and get the known previous nodes for A and B
        while(curNode is not None):

            # check if a is the next node for the current node being checked
            if(curNode.next == a):
                prevNodeA = curNode
            
            elif(curNode.next == b):
                prevNodeB = curNode
            
            curNode = curNode.next

        # check to see if the prevNodeA was the start of the list
        if(prevNodeA is not None):

            #if true set previous node of a to be node b
            prevNodeA.next = b
        else:

            # if false set the head of the list to be b
            self.head = b
        

        #check to see if the prevNodeB was the start of the list
        if(prevNodeB is not None):

            # if true set previous node of b to be node a
            prevNodeB.next = a
    
        else:

            # if false set the head of the list to be a
            self.head = a

        # checking any adjacent nodes to be swapped
        if(a.next == b):
            a.next = b.next
            b.next = a
        
        elif(b.next == a):
            b.next = a.next
            a.next = b
        
        else:
            # rearrange and swap the pointers of a and b
            temp = a.next
            a.next = b.next
            b.next = temp
    
    def sortBySeatCost(self):

        # check if the list exists
        if(self.head is None):
           print("Throw Error: List does not exist")
           return
        

        # initialize a flag to check if the songs are required to swap
        swappingNodeFlag = True;


        # iterate over the amount of swaps necessary to properly sort the list in lexicographical order
        while(swappingNodeFlag):

            # to set the flag to be false to end the program if the swaps are not needed in the bubble sort algorithm
            # which indicates the sorting is completed
            swappingNodeFlag = False

            # Start at the head of the list at each known swapping pass
            curNode = self.head

            # iterate and traverse through the current song in the list and the next song in list and compare each song
            # do the required sorting and comparisons until you reach the end of the list
            while (curNode is not None and curNode.next is not None):
                futureNode = curNode.next
                # check to see if the current song name lexicographically comes before the next song in the list
                if (curNode.cost > futureNode.cost):

                    # this condition is reached if the current song should not be going before the next song
                    # swap the positions of the current node and the next node seen in the list
                    self.swap(curNode, futureNode)

                    # set the swap flag to true to continue doing the bubble sort algorithm
                    swappingNodeFlag = True

                # reassign pointers to make the next item of the list be the current node
                curNode = curNode.next
    

    def sortBySeatNum(self):

        # check if the list exists
        if(self.head is None):
           print("Throw Error: List does not exist")
           return
        

        # initialize a flag to check if the songs are required to swap
        swappingNodeFlag = True;


        # iterate over the amount of swaps necessary to properly sort the list in lexicographical order
        while(swappingNodeFlag):

            # to set the flag to be false to end the program if the swaps are not needed in the bubble sort algorithm
            # which indicates the sorting is completed
            swappingNodeFlag = False

            # Start at the head of the list at each known swapping pass
            curNode = self.head

            # iterate and traverse through the current song in the list and the next song in list and compare each song
            # do the required sorting and comparisons until you reach the end of the list
            while (curNode is not None and curNode.next is not None):

                # check to see if the current song name lexicographically comes before the next song in the list
                if (curNode.data > curNode.next.data):

                    # this condition is reached if the current song should not be going before the next song
                    # swap the positions of the current node and the next node seen in the list
                    self.swap(curNode, curNode.next)

                    # set the swap flag to true to continue doing the bubble sort algorithm
                    swappingNodeFlag = True

                # reassign pointers to make the next item of the list be the current node
                curNode = curNode.next

    def sortBySeatStatus(self):

        # check if the list exists
        if(self.head is None):
           print("Throw Error: List does not exist")
           return
        

        # initialize a flag to check if the songs are required to swap
        swappingNodeFlag = True;


        # iterate over the amount of swaps necessary to properly sort the list in lexicographical order
        while(swappingNodeFlag):

            # to set the flag to be false to end the program if the swaps are not needed in the bubble sort algorithm
            # which indicates the sorting is completed
            swappingNodeFlag = False

            # Start at the head of the list at each known swapping pass
            curNode = self.head

            # iterate and traverse through the current song in the list and the next song in list and compare each song
            # do the required sorting and comparisons until you reach the end of the list
            while (curNode is not None and curNode.next is not None):

                # check to see if the current song name lexicographically comes before the next song in the list
                if (curNode.status > curNode.status):

                    # this condition is reached if the current song should not be going before the next song
                    # swap the positions of the current node and the next node seen in the list
                    self.swap(curNode, curNode.next)

                    # set the swap flag to true to continue doing the bubble sort algorithm
                    swappingNodeFlag = True

                # reassign pointers to make the next item of the list be the current node
                curNode = curNode.next

    def book_seat(self, available_seat_list):
        user_seat_input = int(input("Please enter a seat number to book: "))

        curr_available_seat_node = available_seat_list.head
        index_count = 0

        while curr_available_seat_node.next is not None and curr_available_seat_node.data != user_seat_input:
            index_count += 1
            curr_available_seat_node = curr_available_seat_node.next

        if user_seat_input == curr_available_seat_node.data:
            self.insert_at_end_status_cost_distrib(user_seat_input, curr_available_seat_node.cost, curr_available_seat_node.status)
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
            available_seat_list.add_node_at_position(index_count_aval, user_seat_input, curr_aval_seat_node.cost, curr_aval_seat_node.status)
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

    def add_node_at_position(self, position_index, data, overallCost, stat):
        new_node = SeatNode(data, overallCost, stat)
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

    def get_seat(self, seat_number):
        curr_available_seat_node = self.aval_seating_list.head
        index_count = 0

        while curr_available_seat_node.next is not None and curr_available_seat_node.data != seat_number:
            index_count += 1
            curr_available_seat_node = curr_available_seat_node.next

        return curr_available_seat_node if curr_available_seat_node.data == seat_number else None
    
    def to_print(self):
        # Initialize the temp node to hold the current node
        temp = self.head

        # Check to see if there are no elements in the list
        if self.head is None:
            print("There are no seats in the list")
            return

        # Iterate over each node and print each node's data and pointer address
        while temp is not None:
            print(f"Seat: {temp.data}, Type: {temp.status}, Cost: {temp.cost}", end="  |  ")

            # This is how you iterate to the next node in the list
            temp = temp.next

        print()  # Print a newline at the end

    def as_list(self):
        """ JSONifyable represention of the linked list """
        temp = self.head
        seats_list = []
        while temp is not None:
            print(f"Seat: {temp.data}, Type: {temp.status}, Cost: {temp.cost}", end="  |  ")
            seats_list.append(temp.as_dict())
            temp = temp.next
        return seats_list