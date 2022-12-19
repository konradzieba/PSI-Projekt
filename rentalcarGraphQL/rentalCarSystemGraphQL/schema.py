import graphene
from graphene_django import DjangoObjectType
from .models import Client, Vehicle, Rent
from django.db.models import Q

# TYPE
class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'pesel',
            'driver_licence_number',
            'phone_number',
            'email',
            'gender',
        )


class VehicleType(DjangoObjectType):
    class Meta:
        model = Vehicle
        fields = (
            'id',
            'car_type',
            'status',
            'mark',
            'model',
            'price_per_day'
        )


class RentType(DjangoObjectType):
    class Meta:
        model = Rent
        fields = (
            'id',
            'rent_start_date',
            'rent_end_date',
            'final_price',
            'km_limit',
            'vehicle',
            'client'
        )


# QUERY
class Query(graphene.ObjectType):
    clients = graphene.List(ClientType)
    vehicles = graphene.List(VehicleType)
    rents = graphene.List(RentType)
    rent_price_range = graphene.List(RentType, min_price=graphene.Int(), max_price=graphene.Int())
    rent_start_date_range = graphene.List(RentType, min_start_date=graphene.Date(), max_start_date=graphene.Date())
    rent_km_limit_range = graphene.List(RentType, min_km_limit=graphene.Int(), max_km_limit=graphene.Int())
    rent_client_gender = graphene.List(RentType, gender=graphene.String())
    rent_vehicle_mark_and_model = graphene.List(RentType, mark=graphene.String(required=True), model=graphene.String())

    def resolve_clients(root, info, **kwargs):
        return Client.objects.all()

    def resolve_vehicles(root, info, **kwargs):
        return Vehicle.objects.all()

    def resolve_rents(root, info, **kwargs):
        return Rent.objects.all()

    def resolve_client_by_gender(root, info, gender):
        return Client.objects.filter(gender=gender)

    def resolve_rent_price_range(root, info, min_price=None, max_price=None, **kwargs):
        qs = Rent.objects.all()
        if min_price is not None:
            qs = qs.filter(final_price__gte=min_price)
        if max_price is not None:
            qs = qs.filter(final_price__lte=max_price)
        return qs

    def resolve_rent_start_date_range(root, info, min_start_date=None, max_start_date=None, **kwargs):
        qs = Rent.objects.all()
        if min_start_date is not None:
            qs = qs.filter(rent_start_date__gte=min_start_date)
        if max_start_date is not None:
            qs = qs.filter(rent_start_date__lte=max_start_date)
        return qs

    def resolve_rent_km_limit_range(root, info, min_km_limit=None, max_km_limit=None, **kwargs):
        qs = Rent.objects.all()
        if min_km_limit is not None:
            qs = qs.filter(km_limit__gte=min_km_limit)
        if max_km_limit is not None:
            qs = qs.filter(km_limit__lte=max_km_limit)
        return qs

    def resolve_rent_client_gender(root, info, gender=None, **kwargs):
        qs = Rent.objects.all()
        if gender is not None:
            qs = qs.filter(client__gender=gender)
        return qs

    def resolve_rent_vehicle_mark_and_model(root, info, mark, model=None, **kwargs):
        qs = Rent.objects.all()
        q = Q(vehicle__model=model) & Q(vehicle__mark=mark)
        if model is not None:
            qs = qs.filter(q)
        else:
            qs = qs.filter(vehicle__mark=mark)
        return qs


