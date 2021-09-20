from django.db import models


class Merch(models.Model):
    size_ch = (('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'))
    name = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.IntegerField(null=False)
    size = models.CharField(max_length=30, default='M', choices=size_ch)
    description = models.TextField(max_length=1000, default='no description')
    for_vip = models.BooleanField(default=0)
    for_city = models.BooleanField(default=0)
    for_real = models.BooleanField(default=0)
    for_united = models.BooleanField(default=0)
    for_barcelona = models.BooleanField(default=0)

    def __str__(self):
        return self.name
