from django.db import models

from hospitality.models import AvailableDate


class Booking(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    nr_of_persons = models.IntegerField(null=False)
    other_details = models.TextField(max_length=800, default='no detail')
    date = models.ForeignKey(AvailableDate, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
