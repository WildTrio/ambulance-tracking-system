from django.db import models

class Ambulance(models.Model):
    vehicle_number = models.CharField(max_length=20)

    driver_name = models.CharField(max_length=100)

    driver_phone = models.CharField(max_length=15)

    ambulance_type = models.CharField(max_length=50)

    latitude = models.FloatField()

    longitude = models.FloatField()

    status = models.CharField(
        max_length=20,
        default='Available'
    )

    def __str__(self):
        return self.vehicle_number