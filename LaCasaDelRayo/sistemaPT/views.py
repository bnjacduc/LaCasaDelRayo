from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def base (request):
    return render (request,'base.html')

def login_view(request):
    return render(request, 'login.html')