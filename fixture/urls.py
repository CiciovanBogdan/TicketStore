from django.urls import path

from fixture import views

urlpatterns = [
    path('ticket-man-city/', views.FixtureListView.as_view(), name='ticket'),
    path('ticket-real-madrid/', views.FixtureRealMadridListView.as_view(), name='ticket_real'),
    path('ticket-man-united/', views.FixtureManUnitedListView.as_view(), name='ticket_man_united'),
    path('ticket-barcelona/', views.FixtureBarcelonaListView.as_view(), name='ticket_barcelona'),
    path('checkout/', views.checkout, name='checkout'),
    path('success-purchase/', views.success_purchase, name='success_purchase'),
]
