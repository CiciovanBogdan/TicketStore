from django.db import models


class HospitalityPayed(models.Model):
    name_city = models.CharField(max_length=150, null=True, blank=True)
    price_city = models.IntegerField(help_text='price in euro', null=True, blank=True)
    description_city = models.TextField(max_length=800, default='no description', null=True, blank=True)
    name_barcelona = models.CharField(max_length=150, null=True, blank=True)
    price_barcelona = models.IntegerField(help_text='price in euro', null=True, blank=True)
    description_barcelona = models.TextField(max_length=800, default='no description', null=True, blank=True)

    def __str__(self):
        return self.name_city


class HospitalityVIP(models.Model):
    name_real = models.CharField(max_length=150, null=True, blank=True)
    description_real = models.TextField(max_length=800, default='no description', null=True, blank=True)
    name_united = models.CharField(max_length=150, null=True, blank=True)
    description_united = models.TextField(max_length=800, default='no description', null=True, blank=True)

    def __str__(self):
        return self.name_real


class AvailableDate(models.Model):
    date = models.CharField(max_length=150)

    def __str__(self):
        return self.date
