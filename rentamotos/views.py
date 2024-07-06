from django.shortcuts import render, redirect
from .models import Alquiler
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

from django.db.models import Sum
from .models import Alquiler


def alquileres(request):
    # Obtener parámetros de filtro
    fecha = request.GET.get('fecha')
    nombre_cliente = request.GET.get('cliente')

    # Filtrar los alquileres según los parámetros recibidos
    alquileres_list = Alquiler.objects.all()

    if fecha:
        alquileres_list = alquileres_list.filter(fecha=fecha)

    if nombre_cliente:
        alquileres_list = alquileres_list.filter(cliente=nombre_cliente)

    # Calcular el monto total de los alquileres filtrados
    monto_total = alquileres_list.aggregate(Sum('monto'))['monto__sum']

    context = {
        'alquileres': alquileres_list,
        'monto_total': monto_total if monto_total else 0,
    }

    if request.method == 'POST':
        if 'devolver_moto' in request.POST:
            alquiler_id = request.POST.get('alquiler_id')
            try:
                alquiler = Alquiler.objects.get(pk=alquiler_id)
                alquiler.moto.estado = 'disponible'  
                alquiler.moto.save() 
                alquiler.estado = 'disponible' 
                alquiler.save()  
            except Alquiler.DoesNotExist:
                pass 
          
            return redirect('home')

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


from django.shortcuts import render, redirect
from datetime import datetime
from .models import Alquiler, Cliente, Moto

from datetime import datetime, time
from django.shortcuts import render, redirect
from .models import Alquiler, Cliente, Moto


def crear_alquiler(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        moto_id = request.POST.get('moto')
        hora_inicio_str = request.POST.get('hora_inicio')
        hora_fin_str = request.POST.get('hora_fin')

        try:
            cliente = Cliente.objects.get(ndi=cliente_id)
            moto = Moto.objects.get(pk=moto_id)

            # Convertir hora_inicio_str y hora_fin_str a objetos time
            hora_inicio = datetime.strptime(hora_inicio_str, '%H:%M').time()
            hora_fin = datetime.strptime(hora_fin_str, '%H:%M').time()

            alquiler = Alquiler(
                fecha=datetime.now().date(),
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                cliente=cliente,
                moto=moto,
                estado='ocupado',  # Estado se establece automáticamente como 'ocupado'
            )

            alquiler.save()

            # Actualizar el estado de la moto a 'ocupado'
            moto.estado = 'ocupado'
            moto.save()

            return redirect('alquileres')  # Redirigir a una página de confirmación si es necesario
        except (Cliente.DoesNotExist, Moto.DoesNotExist):
            # Manejar errores si el cliente o la moto no existen
            return render(request, 'error.html', {'mensaje': 'Cliente o moto no encontrados'})
    
    # Obtener todos los clientes y motos disponibles para el formulario
    clientes = Cliente.objects.all()
    
    # Filtrar motos disponibles que no estén ocupadas
    motos = Moto.objects.filter(estado='disponible')

    context = {
        'clientes': clientes,
        'motos': motos,
    }
    return render(request, 'crear_alquiler.html', context)


def lista_motos(request):
    motos = Moto.objects.all()
    return render(request, 'lista_motos.html', {'motos': motos})