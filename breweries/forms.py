from django import forms
from .models import Brewery, Food, Beer

class BreweryForm(forms.ModelForm):

    class Meta:
        model = Brewery
        fields = ('name', 'address', 'city', 'zipcode', 'phone', 'monday_hours', 'tuesday_hours', 'wednesday_hours', 'thursday_hours', 'friday_hours', 'saturday_hours', 'sunday_hours', 'logo_url')

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('item', 'description', 'options', 'price', 'brewery')

class BeerForm(forms.ModelForm):

    class Meta:
        model = Beer
        fields = ('name', 'style', 'abv', 'ibus', 'full_price', 'flight_price', 'glassware', 'description', 'image', 'brewery')
