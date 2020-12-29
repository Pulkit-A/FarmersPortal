from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=100)
    msp = models.FloatField()
    stock = models.IntegerField()
    location = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(null=True , max_length=500)
