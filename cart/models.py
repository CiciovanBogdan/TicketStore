from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from merch.models import Merch


# model pentru cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    status = models.CharField(default='open', max_length=200)

    def __str__(self):
        return f"{self.status} cart of {self.user}"


# model pentru produsele din cart
class CartItem(models.Model):
    product = models.ForeignKey(Merch, on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=CASCADE)

    def __str__(self):
        return f"{self.quantity}X{self.product.name}"
