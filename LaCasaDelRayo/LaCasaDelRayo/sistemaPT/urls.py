from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # ruta principal de la app
    path('base/', views.base, name="base"),
    path('login', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('acceso/', views.acceso, name="acceso"),
    path('clientes/', views.clientes, name="clientes"),
    path('datos/', views.datos, name="datos"),
    path('empleados/', views.empleados, name='empleados'),
    path('finanzas/', views.finanzas, name='finanzas'),
    path('insumos/', views.insumos, name='insumos'),
]

