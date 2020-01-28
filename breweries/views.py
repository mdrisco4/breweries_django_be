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
    beers = Beer.objects.get(id=pk)
    return render(request, 'breweries/beer_detail.html', {'beer': beer})
    
# class BeerList(generics.ListCreateAPIView):
#     queryset = Beer.objects.all()
#     serializer_class = BrewerySerializer

# class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Beer.objects.all()
#     serializer_class = BrewerySerializer