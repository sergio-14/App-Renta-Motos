from django.shortcuts import render
from .models import Alquiler

def home(request):
    return render(request, 'home.html')

def alquileres(request):
    alquileres_list = Alquiler.objects.all()
    context = {
        'alquileres': alquileres_list,
    }
    return render(request, 'alquileres.html', context)
