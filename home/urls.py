from django.urls import path

from home import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('become-vip/', views.become_vip, name='become_vip'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('thank-you-for-contact/', views.thx_for_contact, name='thank_you_for_contact'),
    path('search/', views.search_page_view, name='search'),
    path('search-real/', views.search_madrid_view, name='search_madrid'),
    path('search-hospitality/', views.search_hospitality_view, name='search_hospitality'),
    # path('search-hospitality-real/', views.search_hospitality_real_view, name='search_hospitality_real'),
    path('search-tickets/', views.search_fixture_view, name='fixture_search'),
]
