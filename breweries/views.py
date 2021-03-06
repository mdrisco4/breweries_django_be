from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from rest_framework import permissions
from rest_framework import generics
from .models import Brewery, Food, Beer
from .serializers import BrewerySerializer
from .serializers import FoodSerializer
from .serializers import BeerSerializer
from .forms import BreweryForm
from .forms import FoodForm
from .forms import BeerForm

def brewery_list(request):
    breweries = Brewery.objects.all()
    return render(request, 'breweries/brewery_list.html', {'breweries': breweries})

def brewery_detail(request, pk):
    brewery = Brewery.objects.get(id=pk)
    return render(request, 'breweries/brewery_detail.html', {'brewery': brewery})

def brewery_create(request):
    if request.method == 'POST':
        form = BreweryForm(request.POST)
        if form.is_valid:
            brewery = form.save()
            return redirect('brewery_detail', pk=brewery.pk)
    else:
        form = BreweryForm()
        return render(request, 'breweries/brewery_form.html', {'form': form})

def brewery_edit(request, pk):
    brewery = Brewery.objects.get(pk=pk)
    if request.method == 'POST':
        form = BreweryForm(request.POST, instance = brewery)
        if form.is_valid:
            brewery = form.save()
            return redirect('brewery_detail', pk = brewery.pk)
    else:
        form = BreweryForm(instance = brewery)
        return render(request, 'breweries/brewery_form.html', {'form': form})

def brewery_delete(request, pk):
    Brewery.objects.get(id=pk).delete()
    return redirect('brewery_list')

class BreweryList(generics.ListCreateAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)

class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)

def food_list(request):
    breweries = Brewery.objects.all()
    return render(request, 'breweries/food_list.html', {'breweries': breweries})

def food_detail(request, pk):
    food = Food.objects.get(id=pk)
    return render(request, 'breweries/food_detail.html', {'food': food})

def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid:
            food = form.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm()
        return render(request, 'breweries/food_form.html', {'form': form})

def food_edit(request, pk):
    food = Food.objects.get(pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance = food)
        if form.is_valid:
            food = form.save()
            return redirect('food_detail', pk = food.pk)
    else:
        form = FoodForm(instance = food)
        return render(request, 'breweries/food_form.html', {'form': form})

def food_delete(request, pk):
    Food.objects.get(id=pk).delete()
    return redirect('food_list')

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)

def beer_list(request):
    breweries = Brewery.objects.all()
    return render(request, 'breweries/beer_list.html', {'breweries': breweries})


def beer_detail(request, pk):
    beer = Beer.objects.get(id=pk)
    return render(request, 'breweries/beer_detail.html', {'beer': beer})

def beer_create(request):
    if request.method == 'POST':
        form = BeerForm(request.POST)
        if form.is_valid:
            beer = form.save()
            return redirect('beer_detail', pk=beer.pk)
    else:
        form = BeerForm()
        return render(request, 'breweries/beer_form.html', {'form': form})

def beer_edit(request, pk):
    beer = Beer.objects.get(pk=pk)
    if request.method == 'POST':
        form = BeerForm(request.POST, instance = beer)
        if form.is_valid:
            beer = form.save()
            return redirect('beer_detail', pk = beer.pk)
    else:
        form = BeerForm(instance = beer)
        return render(request, 'breweries/beer_form.html', {'form': form})

def beer_delete(request, pk):
    Beer.objects.get(id=pk).delete()
    return redirect('beer_list')
    
class BeerList(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)

class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beer.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)