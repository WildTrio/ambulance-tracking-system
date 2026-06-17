from django.contrib.auth.models import User
from django.test import TestCase

from ambulance.models import Ambulance
from .models import Booking


class BookingAmbulanceStatusTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="patient",
            password="password123",
        )
        self.ambulance = Ambulance.objects.create(
            vehicle_number="AMB-001",
            driver_name="Driver One",
            driver_phone="9999999999",
            ambulance_type="Basic",
            latitude=12.9716,
            longitude=77.5946,
            status="Booked",
        )

    def create_booking(self, status="Pending"):
        return Booking.objects.create(
            user=self.user,
            ambulance=self.ambulance,
            pickup_location="Hospital Road",
            destination="City Hospital",
            contact_number="8888888888",
            emergency_description="Emergency pickup",
            status=status,
        )

    def refresh_ambulance(self):
        self.ambulance.refresh_from_db()
        return self.ambulance

    def test_pending_booking_sets_ambulance_available(self):
        self.create_booking(status="Pending")

        self.assertEqual(
            self.refresh_ambulance().status,
            "Available",
        )

    def test_completed_booking_sets_ambulance_available(self):
        booking = self.create_booking(status="Accepted")

        booking.status = "Completed"
        booking.save()

        self.assertEqual(
            self.refresh_ambulance().status,
            "Available",
        )

    def test_cancelled_booking_sets_ambulance_available(self):
        booking = self.create_booking(status="Accepted")

        booking.status = "Cancelled"
        booking.save()

        self.assertEqual(
            self.refresh_ambulance().status,
            "Available",
        )

    def test_active_booking_statuses_set_ambulance_booked(self):
        booking = self.create_booking(status="Pending")

        for status in ("Accepted", "On The Way"):
            booking.status = status
            booking.save()

            self.assertEqual(
                self.refresh_ambulance().status,
                "Booked",
            )
