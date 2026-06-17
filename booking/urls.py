from django.urls import path
from .views import book_ambulance, my_bookings

urlpatterns = [
    path("book/<int:ambulance_id>/", book_ambulance, name="book_ambulance"),
    path("my-bookings/", my_bookings, name="my_bookings"),
]
