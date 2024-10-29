#include <iostream>

using namespace std;

// to define a node class that represents
class SeatNode{

public:

    // initialize the attributes the makeup a seat.
    int data;
    SeatNode *next;

    // default constructor to define seat
    SeatNode(){
        data = 0;
        next=NULL;
    }

    // constructor to define seat
    SeatNode(int data){
        this->data = data;
        this->next=NULL;
    }
};


// to represent a single linked list class.
class SingleLinkedSeatingList{

public:

    SeatNode *head;
    SingleLinkedSeatingList(){
        head=NULL;
    }

    // to insert a new node in the linked list at the headTop of the single linked list
    void insertHead(int data){

        //create a new node pointer object
        SeatNode* newNode = new SeatNode(data);
        if(head==NULL){
            head=newNode;
            return;
        }

        //re-assign the address to allow new Node to be added to the front of the list
        newNode->next = this->head;
        this->head=newNode;
    }

    // to insert a new node in the linked list at the end or tail of the single linked list
    void insertAtEnd(int value){

        //create a new node pointer object
        SeatNode* newNode = new SeatNode(value);
        if(head==NULL){
            head=newNode;
        }
        else{

            //create a temporary node
            SeatNode* temp = head;

            // iterate through the linked list until the tempNode
            // reaches the last element in the linked list
            while(temp->next != NULL){
                temp=temp->next;
            }

            // assign the last element of the linked list to the new node
            temp->next = newNode;
        }
    }

    // to allow the user to book a seat based on the given a hand selected availability list
    void bookSeat(SingleLinkedSeatingList &availableSeatList){

        // to allow the user to book a seat based on the user input
        int userSeatInput;
        cout << "Please enter a seat number to book: ";
        cin >> userSeatInput;

        // to iterate over the current seat availability list to check if the seat is available to be booked.
        SeatNode* currAvailableSeatNode = availableSeatList.head;

        // initialize a count to keep track of the of where the available seat is located in the available seat list
        int indexCount = 0;
        while(currAvailableSeatNode->next != nullptr && currAvailableSeatNode->data != userSeatInput){
            // Since Linked Lists have no index keep count
            indexCount++;

            // iterate over the available seat list through recursion
            currAvailableSeatNode =  currAvailableSeatNode->next;
        }

        // check to see if the user's input is valid and allowed to be selected to be booked
        if(userSeatInput == currAvailableSeatNode->data){

            // to insert the selected seat in the book list.
            insertAtEnd(userSeatInput);
            cout << "Seat " << userSeatInput << " has been booked" << endl;
            cout << endl;

            // Print Booked Seating List with new changeS
            cout << "Seat " << userSeatInput << " has been added to the BOOKED LIST" << endl;
            toPrint();

            cout << endl;
            // delete the booked seat from the available list as it is not available no more
            cout << "Delete Seat: " << userSeatInput << " from the AVAILABLE LIST" << endl;
            availableSeatList.deleteNodeAtPosition(indexCount);
            cout << endl;

            return;

        }
        else{

            // else case is to notify user to understand that the input was invalid.
            cout << "Sorry the seat you entered was can't be booked" << endl;
            toPrint();
            cout<<endl;
            return;
        }

    }

    // to allow the user to cancel a seat reservation from the booked list
    void cancelASeat(SingleLinkedSeatingList &availableSeatList){

        // to allow user input to select a seat to cancel
        int userSeatInput;
        cout << "Please enter a seat number to cancel: ";
        cin >> userSeatInput;

        // check if the booked list has nothing in it.
        if(head == NULL){

            // if it is true then throw an error.
            cout << "You can't cancel the seat. ERROR No Seats in Booked List to cancel";
            return;
        }

        // initialize a node that represents the current seat of the booked list
        SeatNode* currBookedSeatNode = head;

        // to keep count for the index of where the current booked seat is located
        int indexCount = 0;

        // to iterate over the booked seat list to see if that the user wanted to cancel exits in the booked list
        while(currBookedSeatNode->next != nullptr && currBookedSeatNode->data != userSeatInput){
            indexCount++;
            // Since Linked Lists have no index keep count
            currBookedSeatNode = currBookedSeatNode->next;
        }

        // to check if the seat that the seat the user wants to cancel is in the booked list node
        if(currBookedSeatNode->data == userSeatInput){

            // initialize a node that represents the current seat of the available list
            SeatNode* currAvalSeatNode = availableSeatList.head;

            // initialize a count to keep track where to place the removed booked seat
            // back into the available seating list.
            int indexCountAval = 0;

            // remove the cancelled seat from the booked list
            cout << "Seat " << userSeatInput << " has been cancelled" <<endl;
            cout << endl;
            cout << "Delete Seat: " << userSeatInput << " from the BOOKED LIST" <<endl;
            deleteNodeAtPosition(indexCount);

            // to iterate over the available seat list to check
            // where to put back the canceled seat into the available list to maintain the chronological order.
            while(currAvalSeatNode->next != nullptr && userSeatInput > currAvalSeatNode->data){

                // Since Linked Lists have no index keep count
                currAvalSeatNode =  currAvalSeatNode->next;
                indexCountAval++;
            }

            // add the removed booked seat into the available seat list
            cout << endl;
            cout << "Add Seat: " << userSeatInput << " to the AVAILABLE LIST" <<endl;
            availableSeatList.addNodeAtPosition(indexCountAval, userSeatInput);
        }
        else{
            // Notify user that the input was invalid
            cout << "Sorry this seat cannot be cancelled" <<endl;
        }

    }




