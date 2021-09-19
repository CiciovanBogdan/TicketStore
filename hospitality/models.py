from django.db import models


class Hospitality(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(null=False, help_text='price in euro')
    description = models.TextField(max_length=800, default='no description', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AvailableDate(models.Model):
    date = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date


class HospitalityReal(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=800, default='no description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
