from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
import datetime


class Address(models.Model):

    class Meta:
        verbose_name_plural = "Addresses"

    zip_code = models.CharField(max_length=6, blank=False, null=False, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    town = models.CharField(max_length=45, blank=False, null=False, validators=[MinLengthValidator(2), MaxLengthValidator(45)])
    country = models.CharField(max_length=45, blank=False, null=False, validators=[MinLengthValidator(2), MaxLengthValidator(45)])
    street = models.CharField(max_length=45, blank=False, null=False, validators=[MinLengthValidator(2), MaxLengthValidator(60)])
    apartment_number = models.CharField(max_length=7, blank=False, null=False, validators=[MinLengthValidator(1), MaxLengthValidator(7)])

    def __str__(self):
        return f'Address ID: {self.pk}, ' \
               f'{self.zip_code}' \
               f' {self.town}' \
               f' ({self.street}' \
               f' {self.apartment_number})' \
               f' {self.country}'


class Client(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)

    first_name = models.CharField(max_length=45, blank=False, null=False, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=45, blank=False, null=False, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default="2000-01-01", blank=False, null=False)
    pesel = models.CharField(max_length=11, blank=False, null=False, unique=True, validators=[MinLengthValidator(11), MinLengthValidator(11)])
    driver_licence_number = models.CharField(max_length=13, blank=False, null=False, validators=[MinLengthValidator(11), MinLengthValidator(11)], unique=True)
    phone_numer = models.CharField(max_length=15, blank=False, null=False, validators=[MinLengthValidator(9), MinLengthValidator(15)], unique=True)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    # email = models.CharField(max_length=15, blank=False, null=False, unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE, blank=False, null=False)
    # adress = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Client ID: {self.pk}, ' \
               f'{self.first_name[0]}.' \
               f' {self.last_name},' \
               f' {self.pesel}'


class Payment(models.Model):
    # cash = models.SmallIntegerField(blank=False, null=False)
    cash = models.BooleanField("Was payed by cash?", default=1, blank=True, null=True)
    card_number = models.CharField("Card number [if cash unchecked]", max_length=45, blank=True, null=True)
    def __str__(self):
        if self.cash == 1:
            return f'Payment ID: {str(self.pk)}, ' \
                   f'Payment: CASH'
        return f'Payment ID: {str(self.pk)}, ' \
               f'Payment: CREDIT CARD, ' \
               f'Card Number: {self.card_number}'


class Rent(models.Model):
    rent_start_date = models.DateField(blank=False, null=False)
    rent_end_date = models.DateField(blank=False, null=False)
    final_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_in_perc = models.SmallIntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(99), MinLengthValidator(1), MaxLengthValidator(2)])
    deposit = models.IntegerField(default=0, blank=True, null=True, validators=[MinLengthValidator(3), MaxLengthValidator(5)])
    km_limit = models.IntegerField(default=0, validators=[MaxLengthValidator(4)])

    def __str__(self):
        if self.discount_in_perc == 0:
            return f'Rent ID: {self.pk}, ' \
                   f'{self.rent_start_date} - ' \
                   f'{self.rent_start_date}, ' \
                   f'Km Limit: {self.km_limit}, ' \
                   f'Price: {self.final_price}'
        return f'Rent ID: {self.pk}, ' \
               f'{self.rent_start_date} - ' \
               f'{self.rent_start_date}, ' \
               f'Km Limit: {self.km_limit}, ' \
               f'Price: {self.final_price}PLN , ' \
               f'Discount: {self.discount_in_perc}%'