    // to remove the node in a single linked list at a given position index
    void deleteNodeAtPosition(int positionIndex){

        // initialize the count
        int count = 0;

        // Check Empty Case
        if(head == NULL){
            cout<<"The list is empty" << endl;
            return;
        }

        // Check if the user wants to remove a node at the start of the single linked list.
        if (positionIndex == 0){
            SeatNode* temp = head;
            head=temp->next;
            return;
        }

        // Traverse and Iterate over the linked list until you reach the node the user wants to remove
        SeatNode* curr_Node = head;
        while(curr_Node->next != nullptr && positionIndex-1 != count){

            // Since Linked Lists have no index keep count
            count += 1;
            curr_Node =  curr_Node->next;
        }

        // to get the node you want to remove
        SeatNode *tempNode = curr_Node->next;

        cout << "Deleting Seat: " << tempNode->data << ", Address: " << curr_Node->next << endl;

        // reassign the addressing
        curr_Node->next = tempNode->next;

        //delete the node
        delete tempNode;

    }

    // to add node at a given position
    void addNodeAtPosition(int positionIndex, int data){

        // initalize new node to be added to the linked list
        SeatNode* newNode = new SeatNode(data);

        // keep count to keep track the nodes in the linked list
        int count = 0;

        // check empty case
        if(head == NULL){

            // throw an error since the linked list is a null pointer
            cout<<"The list is empty" << endl;
            return;
        }

        // check to see if the user selected to insert the node at the head.
        if(positionIndex == 0){

            // insert the node at the start of the linked list
            newNode->next = head;
            head = newNode;
            return;
        }

        // traverse and iterate over each node linked list
        // until you reach the previous node before you place your new node
        SeatNode* currNode = head;
        while(currNode->next != nullptr && positionIndex - 1 != count){

            // Since Linked Lists have no index keep count
            count += 1;
            currNode =  currNode->next;
        }


        cout << "Add Data:" << newNode->data << ", Address: " << currNode->next << endl;


        // reassign the addressing to allow the new node to be placed in the linked list
        newNode->next = currNode->next;
        currNode->next = newNode;


    }


    // to print the linked list
    void toPrint(){

        // to initalize the temp node to hold the current node
        SeatNode *temp=head;

        // check to see if there are no elements in the list
        if(head==NULL){
            cout << "There is no seats in list" << endl;
            return;
        }

        // iterate over each node and print the each node's data and pointer address
        while(temp!=NULL){
            cout<< "Seat:" << temp->data << " Address:" << temp->next<< "  |  ";

            //this is how you iterate ove next node in list
            temp = temp->next;
        }
        cout<<endl;
    }

};

// create a main menu to allow the user to interact with in the booking seat automation system
void mainMenuCatalog(){

    // initialize a variable to store the user input
    string userInput;

    // initialize a variable to store the single linked list for the available seating list
    SingleLinkedSeatingList avalSeatingList;

    // initialize a variable to store the single linked list for the booked seating list
    SingleLinkedSeatingList bookedSeatingList;
    int maxSeatInRow = 12;

    // Add seats to the available seats in the linked list
    for(int i = 0; i < maxSeatInRow; i++){
        avalSeatingList.insertAtEnd(100 + i);
    }


    while(true) {

        // Create Menu UI options for user to interact with.
        cout << "Event Ticket Booking System: MAIN MENU";
        cout << endl;
        cout << "Please Select an Option: "<< endl;
        cout << "1. Book a Seat" << endl;
        cout << "2. Cancel a Seat" << endl;
        cout << "3. Show Available Seats (All Booked Seats List)" << endl;
        cout << "4. Exit" << endl;
        cout << "5. Show All Open Seats" << endl;

        cout << "Insert Operation Number: ";
        cin >> userInput;
        cout << endl;


        if(userInput == "1"){
            cout << endl;
            cout << "You selected to Book a Seat" << endl;
            bookedSeatingList.bookSeat(avalSeatingList);
            cout << endl;
        }
        else if(userInput == "2"){
            cout << endl;
            cout << "You selected to Cancel a Seat" << endl;
            bookedSeatingList.cancelASeat(avalSeatingList);
            cout << endl;
        }
        else if(userInput == "3"){
            cout << endl;
            cout << "You selected Display Available Seats. (Booked Seats)" << endl;
            bookedSeatingList.toPrint();
            cout << endl;
        }
        else if(userInput == "4"){
            cout << endl;
            cout << "You selected to terminate the program. Please reselect you input" << endl;
            cout << endl;
            break;
        }
        else if(userInput == "5"){
            cout << endl;
            cout << "You selected Display All Open Seats" << endl;
            avalSeatingList.toPrint();
            cout << endl;
        }
        else{
            cout << endl;
            cout << "You selected an invalid option. Please reselect you input" << endl;
            cout << endl;
        }

    }
};


int main() {
    mainMenuCatalog();
}
