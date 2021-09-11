from django.urls import path

from home import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('become-vip/', views.become_vip, name='become_vip'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('thank-you-for-contact/', views.thx_for_contact, name='thank_you_for_contact'),
]
