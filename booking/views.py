from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from .models import Booking
from ambulance.models import Ambulance


@login_required
def book_ambulance(request, ambulance_id):

    ambulance = get_object_or_404(
        Ambulance,
        id=ambulance_id
    )

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user

            booking.ambulance = ambulance

            booking.save()

            ambulance.status = "Booked"
            ambulance.save()

            return redirect('my_bookings')

    else:
        form = BookingForm()

    return render(
        request,
        'booking/booking_form.html',
        {
            'form': form,
            'ambulance': ambulance
        }
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'booking/my_bookings.html',
        {
            'bookings': bookings
        }
    )