from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/images')

class Crop(models.Model):
    name = models.CharField(max_length=100)
    msp = models.FloatField()
    stock = models.IntegerField()
    location = models.CharField(max_length=255)
    image = models.ImageField(storage=fs)
