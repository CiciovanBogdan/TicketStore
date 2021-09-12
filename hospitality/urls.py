from django.urls import path

from hospitality import views

urlpatterns = [
    path('hospitality/', views.HospitalityListView.as_view(), name='hospitality'),
    # path('hospitality-real/', views.HospitalityListView.as_view(), name='hospitality'),  # trebe sa il faci ca nu ii bun
    path('create-hospitality/', views.HospitalityCreateView.as_view(), name='create_hospitality'),
    path('update-hospitality/<int:pk>/', views.HospitalityUpdateView.as_view(), name='update_hospitality'),
    path('delete-hospitality/<int:pk>/', views.HospitalityDeleteView.as_view(), name='delete_hospitality'),
]
