from .models import Address, Client, Payment, Rent, Vehicle, VehicleInformation, VehicleSpecification
from rest_framework import serializers



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['url', 'id', 'zip_code', 'town', 'country', 'street', 'apartment_number', 'full_name']


class ClientSerializer(serializers.ModelSerializer):
    address = serializers.SlugRelatedField(queryset=Address.objects.all(), slug_field='full_name')

    class Meta:
        model = Client
        fields = ['url', 'id', 'first_name', 'last_name', 'birth_date',
                  'pesel', 'driver_licence_number', 'phone_number', 'email', 'address']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['url', 'id', 'cash', 'card_number']


class VehicleSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSpecification
        fields = ['url', 'id', 'color', 'gear_box', 'type_of_drive', 'type_of_fuel',
                  'avg_fuel_consumption', 'num_of_doors', 'num_of_seats', 'boot_capacity']


class VehicleInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInformation
        fields = ['url', 'id', 'year_of_production', 'license_plate_number', 'vin_number',
                  'date_of_the_review', 'condition_comment', 'mileage', 'last_service']


class VehicleSerializer(serializers.ModelSerializer):
    vehicle_specification = serializers.SlugRelatedField(queryset=VehicleSpecification.objects.all(), slug_field='full_name')
    vehicle_information = serializers.SlugRelatedField(queryset=VehicleInformation.objects.all(), slug_field='full_name')

    class Meta:
        model = Vehicle
        fields = ['url', 'id', 'car_type', 'status', 'mark', 'model',
                  'price_per_day', 'vehicle_specification', 'vehicle_information']


class RentSerializer(serializers.ModelSerializer):
    vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(), slug_field='full_name')
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='full_name')
    payment = serializers.SlugRelatedField(queryset=Payment.objects.all(), slug_field='full_name')

    class Meta:
        model = Rent
        fields = ['url', 'id', 'rent_start_date', 'rent_end_date', 'final_price',
                  'discount_in_perc', 'deposit', 'km_limit', 'payment', 'vehicle', 'client']

    def validate(self, data):
        if data['rent_start_date'] > data['rent_end_date']:
            raise serializers.ValidationError(
                {'rent_end_date': 'Rent end date can not be before Rent start date'})
        return data
