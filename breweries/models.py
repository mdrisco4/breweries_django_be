from django.db import models

class Brewery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    hours = models.CharField(max_length=20)
    logo_url = models.TextField()

class Food(models.Model):
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)

class Beer(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    full_price = models.CharField(max_length=10)
    flight_price = models.CharField(max_length=10)
    glassware = models.CharField(max_length=20)
    abv = models.TextField(max_length=10)
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)
