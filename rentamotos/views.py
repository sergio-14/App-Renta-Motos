from django.shortcuts import render, redirect
from .models import Alquiler
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def alquileres(request):
    alquileres_list = Alquiler.objects.all()
    context = {
        'alquileres': alquileres_list,
    }
    return render(request, 'alquileres.html', context)

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Usuario y/o contraseña incorrectos."
            return render(request, 'signin.html', {'error_message': error_message})
    return render(request, 'signin.html')