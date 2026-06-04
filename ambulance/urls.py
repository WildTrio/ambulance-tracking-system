from django.urls import path
from .views import (
    home,
    ambulance_list,
    nearest_ambulances,
    ambulances_nearby,
    ambulance_map
)

from .views import (
    home,
    ambulance_list,
    nearest_ambulances,
    ambulances_nearby
)

urlpatterns = [
    path('', home, name='home'),

    path(
        'ambulances/',
        ambulance_list,
        name='ambulance_list'
    ),

    path(
        'nearest/',
        nearest_ambulances,
        name='nearest_ambulances'
    ),

    path(
        'ambulances-nearby/',
        ambulances_nearby,
        name='ambulances_nearby'
    ),

    path(
        'map/',
        ambulance_map,
        name='ambulance_map'
    ),
]