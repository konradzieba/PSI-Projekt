from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Address, Client, Payment, Rent, VehicleInformation, VehicleSpecification, Vehicle
from .serializers import AddressSerializer, ClientSerializer, PaymentSerializer, RentSerializer, \
    VehicleInformationSerializer, VehicleSpecificationSerializer, VehicleSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet, DateFilter, ModelChoiceFilter, ChoiceFilter, BooleanFilter, MultipleChoiceFilter
from django import forms
import datetime
from django.db.models import Q



class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-list'

    filter_fields = ['zip_code', 'town', 'country', 'street']
    search_fields = ['$zip_code', '$town', 'country', '$street']
    ordering_fields = ['town', 'country', 'street']


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'


GENDER_CHOICES = (('MALE', 'Male'), ('FEMALE', 'Female'))
class ClientFilter(FilterSet):
    min_birth_date = DateFilter(field_name='birth_date', lookup_expr='gte', label='Birth date from:', widget=forms.DateInput(attrs={'type': 'date'}))
    max_birth_date = DateFilter(field_name='birth_date', lookup_expr='lte', label='Birth date to:', widget=forms.DateInput(attrs={'type': 'date'}))
    gender = ChoiceFilter(choices=GENDER_CHOICES, label='Gender', empty_label='Any')


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    filterset_class = ClientFilter

    filter_fields = ['first_name', 'last_name', 'pesel', 'driver_licence_number', 'phone_number', 'email', 'birth_date', 'gender']
    search_fields = ['first_name', '$last_name', '$pesel', '$driver_licence_number', '$phone_number', '$email']
    ordering_fields = ['first_name', 'last_name', 'birth_date']


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


CASH_CHOICES = (('1', 'Yes'), ('0', 'No'))
class PaymentFilter(FilterSet):
    cash = ChoiceFilter(choices=CASH_CHOICES, empty_label='Any')


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    name = 'payment-list'
    #dodac swoj czy gotowka czy karta
    filter_fields = ['card_number']
    search_fields = ['$card_number']
    ordering_fields = ['card_number']
    filterset_class = PaymentFilter


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    name = 'payment-detail'


class RentFilter(FilterSet):
    min_final_price = NumberFilter(field_name='final_price', lookup_expr='gte', label='Final price from:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 1000'}))
    max_final_price = NumberFilter(field_name='final_price', lookup_expr='lte', label='Final price to:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 5500'}))
    min_rent_start_date = DateFilter(field_name='rent_start_date', lookup_expr='gte', label='Rent start date from:', widget=forms.DateInput(attrs={'type': 'date'}))
    max_rent_start_date = DateFilter(field_name='rent_start_date', lookup_expr='lte', label='Rent end date to:', widget=forms.DateInput(attrs={'type': 'date'}))
    min_rent_end_date = DateFilter(field_name='rent_end_date', lookup_expr='gte', label='Rent end date from:', widget=forms.DateInput(attrs={'type': 'date'}))
    max_rent_start_date = DateFilter(field_name='rent_end_date', lookup_expr='lte', label='Rent end date to:', widget=forms.DateInput(attrs={'type': 'date'}))
    min_deposit = NumberFilter(field_name='deposit', lookup_expr='gte', label='Deposit price from:', widget=forms.NumberInput(attrs={'placeholder' : 'Example: 100', 'step': '10'}))
    max_deposit = NumberFilter(field_name='deposit', lookup_expr='lte', label='Deposit price to:', widget=forms.NumberInput(attrs={'placeholder' : 'Example: 500', 'step': '10'}))    


class RentList(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    name = 'rent-list'
    filterset_class = RentFilter
    #dodac filtr po datach konca i poczatku, zawieraja znizke,
    #kiedy zamienimy id - dodac wyszukiwanie po samochodzie i imieniu
    filter_fields = ['rent_start_date', 'rent_end_date', 'final_price', 'deposit']
    search_fields = ['$rent_start_date', '$rent_end_date', 'final_price', 'deposit']
    ordering_fields = ['rent_start_date', 'rent_end_date', 'final_price', 'deposit']


class RentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    name = 'rent-detail'


TYPEOFDRIVE_CHOICES = (('FWD', 'FWD'), ('RWD', 'RWD'), ('AWD', 'AWD'))
GEARBOX_CHOICES = (('AUTO', 'Auto'), ('MANUAL', 'Manual'))
TYPEOFFUEL_CHOICES = (('DIESEL', 'Diesel'), ('PETROL', 'Petrol'), ('ELECTRIC', 'Electric'), ('HYBRID', 'Hybrid'),)
class VehicleSpecificationFilter(FilterSet):
    min_avg_fuel_consumption = NumberFilter(field_name='avg_fuel_consumption', lookup_expr='gte', label='Average fuel consumption from:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 5.2', 'step': '0.1'}))
    max_avg_fuel_consumption = NumberFilter(field_name='avg_fuel_consumption', lookup_expr='lte', label='Average fuel consumption to:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 9.4', 'step': '0.1'}))
    min_boot_capacity = NumberFilter(field_name='boot_capacity', lookup_expr='gte', label='Boot capacity from:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 100', 'step': '10'}))
    max_boot_capacity = NumberFilter(field_name='boot_capacity', lookup_expr='lte', label='Boot capacity to:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 550', 'step': '10'}))
    min_num_of_doors = NumberFilter(field_name='num_of_doors', lookup_expr='gte', label='Number of doors from:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 2', 'step': '1'}))
    max_num_of_doors = NumberFilter(field_name='num_of_doors', lookup_expr='lte', label='Number of doors to:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 5', 'step': '1'}))
    min_num_of_seats = NumberFilter(field_name='num_of_seats', lookup_expr='gte', label='Number of seats from:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 2', 'step': '1'}))
    max_num_of_seats = NumberFilter(field_name='num_of_seats', lookup_expr='lte', label='Number of seats to:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 5', 'step': '1'}))
    type_of_drive = MultipleChoiceFilter(choices=TYPEOFDRIVE_CHOICES, label='Type of drive:', widget=forms.CheckboxSelectMultiple)
    type_of_fuel = MultipleChoiceFilter(choices=TYPEOFFUEL_CHOICES, label='Type of fuel:', widget=forms.CheckboxSelectMultiple)
    gear_box = ChoiceFilter(choices=GEARBOX_CHOICES, label='Gear box type:', empty_label='Any')


