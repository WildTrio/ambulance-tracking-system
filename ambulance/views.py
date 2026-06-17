from django.shortcuts import render
from booking.models import Booking
from .models import Ambulance
import math


def ambulance_map(request):

    ambulances = Ambulance.objects.all()

    ambulance_data = []

    for ambulance in ambulances:
        ambulance_data.append(
            {
                "vehicle": ambulance.vehicle_number,
                "lat": ambulance.latitude,
                "lng": ambulance.longitude,
                "type": ambulance.ambulance_type,
                "status": ambulance.status,
            }
        )

    return render(request, "ambulance/map.html", {"ambulances": ambulance_data})


def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def home(request):

    total_ambulances = Ambulance.objects.count()

    available_ambulances = Ambulance.objects.filter(status="Available").count()

    booked_ambulances = Ambulance.objects.filter(status="Booked").count()

    total_bookings = Booking.objects.count()

    return render(
        request,
        "home.html",
        {
            "total_ambulances": total_ambulances,
            "available_ambulances": available_ambulances,
            "booked_ambulances": booked_ambulances,
            "total_bookings": total_bookings,
        },
    )


def ambulance_list(request):
    ambulances = Ambulance.objects.filter(status="Available")

    return render(request, "ambulance/ambulance_list.html", {"ambulances": ambulances})


def nearest_ambulances(request):
    return render(request, "ambulance/nearest.html")


def ambulances_nearby(request):

    if request.method == "POST":

        user_lat = float(request.POST.get("latitude"))

        user_lon = float(request.POST.get("longitude"))
        print("USER LAT:", user_lat)
        print("USER LON:", user_lon)
        ambulances = Ambulance.objects.filter(status="Available")

        ambulance_distances = []

        for ambulance in ambulances:

            distance = calculate_distance(
                user_lat, user_lon, ambulance.latitude, ambulance.longitude
            )
            print(
                ambulance.vehicle_number,
                ambulance.latitude,
                ambulance.longitude,
                distance,
            )

            ambulance_distances.append(
                {"ambulance": ambulance, "distance": round(distance, 2)}
            )

        ambulance_distances.sort(key=lambda x: x["distance"])

        return render(
            request,
            "ambulance/nearby_results.html",
            {"ambulance_distances": ambulance_distances},
        )

    return render(request, "ambulance/nearest.html")
