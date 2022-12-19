from django.contrib import admin
from .models import Client, Vehicle, Rent

admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(Rent)