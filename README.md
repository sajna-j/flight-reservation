# flight-reservation

***Initial Setup:***
1. In your VSCode terminal, cd into the "flight_booking" folder for all the following steps 
2. run `python manage.py makemigrations`
3. run `python manage.py migrate`
4. run `python manage.py createsuperuser`
    This will ask you to come up with an admin username, password, and email
    - just use anything simple you will remember (like user: bob, password: bob, email: bob@bob.com, it really doesn't matter)
    - this username and password will really only live on your own machine 
    By creating this admin user, you can get access to a Django admin website page that lets you view/edit all the Flights/Seats/Everything much easier
5. populate some sample data of flights with `python manage.py populate_flights`
6. To run the server itself:
    run `python manage.py runserver`
7. go to the website link it says it just made, probably something like `http://127.0.0.1:8000/`
8. by adding `admin/` to the end of the link, you can enter the admin page
    (`http://127.0.0.1:8000/admin/`)

***Working with instances of Flights/Seats/Etc. (Models)***
Option 1. (I suggest this for creating/editing)

    - Through the Django Admin Site

    1. run the server & get on the admin page (step 6 & 7 above)

    
    2. log in with the user you created in step 4
    
    3. click on Flights for example, to see all the Flights that have existed so far, or create a new one!
    
        - when you click on an existing one, you should have edit access to that flight (bc you're an admin)
    
        - any changes you make like this will ONLY exist on your machine
    
        - if you want to create some example objects that everyone on the repository can see, create a script that initializes 
        some (for example, `bookings/management/commands/populate_flights.py`)

Option 2. (I suggest this for deleting/viewing/experimenting)

    - Through the Django Shell CLI (Command Line Interface)

    Essentially a python shell that lets you work with all the objects you've made on your machine like a debug console

    1. from the `flight_booking` folder, run `python manage.py shell`

    2. You've entered a python terminal, you can run any python lines

        try importing the flight model by running `from bookings.models import Flight`

    3. view all the Flight objects by running `Flight.objects.all()`  (Returns a QuerySet with all of them)

    4. grab all the flight objects (as a QuerySet) with certain qualities using `.filter()` like `Flight.objects.filter
    (total_seats=30)`
    
    5. grab a single fligh object with `.get()` like `Flight.objects.get(flight_number='AA123')` (this returns the first object 
    that matches the specifications you provided it)
    
    6. DONT DO THIS RN, but in the future if you need to delete an object, use `.delete()` on a QuerySet or a specific object itself

***Writing Code***

Consider every Class you typically make in code as a "Model"

These "Models" will be defined in the `bookings/models.py` file (Flight, and FlightSeat exist already)

You should register each new model you want viewable/editable on the admin site by adding it to the `flight_bookings\bookings\admin.py` file 

The `bookings\urls.py` file serves as a router for certain links to get the information they need:
    For example, if you wanted to get all the flights in the system, you would go to `http://127.0.0.1:8000/api/flights/` 




