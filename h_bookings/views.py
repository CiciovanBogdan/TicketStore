from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from h_bookings.forms import BookingForm
from h_bookings.models import Booking


class BookingCreateView(CreateView):
    template_name = 'booking/create_booking.html'
    model = Booking
    form_class = BookingForm
    context_object_name = 'all_bookings'
    success_url = reverse_lazy('success_booking')


def success_booking(request):
    return render(request, 'booking/success_booking.html')
