from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=45, blank=False, null=False)
    last_name = models.CharField(max_length=45, blank=False, null=False)
    birth_date = models.DateField(default="2000-01-01", blank=False, null=False)
    pesel = models.CharField(max_length=11, blank=False, null=False)
    driver_licence_number = models.CharField(max_length=13, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    gender = models.CharField(max_length=6, blank=False, null=False)


class Vehicle(models.Model):
    car_type = models.CharField(max_length=15, blank=False, null=False)
    status = models.BooleanField("Is vehicle available?", default=1, blank=True, null=False, editable=False)
    mark = models.CharField(max_length=45, blank=False, null=False)
    model = models.CharField(max_length=45, blank=False, null=False)
    price_per_day = models.IntegerField(blank=False, null=False)


class Rent(models.Model):
    rent_start_date = models.DateField(blank=False, null=False)
    rent_end_date = models.DateField(blank=False, null=False)
    final_price = models.IntegerField(blank=False, null=False)
    km_limit = models.IntegerField(blank=False, null=False)
    vehicle = models.ForeignKey(Vehicle, blank=True, null=True, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)