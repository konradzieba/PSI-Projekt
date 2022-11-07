from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Address, Client, Payment, Rent, VehicleInformation, VehicleSpecification, Vehicle
from .serializers import AddressSerializer, ClientSerializer, PaymentSerializer, RentSerializer, \
    VehicleInformationSerializer, VehicleSpecificationSerializer, VehicleSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-list'


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    name = 'payment-list'


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    name = 'payment-detail'


class RentList(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    name = 'rent-list'


class RentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    name = 'rent-detail'


class VehicleInformationList(generics.ListCreateAPIView):
    queryset = VehicleInformation.objects.all()
    serializer_class = VehicleInformationSerializer
    name = 'vehicleinformation-list'


class VehicleInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleInformation.objects.all()
    serializer_class = VehicleInformationSerializer
    name = 'vehicleinformation-detail'


class VehicleSpecificationList(generics.ListCreateAPIView):
    queryset = VehicleSpecification.objects.all()
    serializer_class = VehicleSpecificationSerializer
    name = 'vehiclespecification-list'


class VehicleSpecificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleSpecification.objects.all()
    serializer_class = VehicleSpecificationSerializer
    name = 'vehiclespecification-detail'


class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicle-list'


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
