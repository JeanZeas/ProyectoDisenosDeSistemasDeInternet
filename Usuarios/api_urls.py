from django.urls import path
from . import api 

urlpatterns = [
    path('usuarios/', api.usuarios_list, name='usuarios_list'),
    path('usuarios/<int:id>/', api.usuario_detail, name='usuario_detail'),
    path('usuarios/crear/', api.usuario_create, name='usuario_create'),
    path('usuarios/eliminar/<int:id>/', api.usuario_delete, name='usuario_delete'),
]
