from django.urls import path

from merch import views

urlpatterns = [
    path('merch/', views.MerchListView.as_view(), name='merch'),
    path('merch-real/', views.MerchRealListView.as_view(), name='merch_real'),
    path('merch-united/', views.MerchManUnitedListView.as_view(), name='merch_united'),
    path('merch-barcelona/', views.MerchBarcelonaListView.as_view(), name='merch_barcelona'),
    path('create-merch/', views.MerchCreateView.as_view(), name='create_merch'),
    path('update-merch/<int:pk>/', views.MerchUpdateView.as_view(), name='update_merch'),
    path('delete-merch/<int:pk>/', views.MerchDeleteView.as_view(), name='delete_merch'),
    path('buy-product/<int:pk>/', views.MerchDetailView.as_view(), name='buy_product'),
    path('final-details/', views.final_details, name='final_details'),
    path('checkout-merch/', views.checkout_merch, name='checkout_merch'),  # loc pt checkout merch
    path('final-purchse-details/<int:pk>/', views.MerchFinalDetailView.as_view(), name='final_purchase_details'),
]
