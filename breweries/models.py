from django.db import models

class Brewery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    hours = models.CharField(max_length=20)
    logo_url = models.TextField()

    def __str__(self):
        return self.name

class Food(models.Model):
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)

    def __str__(self):
        return self.item

class Beer(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.CharField(max_length=10)
    full_price = models.CharField(max_length=10)
    flight_price = models.CharField(max_length=10)
    glassware = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
