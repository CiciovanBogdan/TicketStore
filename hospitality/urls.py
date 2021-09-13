from django.urls import path

from hospitality import views

urlpatterns = [
    path('hospitality/', views.HospitalityListView.as_view(), name='hospitality'),
    path('hospitality-real/', views.HospitalityRealListView.as_view(), name='hospitality_real'),
    path('create-hospitality/', views.HospitalityCreateView.as_view(), name='create_hospitality'),
    path('create-hospitality-real/', views.HospitalityRealCreateView.as_view(), name='create_hospitality_real'),
    path('update-hospitality/<int:pk>/', views.HospitalityUpdateView.as_view(), name='update_hospitality'),
    path('update-hospitality-real/<int:pk>/', views.HospitalityRealUpdateView.as_view(),
         name='update_hospitality_real'),
    path('delete-hospitality/<int:pk>/', views.HospitalityDeleteView.as_view(), name='delete_hospitality'),
    path('delete-hospitality-real/<int:pk>/', views.HospitalityRealDeleteView.as_view(),
         name='delete_hospitality_real'),
]
