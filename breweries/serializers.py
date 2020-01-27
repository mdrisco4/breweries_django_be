from rest_framework import serializers
from .models import Brewery, Food, Beer

# class BrewerySerializer(serializers.HyperlinkedModelSerializer):
#     food = serializers.HyperlinkedRelatedField(
#         view_name='food_detail',
#         many=True,
#         read_only=True
#     )
#     beer = serializers.HyperlinkedRelatedField(
#         view_name='beer_detail',
#         many=True,
#         read_only=True
#     )
#     class Meta:
#         model = Brewery
#         fields = ('id', 'name', 'address', 'phone', 'hours', 'logo_url', 'food', 'beer', )

class BrewerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Brewery
        fields = ['id', 'name', 'address', 'phone', 'hours', 'logo_url', ]

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'item', 'description', 'price', ]

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ['id', 'name', 'style', 'abv', 'full_price', 'flight_price', 'glassware', 'description', ]