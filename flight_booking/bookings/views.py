from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Flight, FlightSeat, Booking

def flight_list(request):
    flights = Flight.objects.all()
    data = [{"id": flight.id, "flight_number": flight.flight_number, "departure": flight.departure, "destination": flight.destination} for flight in flights]
    return JsonResponse(data, safe=False)

def flight_seats(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    seats = FlightSeat.objects.filter(flight=flight)
    data = [{"id": seat.id, "seat_number": seat.seat_number, "is_booked": seat.is_booked} for seat in seats]
    return JsonResponse(data, safe=False)

@login_required
@require_POST
def book_seat(request, seat_id):
    seat = get_object_or_404(FlightSeat, id=seat_id)
    
    if seat.is_booked:
        return JsonResponse({"error": "This seat is already booked"}, status=400)
    
    booking = Booking.objects.create(user=request.user, seat=seat)
    seat.is_booked = True
    seat.save()
    
    return JsonResponse({"message": "Seat booked successfully", "booking_id": booking.id})