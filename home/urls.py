from django.urls import path

from home import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('become-vip/', views.BecomeVIPListView.as_view(), name='become_vip'),
    path('checkout-vip/', views.checkout_vip, name='checkout_vip'),
    path('success-vip/', views.add_to_member, name='success_vip'),
    path('cancel-vip/', views.remove_from_member, name='cancel_vip_sub'),
    path('create-vip-card/', views.VIPCreateView.as_view(), name='create_vip_card'),
    path('delete-vip-card/<int:pk>/', views.VIPDeleteView.as_view(), name='delete_vip_card'),
    path('update-vip-card/<int:pk>/', views.VIPUpdateView.as_view(), name='update_vip_card'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('thank-you-for-contact/', views.thx_for_contact, name='thank_you_for_contact'),
    path('search-merch-city/', views.search_merch_city, name='search_merch_city'),
    path('search-merch-real/', views.search_merch_real, name='search_merch_real'),
    path('search-merch-united/', views.search_merch_united, name='search_merch_united'),
    path('search-merch-barcelona/', views.search_merch_barcelona, name='search_merch_barcelona'),
    path('search-hospitality/', views.search_hospitality_payed_city, name='search_hospitality_payed_city'),
    path('search-hospitality-barca/', views.search_hospitality_payed_barcelona,
         name='search_hospitality_payed_barcelona'),
    path('search-hospitality-real/', views.search_hospitality_vip_real, name='search_hospitality_vip_real'),
    path('search-hospitality-united/', views.search_hospitality_vip_united, name='search_hospitality_vip_united'),
    path('search-fixture-city/', views.search_fixture_city, name='search_fixture_city'),
    path('search-fixture-real/', views.search_fixture_real, name='search_fixture_real'),
    path('search-fixture-united/', views.search_fixture_man_united, name='search_fixture_united'),
    path('search-fixture-barcelona/', views.search_fixture_barcelona, name='search_fixture_barcelona'),
]
