from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "ambulance",
        "user",
        "pickup_location",
        "destination",
        "contact_number",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "created_at",
        "ambulance__ambulance_type",
    )
    search_fields = (
        "ambulance__vehicle_number",
        "user__username",
        "pickup_location",
        "destination",
        "contact_number",
        "emergency_description",
    )
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