class VehicleSpecification(models.Model):
    class Meta:
        verbose_name_plural  = "Vehicle Specifications"
    DIESEL = 'DIESEL'
    PETROL = 'PETROL'
    ELECTRIC = 'ELECTRIC'
    HYBRID = 'HYBRID'
    TYPEOFFUEL_CHOICES = ((DIESEL, 'Diesel'), (PETROL, 'Petrol'), (ELECTRIC, 'Electric'), (HYBRID, 'Hybrid'),)

    MANUAL = 'MANUAL'
    AUTO = 'AUTO'
    GEARBOX_CHOICES = ((AUTO, 'Auto'), (MANUAL, 'Manual'))

    FWD = 'FWD'
    RWD = 'RWD'
    AWD = 'AWD'
    TYPEOFDRIVE_CHOICES = ((FWD, 'FWD'), (RWD, 'RWD'), (AWD, 'AWD'),)

    color = models.CharField(max_length=45, blank=False, null=False, validators=[MinLengthValidator(2)])
    gear_box = models.CharField(max_length=7, choices=GEARBOX_CHOICES, blank=False, null=False, default=AUTO)
    type_of_drive = models.CharField(max_length=4, choices=TYPEOFDRIVE_CHOICES, blank=False, null=False, default=FWD)
    type_of_fuel = models.CharField(max_length=11, choices=TYPEOFFUEL_CHOICES, blank=False, null=False, default=DIESEL)
    avg_fuel_consumption = models.FloatField("Average fuel consumption per 100km [L]", max_length=4, default=10.0, blank=False, null=False)
    num_of_doors = models.SmallIntegerField("Number of doors", default=4, blank=False, null=False, validators=[MinValueValidator(2), MaxValueValidator(5)])
    num_of_seats = models.SmallIntegerField("Number of seats", default=5, blank=False, null=False, validators=[MinValueValidator(2), MaxValueValidator(9)])
    boot_capacity = models.IntegerField("Boot Capacity", blank=False, null=False, validators=[MinValueValidator(100), MaxValueValidator(2000)])

    def __str__(self):
        return f'VehSpec ID: {self.pk}, ' \
               f'Color: {self.color}, ' \
               f'{self.num_of_doors} doors ' \
               f'{self.type_of_drive} ' \
               f'{self.type_of_fuel}'


class VehicleInformation(models.Model):
    class Meta:
        verbose_name_plural = "Vehicle Informations"
    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.date.today().year + 1)]

    year_of_production = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    license_plate_number = models.CharField(max_length=9, blank=False, null=False, validators=[MinLengthValidator(6)]) #Individual plate numbers validated (shorter ones)
    vin_number = models.CharField(max_length=17, blank=False, null=False, validators=[MinLengthValidator(17)]) #VIN number got 17 chars
    date_of_the_review = models.DateField(blank=False, null=False) #Last date of formal review imposed by law
    condition_comment = models.CharField(max_length=250, blank=True, null=True) #Not neccessery, comment about car condition
    mileage = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(300000)]) #Mileage < 200 000 km imposed by company
    last_service = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(5000), MaxValueValidator(300000)]) #Mileage during last service inside of company [IN KM]

    def __str__(self):
        km_to_service = (int(self.last_service + 15000)) - int(self.mileage)
        if self.condition_comment is not None:
            return f'VehSpec ID: {self.pk}, ' \
                   f'Plate: {self.license_plate_number}, ' \
                   f'Production: {self.year_of_production}, ' \
                   f'Mileage: {self.mileage}, ' \
                   f'To Service: {km_to_service} ' \
                   f'*CONTAIN COMMENT*'

        return f'VehSpec ID: {self.pk}, ' \
               f'Plate: {self.license_plate_number}, ' \
               f'Production: {self.year_of_production}, ' \
               f'Mileage: {self.mileage}, ' \
               f'Till Service: {km_to_service}'


class Vehicle(models.Model):
    SUV = 'SUV'
    MINIBUS = 'MINIBUS'
    LIMUZYNA = 'LIMUZYNA'
    COUPE = 'COUPE'
    KOMBI = 'KOMBI'
    CARTYPE_CHOICES = ((SUV, 'Suv'), (MINIBUS, 'Minibus'), (LIMUZYNA, 'Limuzyna'), (COUPE, 'Coupe'), (KOMBI, 'Kombi'),)

    car_type = models.CharField(max_length=10, choices=CARTYPE_CHOICES, blank=False, null=False, default=KOMBI)
    status = models.BooleanField("Is vehicle available?", default=1, blank=True, null=False)
    mark = models.CharField(max_length=45, blank=False, null=False)
    model = models.CharField(max_length=45, blank=False, null=False)
    price_per_day = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(100), MaxValueValidator(7500)])

    def __str__(self):
        if self.status == 0:
            return f'Vehicle ID: {self.pk}, ' \
                   f'{self.mark} ' \
                   f'{self.model} [UNAVAILABLE]'
        return f'Vehicle ID: {self.pk}, ' \
               f'{self.mark} ' \
               f'{self.model} [AVAILABLE]'


