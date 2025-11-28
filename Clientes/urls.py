from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='Clientes'),     
    path('agregar/', views.agregar_cliente, name='agregar_cliente'), 
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),

]
