from django.urls import path

from ticket import views

urlpatterns = [
    path('ticket-man-city/', views.FixtureListView.as_view(), name='ticket'),
    path('ticket-real-madrid/', views.FixtureRealMadridListView.as_view(), name='ticket_real'),
    path('success-purchase/', views.success_purchase, name='success_purchase'),
    path('checkout/', views.checkout, name='checkout'),
]
