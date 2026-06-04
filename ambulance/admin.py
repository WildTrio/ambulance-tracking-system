from django.contrib import admin
from .models import Ambulance


@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle_number",
        "driver_name",
        "driver_phone",
        "ambulance_type",
        "status",
        "latitude",
        "longitude",
    )
    list_filter = (
        "status",
        "ambulance_type",
    )
    search_fields = (
        "vehicle_number",
        "driver_name",
        "driver_phone",
        "ambulance_type",
    )
    ordering = (
        "vehicle_number",
    )
