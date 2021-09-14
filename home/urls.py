from django.urls import path

from home import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('become-vip/', views.BecomeVIPListView.as_view(), name='become_vip'),
    path('checkout-vip/', views.checkout_vip, name='checkout_vip'),
    path('success-vip/', views.add_to_member, name='success_vip'),
    path('create-vip-card/', views.VIPCreateView.as_view(), name='create_vip_card'),
    path('delete-vip-card/<int:pk>/', views.VIPDeleteView.as_view(), name='delete_vip_card'),
    path('update-vip-card/<int:pk>/', views.VIPUpdateView.as_view(), name='update_vip_card'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('thank-you-for-contact/', views.thx_for_contact, name='thank_you_for_contact'),
    path('search/', views.search_page_view, name='search'),
    path('search-real/', views.search_madrid_view, name='search_madrid'),
    path('search-hospitality/', views.search_hospitality_view, name='search_hospitality'),
    path('search-hospitality-real/', views.search_hospitality_real_view, name='search_hospitality_real'),
    path('search-tickets-man-city/', views.search_man_city_fixture, name='search_fixture_man_city'),
    path('search-tickets-real-madrid/', views.search_real_madrid_fixture, name="search_fixture_real_madrid"),
]
