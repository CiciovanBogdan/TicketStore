from django.urls import path

from cart import views

urlpatterns = [
    path('product-cart/', views.open_cart_view, name='product_cart'),
    path('add-to-cart/', views.add_product_to_cart, name='add_to_cart'),
]
