from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator, \
    ValidationError
import datetime

# from django.db.models import F
# from django.db.models.signals import pre_delete
# from django.dispatch import receiver
# from Tools.demo.mcast import sender

def present_date_validator(value):
    if value < datetime.date.today():
        raise ValidationError('Rent start date cannot be in past')


class Address(models.Model):
    class Meta:
        verbose_name_plural = "Addresses"

    zip_code = models.CharField(max_length=6, blank=False, null=False,
                                validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    town = models.CharField(max_length=45, blank=False, null=False,
                            validators=[MinLengthValidator(2), MaxLengthValidator(45)])
    country = models.CharField(max_length=45, blank=False, null=False,
                               validators=[MinLengthValidator(2), MaxLengthValidator(45)])
    street = models.CharField(max_length=45, blank=False, null=False,
                              validators=[MinLengthValidator(2), MaxLengthValidator(60)])
    apartment_number = models.CharField(max_length=7, blank=False, null=False,
                                        validators=[MinLengthValidator(1), MaxLengthValidator(7)])
    full_name = models.CharField(max_length=500, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.full_name = self.zip_code + " " + self.town + " " + self.country + ", " + self.street + " " + self.apartment_number
        super(Address, self).save(*args, **kwargs)

    def __str__(self):
        return f'Address ID: {self.pk}, ' \
               f' {self.zip_code}' \
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
    pesel = models.CharField(max_length=11, blank=False, null=False, unique=True,
                             validators=[MinLengthValidator(11), MinLengthValidator(11)])
    driver_licence_number = models.CharField(max_length=13, blank=False, null=False,
                                             validators=[MinLengthValidator(11), MinLengthValidator(11)], unique=True)
    phone_number = models.CharField(max_length=15, blank=False, null=False,
                                    validators=[MinLengthValidator(9), MinLengthValidator(15)], unique=True)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE, blank=False, null=False)
    address = models.OneToOneField(Address, related_name='addresses', blank=True, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + " " + self.last_name
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return f'Client ID: {self.pk}, ' \
               f'{self.first_name[0]}.' \
               f' {self.last_name},' \
               f' {self.pesel}'


class Payment(models.Model):
    cash = models.BooleanField("Was payed by cash?", default=1, blank=True, null=True)
    card_number = models.CharField("Card number [if cash unchecked]", max_length=45, blank=True, null=True)
    full_name = models.CharField(max_length=500, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.cash == 1:
            self.full_name = 'CASH'
            super(Payment, self).save(*args, **kwargs)
        else:
            self.full_name = 'CREDIT CARD' + ": " + self.card_number
            super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        if self.cash == 1:
            return f'Payment ID: {str(self.pk)}, ' \
                   f'Payment: CASH'
        return f'Payment ID: {str(self.pk)}, ' \
               f'Payment: CREDIT CARD, ' \
               f'Card Number: {self.card_number}'


class VehicleSpecification(models.Model):
    class Meta:
        verbose_name_plural = "Vehicle Specifications"

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
    avg_fuel_consumption = models.FloatField("Average fuel consumption per 100km [L]", max_length=4, default=10.0,
                                             blank=False, null=False)
    num_of_doors = models.SmallIntegerField("Number of doors", default=4, blank=False, null=False,
                                            validators=[MinValueValidator(2), MaxValueValidator(5)])
    num_of_seats = models.SmallIntegerField("Number of seats", default=5, blank=False, null=False,
                                            validators=[MinValueValidator(2), MaxValueValidator(9)])
    boot_capacity = models.IntegerField("Boot Capacity", blank=False, null=False,
                                        validators=[MinValueValidator(100), MaxValueValidator(2000)])
    full_name = models.CharField(max_length=500, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.full_name = f'{self.color}, {self.gear_box}, {self.type_of_drive}, {self.type_of_fuel}, {self.avg_fuel_consumption} per 100km, {self.num_of_doors} doors, {self.boot_capacity} kg, {self.num_of_seats} seats'
        super(VehicleSpecification, self).save(*args, **kwargs)

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
    license_plate_number = models.CharField(max_length=9, blank=False, null=False, validators=[
        MinLengthValidator(6)])  # Individual plate numbers validated (shorter ones)
    vin_number = models.CharField(max_length=17, blank=False, null=False,
                                  validators=[MinLengthValidator(17)])  # VIN number got 17 chars
    date_of_the_review = models.DateField(blank=False, null=False)  # Last date of formal review imposed by law
    condition_comment = models.CharField(max_length=250, blank=True,
                                         null=True)  # Not neccessery, comment about car condition
    mileage = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(
        300000)])  # Mileage < 200 000 km imposed by company
    last_service = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(5000), MaxValueValidator(
        300000)])  # Mileage during last service inside of company [IN KM]
    full_name = models.CharField(max_length=500, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.full_name = f'{self.year_of_production}, {self.license_plate_number}, {self.vin_number}'
        super(VehicleInformation, self).save(*args, **kwargs)

    def __str__(self):
        # km_to_service = (int(self.last_service + 15000)) - int(self.mileage)
        if self.condition_comment is not None:
            return f'VehInfo ID: {self.pk}, ' \
                   f'Plate: {self.license_plate_number}, ' \
                   f'Production: {self.year_of_production}, ' \
                   f'Mileage: {self.mileage}, ' \
                   f'*CONTAIN COMMENT*'

        return f'VehSpec ID: {self.pk}, ' \
               f'Plate: {self.license_plate_number}, ' \
               f'Production: {self.year_of_production}, ' \
               f'Mileage: {self.mileage}, '


class Vehicle(models.Model):
    SUV = 'SUV'
    MINIBUS = 'MINIBUS'
    LIMOUSINE = 'LIMOUSINE'
    COUPE = 'COUPE'
    KOMBI = 'KOMBI'
    CITY_CAR = 'CITY CARS'

    CARTYPE_CHOICES = ((SUV, 'Suv'), (MINIBUS, 'Minibus'), (LIMOUSINE, 'Limousine'), (COUPE, 'Coupe'), (KOMBI, 'Kombi'),
                       (CITY_CAR, 'City Cars'))

    car_type = models.CharField(max_length=15, choices=CARTYPE_CHOICES, blank=False, null=False, default=CITY_CAR)
    status = models.BooleanField("Is vehicle available?", default=1, blank=True, null=False, editable=False)
    mark = models.CharField(max_length=45, blank=False, null=False)
    model = models.CharField(max_length=45, blank=False, null=False)
    price_per_day = models.IntegerField(blank=False, null=False,
                                        validators=[MinValueValidator(100), MaxValueValidator(7500)])
    vehicle_specification = models.OneToOneField(VehicleSpecification, related_name='specifications', blank=True,
                                                 null=True, on_delete=models.CASCADE)
    vehicle_information = models.OneToOneField(VehicleInformation, related_name='informations', blank=True, null=True,
                                               on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.full_name = f'{self.car_type}, {self.mark}, {self.model}, {self.price_per_day} per day'
        super(Vehicle, self).save(*args, **kwargs)

    def __str__(self):
        if self.status == 0:
            return f'Vehicle ID: {self.pk}, ' \
                   f'{self.mark} ' \
                   f'{self.model} [UNAVAILABLE]'
        return f'Vehicle ID: {self.pk}, ' \
               f'{self.mark} ' \
               f'{self.model} [AVAILABLE]'


class Rent(models.Model):
    rent_start_date = models.DateField(blank=False, null=False, validators=[present_date_validator])
    rent_end_date = models.DateField(blank=False, null=False)
    final_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, editable=False)
    discount_in_perc = models.SmallIntegerField(default=0, blank=True, null=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(99)])
    deposit = models.IntegerField(null=True, blank=True, editable=False)
    km_limit = models.IntegerField(default=0, validators=[MaxValueValidator(999)])
    number_of_days = models.CharField(max_length=99, blank=True, null=True, editable=False)
    price_per_day = models.IntegerField(blank=True, null=True, editable=False)
    payment = models.OneToOneField(Payment, related_name='payments', blank=True, null=True, on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicle, related_name='vehicles', blank=True, null=True, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='clients', blank=True, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        days = (self.rent_end_date - self.rent_start_date).days
        vehicle_id = self.vehicle.pk
        vehicle = Vehicle.objects.get(id=vehicle_id)
        price = vehicle.price_per_day
        self.number_of_days = days
        self.price_per_day = price
        self.final_price = (int(price) * int(days)) - ((int(price) * (days)) * self.discount_in_perc / 100)
        self.deposit = int(self.final_price * 0.2)
        Vehicle.objects.filter(pk=vehicle_id).update(status=0)
        super(Rent, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        vehicle_id = self.vehicle.pk
        print(vehicle_id)
        Vehicle.objects.filter(pk=vehicle_id).update(status=1)
        super(Rent, self).delete(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     Vehicle.objects.all().update(status=F(1))
    #     return super(Rent, self).delete(*args, **kwargs)

    def clean(self):
        if self.rent_end_date < self.rent_start_date:
            raise ValidationError({'rent_end_date': 'Rent end date can not be before rent start date'})

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


# @receiver(pre_delete, sender=Rent)
# def change_status(sender, instance, **kwargs):
#     print(Rent.vehicle.name)
#     # Vehicle.objects.filter(id=sender.objects.get(id=instance.id)).update(status=0)






