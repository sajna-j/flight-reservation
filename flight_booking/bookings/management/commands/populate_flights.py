from django.core.management.base import BaseCommand
from django.utils import timezone
from bookings.models import Flight

class Command(BaseCommand):
    help = 'Populates the database with 10 specific example flights'

    def handle(self, *args, **kwargs):
        # List of 10 specific flights
        flights = [
            {
                'flight_number': 'AA123',
                'departure': 'New York (JFK)',
                'destination': 'Los Angeles (LAX)',
                'departure_time': timezone.now() + timezone.timedelta(days=1, hours=10),
                'total_seats': 30
            },
            {
                'flight_number': 'BB145',
                'departure': 'London (LHR)',
                'destination': 'Paris (CDG)',
                'departure_time': timezone.now() + timezone.timedelta(days=2, hours=5),
                'total_seats': 20
            },
            {
                'flight_number': 'CC345',
                'departure': 'Tokyo (HND)',
                'destination': 'Singapore (SIN)',
                'departure_time': timezone.now() + timezone.timedelta(days=1, hours=15),
                'total_seats': 10
            },
            {
                'flight_number': 'DD567',
                'departure': 'Dubai (DXB)',
                'destination': 'Sydney (SYD)',
                'departure_time': timezone.now() + timezone.timedelta(days=3, hours=8),
                'total_seats': 35
            },
            {
                'flight_number': 'EE789',
                'departure': 'Chicago (ORD)',
                'destination': 'Miami (MIA)',
                'departure_time': timezone.now() + timezone.timedelta(days=2, hours=12),
                'total_seats': 28
            },
            {
                'flight_number': 'FF234',
                'departure': 'San Francisco (SFO)',
                'destination': 'Seattle (SEA)',
                'departure_time': timezone.now() + timezone.timedelta(days=1, hours=6),
                'total_seats': 50
            },
            {
                'flight_number': 'GG678',
                'departure': 'Berlin (BER)',
                'destination': 'Rome (FCO)',
                'departure_time': timezone.now() + timezone.timedelta(days=4, hours=3),
                'total_seats': 25
            },
            {
                'flight_number': 'HH901',
                'departure': 'Toronto (YYZ)',
                'destination': 'Vancouver (YVR)',
                'departure_time': timezone.now() + timezone.timedelta(days=2, hours=18),
                'total_seats': 30
            },
            {
                'flight_number': 'II345',
                'departure': 'Mexico City (MEX)',
                'destination': 'Buenos Aires (EZE)',
                'departure_time': timezone.now() + timezone.timedelta(days=3, hours=22),
                'total_seats': 20
            },
            {
                'flight_number': 'JJ789',
                'departure': 'Amsterdam (AMS)',
                'destination': 'Barcelona (BCN)',
                'departure_time': timezone.now() + timezone.timedelta(days=5, hours=7),
                'total_seats': 28
            },
        ]

        for flight_data in flights:
            flight, created = Flight.objects.get_or_create(
                flight_number=flight_data['flight_number'],
                defaults={
                    'departure': flight_data['departure'],
                    'destination': flight_data['destination'],
                    'departure_time': flight_data['departure_time'],
                    'total_seats': flight_data['total_seats']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created flight: {flight.flight_number}"))
            else:
                self.stdout.write(self.style.WARNING(f"Flight {flight.flight_number} already exists"))

        self.stdout.write(self.style.SUCCESS('Successfully populated flights'))