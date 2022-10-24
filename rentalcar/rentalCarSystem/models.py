from django.db import models
import datetime


def year_choices():
    return [(r, r) for r in range(2000, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class Client(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)

    first_name = models.CharField(max_length=45, blank=False, null=False)
    last_name = models.CharField(max_length=45, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=False)
    pesel = models.CharField(max_length=11, blank=False, null=False, unique=True)
    driver_licence_number = models.CharField(max_length=13, blank=False, null=False, unique=True)
    phone_numer = models.CharField(max_length=15, blank=False, null=False, unique=True)
    email = models.CharField(max_length=15, blank=False, null=False, unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE, blank=False, null=False)


class Address(models.Model):
    zip_code = models.CharField(max_length=6, blank=False, null=False)
    town = models.CharField(max_length=45, blank=False, null=False)
    country = models.CharField(max_length=45, blank=False, null=False)
    street = models.CharField(max_length=45, blank=False, null=False)
    apartment_number = models.CharField(max_length=45, blank=False, null=False)


class Rent(models.Model):
    rent_start_date = models.DateField(blank=False, null=False)
    rent_end_date = models.DateField(blank=False, null=False)
    final_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_in_perc = models.SmallIntegerField(blank=True, null=True)
    deposit = models.IntegerField(blank=True, null=True)
    km_limit = models.IntegerField(default=0)


class Payment(models.Model):
    cash = models.SmallIntegerField(blank=False, null=False)
    card_number = models.CharField(max_length=45, blank=True, null=True)


class Vehicle(models.Model):
    SUV = 'SUV'
    MINIBUS = 'MINIBUS'
    LIMUZYNA = 'LIMUZYNA'
    COUPE = 'COUPE'
    KOMBI = 'KOMBI'
    CARTYPE_CHOICES = ((SUV, 'Suv'), (MINIBUS, 'Minibus'), (LIMUZYNA, 'Limuzyna'), (COUPE, 'Coupe'), (KOMBI, 'Kombi'),)

    car_type = models.CharField(max_length=10, choices=CARTYPE_CHOICES, blank=False, null=False, default=KOMBI)
    status = models.SmallIntegerField(blank=False, null=False)
    model = models.CharField(max_length=45, blank=False, null=False)
    mark = models.CharField(max_length=45, blank=False, null=False)
    price_per_day = models.IntegerField(blank=False, null=False)


class VehicleSpecification(models.Model):
    DIESEL = 'DIESEL'
    BENZYNA = 'BENZYNA'
    ELEKTRYCZNY = 'ELEKTRYCZNY'
    HYBRYDA = 'HYBRYDA'
    TYPEOFFUEL_CHOICES = ((DIESEL, 'Diesel'), (BENZYNA, 'Benzyna'), (ELEKTRYCZNY, 'Elektryczny'), (HYBRYDA, 'Hybryda'),)

    MANUAL = 'MANUAL'
    AUTO = 'AUTO'
    GEARBOX_CHOICES = ((MANUAL, 'Manual'), (AUTO, 'Auto'),)

    FWD = 'FWD'
    RWD = 'RWD'
    AWD = 'AWD'
    TYPEOFDRIVE_CHOICES = ((FWD, 'FWD'), (RWD, 'RWD'), (AWD, 'AWD'),)

    color = models.CharField(max_length=45, blank=False, null=False)
    type_of_fuel = models.CharField(max_length=11, choices=TYPEOFFUEL_CHOICES, blank=False, null=False, default=DIESEL)
    gear_box = models.CharField(max_length=7, choices=GEARBOX_CHOICES, blank=False, null=False, default=MANUAL)
    avg_fuel_consumption = models.FloatField(max_length=4, blank=False, null=False)
    boot_capacity = models.IntegerField(blank=False, null=False)
    num_of_doors = models.SmallIntegerField(blank=False, null=False)
    num_of_seats = models.SmallIntegerField(blank=False, null=False)
    type_of_drive = models.CharField(max_length=4, choices=TYPEOFDRIVE_CHOICES, blank=False, null=False, default=FWD)


# class VehicleInformation(models.Model):
    # year_of_production = models.IntegerField(_('year'), )