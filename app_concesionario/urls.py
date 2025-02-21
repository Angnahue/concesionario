from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cliente/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('modelo/nuevo/', views.crear_modelo, name='crear_modelo'),
    path('vendedor/nuevo/', views.crear_vendedor, name='crear_vendedor'),
    path('modelo/buscar/', views.buscar_modelo, name='buscar_modelo'),
]