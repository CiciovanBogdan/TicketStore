from django.urls import path

from hospitality import views

urlpatterns = [
    path('hospitality/', views.HospitalityListView.as_view(), name='hospitality'),
    path('hospitality-barca/', views.HospitalityBarcaListView.as_view(), name='hospitality_barca'),
    path('hospitality-real/', views.HospitalityVIPListView.as_view(), name='hospitality_real'),
    path('hospitality-united/', views.HospitalityVIPUnitedListView.as_view(), name='hospitality_united'),
    path('create-hospitality/', views.HospitalityCreateView.as_view(), name='create_hospitality'),
    path('create-hospitality-barca/', views.HospitalityBarcaCreateView.as_view(), name='create_hospitality_barca'),
    path('create-hospitality-real/', views.HospitalityVIPCreateView.as_view(), name='create_hospitality_real'),
    path('create-hospitality-united/', views.HospitalityVIPUnitedCreateView.as_view(),
         name='create_hospitality_united'),
    path('update-hospitality/<int:pk>/', views.HospitalityUpdateView.as_view(), name='update_hospitality'),
    path('update-hospitality-barca/<int:pk>/', views.HospitalityBarcaUpdateView.as_view(),
         name='update_hospitality_barca'),
    path('update-hospitality-real/<int:pk>/', views.HospitalityVIPUpdateView.as_view(),
         name='update_hospitality_real'),
    path('update-hospitality-united/<int:pk>/', views.HospitalityVIPUnitedUpdateView.as_view(),
         name='update_hospitality_united'),
    path('delete-hospitality/<int:pk>/', views.HospitalityDeleteView.as_view(), name='delete_hospitality'),
    path('delete-hospitality-barca/<int:pk>/', views.HospitalityBarcaDeleteView.as_view(),
         name='delete_hospitality_barca'),
    path('delete-hospitality-real/<int:pk>/', views.HospitalityVIPDeleteView.as_view(),
         name='delete_hospitality_real'),
    path('delete-hospitality-united/<int:pk>/', views.HospitalityVIPUnitedDeleteView.as_view(),
         name='delete_hospitality_united'),
]
