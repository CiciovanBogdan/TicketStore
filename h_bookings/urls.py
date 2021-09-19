from django.urls import path

from h_bookings import views

urlpatterns = [
    path('create-booking/', views.BookingCreateView.as_view(), name='create_booking'),
    path('success-booking/', views.success_booking, name='success_booking')
]