class VehicleSpecificationList(generics.ListCreateAPIView):
    queryset = VehicleSpecification.objects.all()
    serializer_class = VehicleSpecificationSerializer
    name = 'vehiclespecification-list'
    filter_fields = ['color', 'type_of_fuel', 'gear_box', 'type_of_drive', 'avg_fuel_consumption',
     'boot_capacity', 'num_of_doors', 'num_of_seats']
    search_fields = ['$color', 'type_of_fuel', '$gear_box', 'type_of_drive']
    ordering_fields = ['avg_fuel_consumption',
     'boot_capacity', 'num_of_doors', 'num_of_seats']
    filterset_class = VehicleSpecificationFilter


class VehicleSpecificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleSpecification.objects.all()
    serializer_class = VehicleSpecificationSerializer
    name = 'vehiclespecification-detail'


YEAR_CHOICES = [(r, r) for r in range(2000, datetime.date.today().year + 1)]
class VehicleInformationFilter(FilterSet):
    min_year_of_production = ChoiceFilter(choices=YEAR_CHOICES, field_name='year_of_production', lookup_expr='gte', label='Year of production from:', empty_label='Any')
    max_year_of_production = ChoiceFilter(choices=YEAR_CHOICES, field_name='year_of_production', lookup_expr='lte', label='Year of production to:', empty_label='Any')
    min_mileage = NumberFilter(field_name='mileage', lookup_expr='gte', label='Mileage from:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 25000', 'step': '1000'}))
    max_mileage = NumberFilter(field_name='mileage', lookup_expr='lte', label='Mileage to:', widget=forms.NumberInput(attrs={'placeholder': 'Example: 80000', 'step': '1000'}))
    is_condition_comment_filled = BooleanFilter(field_name='condition_comment', method='filled_condition_comment_filter', label='With condition comment', widget=forms.CheckboxInput)
    is_condition_comment_empty = BooleanFilter(field_name='condition_comment', method='empty_condition_comment_filter', label='Without condition comment', widget=forms.CheckboxInput)
    def empty_condition_comment_filter(self, queryset, field_name, value):
        if value:
            return queryset.filter(condition_comment__exact="")
        return queryset 
    def filled_condition_comment_filter(self, queryset, field_name, value):
        if value:
            return queryset.filter(~Q(condition_comment__exact=""))
        return queryset 

class VehicleInformationList(generics.ListCreateAPIView):
    queryset = VehicleInformation.objects.all()
    serializer_class = VehicleInformationSerializer
    name = 'vehicleinformation-list'
    filter_fields = ['year_of_production', 'license_plate_number', 'vin_number', 'date_of_the_review',
     'mileage', 'last_service']
    search_fields = ['$license_plate_number', 'vin_number', '$year_of_production']
    ordering_fields = ['year_of_production', 'date_of_the_review', 'mileage', 'last_service']
    filterset_class = VehicleInformationFilter


class VehicleInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleInformation.objects.all()
    serializer_class = VehicleInformationSerializer
    name = 'vehicleinformation-detail'


CARTYPE_CHOICES = (('SUV', 'Suv'), ('MINIBUS', 'Minibus'), ('LIMOUSINE', 'Limousine'), ('COUPE', 'Coupe'), ('KOMBI', 'Kombi'), ('CITY_CAR', 'City Cars'))
CASH_CHOICES = (('1', 'Available'), ('0', 'Unavailable'))
    
class VehicleFilter(FilterSet):
    min_price_per_day = NumberFilter(field_name='price_per_day', label='Price for one day from:', lookup_expr='gte', widget=forms.NumberInput(attrs={'placeholder': 'Example: 150', 'step': '10'}))
    max_price_per_day = NumberFilter(field_name='price_per_day', label='Price for one day to:', lookup_expr='lte', widget=forms.NumberInput(attrs={'placeholder': 'Example: 1200', 'step': '10'}))
    car_type = MultipleChoiceFilter(choices=CARTYPE_CHOICES, label="Car type:", widget=forms.CheckboxSelectMultiple)
    status = ChoiceFilter(choices=CASH_CHOICES, empty_label='Any')


class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicle-list'
    filter_fields = ['mark', 'model', 'car_type', 'status', 'price_per_day']
    search_fields = ['$mark', '$model', 'car_type', 'price_per_day']
    ordering_fields = ['mark', 'model', 'car_type', 'status', 'price_per_day']
    filterset_class = VehicleFilter


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicle-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'API-Root'

    def get(self, request, *args, **kwargs):
        return Response({
            'address' : reverse(AddressList.name, request=request),
            'client' : reverse(ClientList.name, request=request),
            'payment' : reverse(PaymentList.name, request=request),
            'rent' : reverse(RentList.name, request=request),
            'vehicle' : reverse(VehicleList.name, request=request),
            'vehicle_information' : reverse(VehicleInformationList.name, request=request),
            'vehicle_specification' : reverse(VehicleSpecificationList.name, request=request),
        })
