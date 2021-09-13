from django.urls import path

from fixture import views

urlpatterns = [
    path('fixture-man-city/', views.FixtureListView.as_view(), name='fixture'),
    path('fixture-real-madrid/', views.FixtureRealMadridListView.as_view(), name='ticket_real'),
    path('checkout/', views.checkout, name='checkout'),
    path('success-purchase/', views.success_purchase, name='success_purchase'),
]
