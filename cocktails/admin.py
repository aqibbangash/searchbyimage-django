from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Inventory
from .models import Cocktails

admin.site.register(Inventory)
admin.site.register(Cocktails)
