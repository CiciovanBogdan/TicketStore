from django.db import models


class Merch(models.Model):
    size_ch = (('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'))
    name = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.IntegerField(null=False)
    discount_price = models.IntegerField(null=True)
    size = models.CharField(max_length=30, default='M', choices=size_ch)
    description = models.TextField(max_length=1000, default='no description')
    for_vip = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MerchReal(models.Model):
    size_ch = (('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL'))
    name = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to='real/')
    price = models.IntegerField(null=False)
    discount_price = models.IntegerField(null=True)
    size = models.CharField(max_length=30, default='M', choices=size_ch)
    description = models.TextField(max_length=1000, default='no description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MerchManUnited(models.Model):
    size_ch = (('S', 'S'), ('M', 'M'), ('L', 'L'), ('Xl', 'XL'), ('XXL', 'XXL'))
    name = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to='real/')
    price = models.IntegerField(null=False)
    discount_price = models.IntegerField(null=True)
    size = models.CharField(max_length=30, default='M', choices=size_ch)
    description = models.TextField(max_length=1000, default='no description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MerchBarcelona(models.Model):
    size_ch = (('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl'))
    name = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to='real/')
    price = models.IntegerField(null=False)
    discount_price = models.IntegerField(null=True)
    size = models.CharField(max_length=30, default='M', choices=size_ch)
    description = models.TextField(max_length=1000, default='no description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
