from django.db import models
from django.contrib.auth.models import User
from ambulance.models import Ambulance

class Booking(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('On The Way', 'On The Way'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    ambulance = models.ForeignKey(
        Ambulance,
        on_delete=models.CASCADE
    )

    pickup_location = models.CharField(max_length=255)

    destination = models.CharField(max_length=255)

    contact_number = models.CharField(max_length=15)

    emergency_description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )