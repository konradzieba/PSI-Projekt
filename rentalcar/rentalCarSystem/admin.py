from django.contrib import admin

from . import models

admin.site.register(models.Client)
admin.site.register(models.Address)
admin.site.register(models.Rent)
admin.site.register(models.Payment)
admin.site.register(models.Vehicle)
admin.site.register(models.VehicleSpecification)
admin.site.register(models.VehicleInformation)