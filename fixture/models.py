from django.db import models


class FixtureMancity(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.title


class FixtureRealMadrid(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.title
