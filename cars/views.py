from django.shortcuts import render
from .models import Car, Bicycle

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'cars/bicycle_list.html', {'bicycles': bicycles})
