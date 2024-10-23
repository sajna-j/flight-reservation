from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/<int:flight_id>/seats/', views.flight_seats, name='flight_seats'),
    path('book-seat/<int:seat_id>/', views.book_seat, name='book_seat'),
]