from django.db import models

# Create your models here.
class Vehicles(models.Model):
    vin = models.CharField(max_length=20)
    pwd = models.CharField(max_length=50)
    url = models.CharField(max_length=100)


