from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='Clientes'),     
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),  
]
