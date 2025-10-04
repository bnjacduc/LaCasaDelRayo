from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm





def inicio(request):
    return render(request, 'inicio/inicio.html')

def base (request):
    return render (request,'inicio/base.html')

def login_view(request):
    return render(request, 'iniciosesion/login.html')
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # logea al usuario recién creado
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


def acceso(request):
    return render (request,'acceso/acceso.html')

def clientes (request):
    return render (request,'clientes/clientes.html')

def datos (request):
    return render (request,'datos/datos.html')

def empleados(request):
    return render (request,'empleados/empleados.html')
def finanzas(request):
    return render (request,'finanzas/finanzas.html')
def insumos(request):
    return render (request,'insumos/insumos.html')
