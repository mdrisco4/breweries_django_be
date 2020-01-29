from django.db import models
from django.contrib.postgres.fields import ArrayField

class Brewery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    monday_hours = models.CharField(max_length=20)
    tuesday_hours = models.CharField(max_length=20)
    wednesday_hours = models.CharField(max_length=20)
    thursday_hours = models.CharField(max_length=20)
    friday_hours = models.CharField(max_length=20)
    saturday_hours = models.CharField(max_length=20)
    sunday_hours = models.CharField(max_length=20)
    logo_url = models.TextField()
    # services_offered = models.TextField()
    # drink = models.ManyToManyField(Beer)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Food(models.Model):
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    options = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    # brewery = models.Charfield(max_length=50)
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT, related_name = 'food')

    def __str__(self):
        return self.item

class Beer(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.CharField(max_length=10)
    ibus = models.CharField(max_length=10)
    full_price = models.CharField(max_length=10)
    flight_price = models.CharField(max_length=10)
    glassware = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    image = models.TextField(max_length=255)
    # brewery = models.CharField(max_length=50)
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT, related_name = 'beers')

    def __str__(self):
        return self.name
