from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import Group, User


class ExtendUser(User):
    age = models.IntegerField(null=False)
    balance = models.IntegerField(null=False, default=0)

    def __str__(self):
        return str(self.balance)


g = Group.objects.get(name='Client')
users = User.objects.all()
for u in users:
    g.user_set.add(u)
