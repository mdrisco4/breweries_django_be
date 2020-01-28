from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from rest_framework import permissions

from .models import Brewery, Food, Beer
from rest_framework import generics
from .serializers import BrewerySerializer
# from .serializers import FoodSerializer
# from .serializers import BeerSerializer

class BreweryList(generics.ListCreateAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)

class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    permission_classes = (permissions.IsAuthenticated,)

def brewery_list(request):
    breweries = Brewery.objects.all()
    return render(request, 'breweries/brewery_list.html', {'breweries': breweries})

def brewery_detail(request, pk):
    brewery = Brewery.objects.get(id=pk)
    return render(request, 'breweries/brewery_detail.html', {'brewery': brewery})

def brewery_create(response):
    if request.method == 'POST':
        form = BreweryForm(request.POST)
        if form.is_valid:
            brewery = form.save()
            return redirect('brewery_detail', pk=house.pk)
    else:
        form = BreweryForm()
        return render(request, 'breweries/brewery_form.html', {'form': form})

def brewery_edit(request, pk):
    brewery = Brewery.objects.get(pk=pk)
    if request.method == 'POST':
        form = BreweryForm(request.POST, instance = house)
        if form.is_valid:
            brewery = form.save()
            return redirect('brewery_detail', pk = brewery.pk)
    else:
        form = BreweryForm(instance = brewery)
        return render(request, 'breweries/brewery_form.html', {'form': form})

def brewery_delete(request, pk):
    Brewery.objects.get(id=pk).delete()
    return redirect('brewery_list')

# class BreweryList(generics.ListCreateAPIView):
#     queryset = Brewery.objects.all()
#     serializer_class = BrewerySerializer

# class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Brewery.objects.all()
#     serializer_class = BrewerySerializer

def food_list(request):
    food = Food.objects.all()
    return render(request, 'breweries/food_list.html', {'food': food})

def food_detail(request, pk):
    food = Food.objects.get(id=pk)
    return render(request, 'breweries/food_detail.html', {'food': food})

def food_create(response):
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
        form = FoodForm(instance = house)
        return render(request, 'breweries/food_form.html', {'form': form})

def food_delete(request, pk):
    Food.objects.get(id=pk).delete()
    return redirect('food_list')

# class FoodList(generics.ListCreateAPIView):
#     queryset = Food.objects.all()
#     serializer_class = BrewerySerializer

# class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Food.objects.all()
#     serializer_class = BrewerySerializer

def beer_list(request):
    beers = Beer.objects.all()
    return render(request, 'breweries/beer_list.html', {'beers': beers})

def beer_detail(request, pk):
    beer = Beer.objects.get(id=pk)
    return render(request, 'breweries/beer_detail.html', {'beer': beer})

def beer_create(response):
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
        form = BeerForm(request.POST, instance = house)
        if form.is_valid:
            beer = form.save()
            return redirect('beer_detail', pk = beer.pk)
    else:
        form = BeerForm(instance = house)
        return render(request, 'breweries/beer_form.html', {'form': form})

def beer_delete(request, pk):
    Beer.objects.get(id=pk).delete()
    return redirect('house_list')
    
# class BeerList(generics.ListCreateAPIView):
#     queryset = Beer.objects.all()
#     serializer_class = BrewerySerializer

# class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Beer.objects.all()
#     serializer_class = BrewerySerializer