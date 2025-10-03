from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),  # ruta principal de la app
    path('base/', views.base, name="base"),
    path('', views.login_view, name='login'),
]