# CREATE
class CreateClient(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        birth_date = graphene.Date()
        pesel = graphene.String()
        driver_licence_number = graphene.String()
        phone_number = graphene.String()
        email = graphene.String()
        gender = graphene.String()

    client = graphene.Field(ClientType)

    def mutate(self, info, first_name, last_name, birth_date, pesel, driver_licence_number, phone_number, email, gender):
        client = Client.objects.create(first_name=first_name,
                                       last_name=last_name,
                                       birth_date=birth_date,
                                       pesel=pesel,
                                       driver_licence_number=driver_licence_number,
                                       phone_number=phone_number,
                                       email=email,
                                       gender=gender)
        return CreateClient(client=client)


class CreateVehicle(graphene.Mutation):
    class Arguments:
        car_type = graphene.String()
        status = graphene.Boolean()
        mark = graphene.String()
        model = graphene.String()
        price_per_day = graphene.Int()

    vehicle = graphene.Field(VehicleType)

    def mutate(self, info, car_type, status, mark, model, price_per_day):
        vehicle = Vehicle.objects.create(car_type=car_type,
                                         status=status,
                                         mark=mark,
                                         model=model,
                                         price_per_day=price_per_day)
        return CreateVehicle(vehicle=vehicle)


class CreateRent(graphene.Mutation):
    class Arguments:
        rent_start_date = graphene.Date()
        rent_end_date = graphene.Date()
        final_price = graphene.Int()
        km_limit = graphene.Int()
        vehicle = graphene.Int()
        client = graphene.Int()

    rent = graphene.Field(RentType)

    def mutate(self, info, rent_start_date, rent_end_date, final_price, km_limit, vehicle, client):
        client = Client.objects.get(pk=client)
        vehicle = Vehicle.objects.get(pk=vehicle)
        rent = Rent.objects.create(rent_start_date=rent_start_date,
                                   rent_end_date=rent_end_date,
                                   final_price=final_price,
                                   km_limit=km_limit,
                                   vehicle=vehicle,
                                   client=client)
        return CreateRent(rent=rent)


# DELETE
class DeleteClientInput(graphene.InputObjectType):
    id = graphene.ID(required=True)


class DeleteClient(graphene.Mutation):
    class Arguments:
        client_data = DeleteClientInput(required=True)

    success = graphene.Boolean()

    def mutate(self, info, client_data):
        client = Client.objects.get(pk=client_data.id)
        client.delete()
        return DeleteClient(success=True)


class DeleteVehicleInput(graphene.InputObjectType):
    id = graphene.ID(required=True)


class DeleteVehicle(graphene.Mutation):
    class Arguments:
        vehicle_data = DeleteVehicleInput(required=True)

    success = graphene.Boolean()

    def mutate(self, info, vehicle_data):
        vehicle = Vehicle.objects.get(pk=vehicle_data.id)
        vehicle.delete()
        return DeleteVehicle(success=True)


class DeleteRentInput(graphene.InputObjectType):
    id = graphene.ID(required=True)


class DeleteRent(graphene.Mutation):
    class Arguments:
        rent_data = DeleteRentInput(required=True)

    success = graphene.Boolean()

    def mutate(self, info, rent_data):
        rent = Rent.objects.get(pk=rent_data.id)
        rent.delete()
        return DeleteRent(success=True)


# UPDATE
class UpdateClientInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    first_name = graphene.String()
    last_name = graphene.String()
    birth_date = graphene.Date()
    pesel = graphene.String()
    driver_licence_number = graphene.String()
    phone_number = graphene.String()
    email = graphene.String()
    gender = graphene.String()


class UpdateClient(graphene.Mutation):
    class Arguments:
        client_data = UpdateClientInput(required=True)

    client = graphene.Field(ClientType)

    def mutate(self, info, client_data):
        client = Client.objects.get(pk=client_data.id)
        if 'first_name' in client_data:
            client.first_name = client_data.first_name
        if 'last_name' in client_data:
            client.last_name = client_data.last_name
        if 'birth_date' in client_data:
            client.birth_date = client_data.birth_date
        if 'pesel' in client_data:
            client.pesel = client_data.pesel
        if 'driver_licence_number' in client_data:
            client.driver_licence_number = client_data.driver_licence_number
        if 'phone_number' in client_data:
            client.phone_number = client_data.phone_number
        if 'email' in client_data:
            client.email = client_data.email
        if 'gender' in client_data:
            client.gender = client_data.gender
        client.save()
        return UpdateClient(client=client)


class UpdateVehicleInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    car_type = graphene.String()
    status = graphene.Boolean()
    mark = graphene.String()
    model = graphene.String()
    price_per_day = graphene.Int()


class UpdateVehicle(graphene.Mutation):
    class Arguments:
        vehicle_data = UpdateVehicleInput(required=True)

    vehicle = graphene.Field(VehicleType)

    def mutate(self, info, vehicle_data):
        vehicle = Vehicle.objects.get(pk=vehicle_data.id)
        if 'car_type' in vehicle_data:
            vehicle.car_type = vehicle_data.car_type
        if 'status' in vehicle_data:
            vehicle.status = vehicle_data.status
        if 'mark' in vehicle_data:
            vehicle.mark = vehicle_data.mark
        if 'model' in vehicle_data:
            vehicle.model = vehicle_data.model
        if 'price_per_day' in vehicle_data:
            vehicle.price_per_day = vehicle_data.price_per_day
        vehicle.save()
        return UpdateVehicle(vehicle=vehicle)


class UpdateRentInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    rent_start_date = graphene.Date()
    rent_end_date = graphene.Date()
    final_price = graphene.Int()
    km_limit = graphene.Int()
    vehicle = graphene.ID()
    client = graphene.ID()


class UpdateRent(graphene.Mutation):
    class Arguments:
        rent_data = UpdateRentInput(required=True)

    rent = graphene.Field(RentType)

    @staticmethod
    def mutate(self, info, rent_data):
        rent = Rent.objects.get(pk=rent_data.id)
        if 'rent_start_date' in rent_data:
            rent.rent_start_date = rent_data.rent_start_date
        if 'rent_end_date' in rent_data:
            rent.rent_end_date = rent_data.rent_end_date
        if 'final_price' in rent_data:
            rent.final_price = rent_data.final_price
        if 'km_limit' in rent_data:
            rent.km_limit = rent_data.km_limit
        if 'vehicle' in rent_data:
            rent.vehicle = Vehicle.objects.get(pk=rent_data.vehicle)
        if 'client' in rent_data:
            rent.client = Client.objects.get(pk=rent_data.client)
        rent.save()
        return UpdateRent(rent=rent)


class Mutation(graphene.ObjectType):
    create_client = CreateClient.Field()
    create_vehicle = CreateVehicle.Field()
    create_rent = CreateRent.Field()
    delete_client = DeleteClient.Field()
    delete_vehicle = DeleteVehicle.Field()
    delete_rent = DeleteRent.Field()
    update_client = UpdateClient.Field()
    update_vehicle = UpdateVehicle.Field()
    update_rent = UpdateRent.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)