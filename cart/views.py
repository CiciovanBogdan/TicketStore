from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cart.models import Cart, CartItem


@login_required
def open_cart_view(request):
    open_cart = get_open_cart(request)
    cart_items = CartItem.objects.filter(cart=open_cart)
    return render(request, 'cart/open_cart.html', {'open_cart': open_cart, 'cart_items': cart_items})


@login_required
def add_product_to_cart(request):
    print(request.POST)
    open_cart = get_open_cart(request)
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))
    cart_items = CartItem.objects.filter(cart=open_cart, product_id=product_id)
    if cart_items.count() > 0:
        cart_item: CartItem = cart_items[0]
        cart_item.quantity += quantity
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(product_id=product_id, quantity=quantity, cart=open_cart)
    return redirect(reverse_lazy('product_cart'))


# django query-sets cauta pe google
def get_open_cart(request):
    open_carts = Cart.objects.filter(user=request.user, status='open')
    if open_carts.count() > 0:
        open_cart = open_carts[0]
    else:
        open_cart = Cart.objects.create(user=request.user, status='open')
    return open_cart
