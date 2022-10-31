from django.shortcuts import render
from django.http import HttpResponse
import datetime


def cars(request):
    return render(request, "index.html")
# Create your views here.
