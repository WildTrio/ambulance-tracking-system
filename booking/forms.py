from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "pickup_location",
            "destination",
            "contact_number",
            "emergency_description",
        ]
