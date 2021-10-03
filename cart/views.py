from functools import reduce

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from cart.models import Cart, CartItem


@login_required
def open_cart_view(request):
    open_cart = get_open_cart(request)
    cart_items = CartItem.objects.filter(cart=open_cart)
    cart_items_with_totals = list(
        map(lambda cart_item: {'cart_item': cart_item, 't_price': cart_item.product.price * cart_item.quantity},
            cart_items))
    final_total = reduce(lambda first, second: first + second['t_price'], cart_items_with_totals, 0)
    return render(request, 'cart/open_cart.html',
                  {'open_cart': open_cart,
                   'cart_items_with_totals': cart_items_with_totals,
                   'final_total': final_total})


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


def get_open_cart(request):
    open_carts = Cart.objects.filter(user=request.user, status='open')
    if open_carts.count() > 0:
        open_cart = open_carts[0]
    else:
        open_cart = Cart.objects.create(user=request.user, status='open')
    cart_items = CartItem.objects.filter(cart=open_cart)
    for cart_item in cart_items:
        if cart_item.quantity <= 0:
            cart_item.delete()
    return open_cart


def cart_update(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    quantity = int(request.POST.get('quantity', 1))
    if cart_item.quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        return HttpResponseRedirect(reverse('product_cart'))
    return render(request, 'cart/open_cart.html')
