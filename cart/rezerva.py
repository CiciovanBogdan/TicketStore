# @login_required
# def open_cart_view(request):
#     open_cart = get_open_cart(request)
#     cart_items = CartItem.objects.filter(cart=open_cart)
#
#     def discount_price():
#         total_unit_price = list(
#             map(lambda cart_item: {'t_price': cart_item.product.price * cart_item.quantity}, cart_items))
#         final_total = reduce(lambda first, second: first + second['t_price'], total_unit_price, 0)
#         return {'total_unit_price': total_unit_price, 'final_total': final_total}
#
#     return render(request, 'cart/open_cart.html',
#                   {'open_cart': open_cart, 'cart_items': cart_items, 'the_price': discount_price()})

# @login_required
# def open_cart_view(request):
#     open_cart = get_open_cart(request)
#     cart_items = CartItem.objects.filter(cart=open_cart)
#     total_unit_price = list(
#         map(lambda cart_item: {'t_price': cart_item.product.price * cart_item.quantity}, cart_items))
#     final_total = reduce(lambda first, second: first + second['t_price'], total_unit_price, 0)
#     print(total_unit_price)
#     print(final_total)
#     return render(request, 'cart/open_cart.html',
#                   {'open_cart': open_cart, 'cart_items': cart_items, 'total_unit_price': total_unit_price,
#                    'final_total': final_total})