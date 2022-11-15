from rest_framework.validators import UniqueValidator
from .models import Address, Client, Payment, Rent, Vehicle, VehicleInformation, VehicleSpecification
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['url', 'id', 'zip_code', 'town', 'country', 'street', 'apartment_number', 'full_name']


class ClientSerializer(serializers.ModelSerializer):
    address = serializers.SlugRelatedField(queryset=Address.objects.all(), slug_field='full_name', validators=[
        UniqueValidator(queryset=Client.objects.all(), message="client with this address already exists")])

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
    vehicle_specification = serializers.SlugRelatedField(queryset=VehicleSpecification.objects.all(),
                                                         slug_field='full_name', validators=[
            UniqueValidator(queryset=Vehicle.objects.all(), message="vehicle with this specification already exists")])
    vehicle_information = serializers.SlugRelatedField(queryset=VehicleInformation.objects.all(),
                                                       slug_field='full_name', validators=[
            UniqueValidator(queryset=Vehicle.objects.all(), message="vehicle with this information already exists")])

    class Meta:
        model = Vehicle
        fields = ['url', 'id', 'car_type', 'status', 'mark', 'model',
                  'price_per_day', 'vehicle_specification', 'vehicle_information']


class RentSerializer(serializers.ModelSerializer):
    vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(), slug_field='full_name', validators=[
        UniqueValidator(queryset=Rent.objects.all(), message="rent with this vehicle already exists")])
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='full_name', validators=[
        UniqueValidator(queryset=Rent.objects.all(), message="rent with this client already exists")])
    payment = serializers.SlugRelatedField(queryset=Payment.objects.all(), slug_field='full_name', validators=[
        UniqueValidator(queryset=Rent.objects.all(), message="rent with this payment already exists")])

    class Meta:
        model = Rent
        fields = ['url', 'id', 'rent_start_date', 'rent_end_date', 'final_price',
                  'discount_in_perc', 'deposit', 'km_limit', 'price_per_day', 'number_of_days', 'payment', 'vehicle', 'client']

    def validate(self, data):
        if data['rent_start_date'] > data['rent_end_date']:
            raise serializers.ValidationError(
                {'rent_end_date': 'Rent end date can not be before Rent start date'})
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'username', 'password', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
