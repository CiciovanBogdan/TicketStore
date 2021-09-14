from django.db import models


class VIP(models.Model):
    vip_type_ch = (('Monthly', 'Monthly'), ('Yearly', 'Yearly'))
    title = models.CharField(max_length=150)
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=1000, default='no description')
    vip_type = models.CharField(choices=vip_type_ch, max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
