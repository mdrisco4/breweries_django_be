from django.contrib import admin
from .models import Brewery
from .models import Food
from .models import Beer

admin.site.register(Brewery)
admin.site.register(Food)
admin.site.register(Beer)
