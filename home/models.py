from django.db import models


class CropOrder(models.Model):
    name = models.CharField(max_length=100)
    productID = models.IntegerField()
    buyerID = models.IntegerField(default=0)
    cost = models.FloatField()
    qty = models.IntegerField()
    location = models.CharField(max_length=200)
