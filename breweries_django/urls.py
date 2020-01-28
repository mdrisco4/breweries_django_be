"""breweries_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from breweries import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('breweries.urls')),
    path('', include('accounts.urls')),
    path('', views.brewery_list),
    path('breweries/', views.brewery_list, name='brewery_list'),
    path('breweries/<int:pk>', views.brewery_detail, name='brewery_detail'),
    path('food/', views.food_list, name='food_list'),
    path('food/<int:pk>', views.food_detail, name='food_detail'),
    path('beers/', views.beer_list, name='beer_list'),
    path('beers/<int:pk>', views.beer_detail, name='beer_detail'),
   ]
