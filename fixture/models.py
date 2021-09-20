from django.db import models


class Fixture(models.Model):
    title_man_city = models.CharField(max_length=150, null=True, blank=True)
    match_info_man_city = models.CharField(max_length=150, null=True, blank=True)
    title_real_madrid = models.CharField(max_length=150, null=True, blank=True)
    match_info_real_madrid = models.CharField(max_length=150, null=True, blank=True)
    title_man_united = models.CharField(max_length=150, null=True, blank=True)
    match_info_man_united = models.CharField(max_length=150, null=True, blank=True)
    title_barcelona = models.CharField(max_length=150, null=True, blank=True)
    match_info_barcelona = models.CharField(max_length=150, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title_real_madrid
