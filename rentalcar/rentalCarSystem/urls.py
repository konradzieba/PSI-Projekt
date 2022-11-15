from django.urls import path, include
from . import views
from .views import UserDetailAPI, RegisterUserAPIView

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('address/', views.AddressList.as_view(), name=views.AddressList.name),
    path('address/<int:pk>', views.AddressDetail.as_view(), name=views.AddressDetail.name),
    path('client/', views.ClientList.as_view(), name=views.ClientList.name),
    path('client/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('payment/', views.PaymentList.as_view(), name=views.PaymentList.name),
    path('payment/<int:pk>', views.PaymentDetail.as_view(), name=views.PaymentDetail.name),
    path('rent/', views.RentList.as_view(), name=views.RentList.name),
    path('rent/<int:pk>', views.RentDetail.as_view(), name=views.RentDetail.name),
    path('vehicle_information/', views.VehicleInformationList.as_view(), name=views.VehicleInformationList.name),
    path('vehicle_information/<int:pk>', views.VehicleInformationDetail.as_view(), name=views.VehicleInformationDetail.name),
    path('vehicle_specification/', views.VehicleSpecificationList.as_view(), name=views.VehicleSpecificationList.name),
    path('vehicle_specification/<int:pk>', views.VehicleSpecificationDetail.as_view(), name=views.VehicleSpecificationDetail.name),
    path('vehicle/', views.VehicleList.as_view(), name=views.VehicleList.name),
    path('vehicle/<int:pk>', views.VehicleDetail.as_view(), name=views.VehicleDetail.name),
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('get-details', UserDetailAPI.as_view()),
    path('register', RegisterUserAPIView.as_view()),
]
