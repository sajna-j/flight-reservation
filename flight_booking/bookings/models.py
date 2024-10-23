from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    total_seats = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.flight_number}: {self.departure} to {self.destination}"

class FlightSeat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.flight.flight_number} - Seat {self.seat_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(FlightSeat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.seat}"