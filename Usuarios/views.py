from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def LoginView(request):
    return render(request, 'login.html')


def RolesViews(request):
    roles = Roles.objects.all()
    return render(request, 'roles.html', {'roles': roles})


def AgregarRole(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        description = request.POST.get('Description')
        Roles.objects.create(Name=name, Description=description)
        return redirect('UsersView')  # redirige a la lista de roles
    return render(request, 'roles/agregar_role.html')  # si quieres mostrar un formulario aparte

def UsersListView(request):
    usuarios = Usuarios.objects.all()
    return render(request,'users.html', {'usuarios':usuarios})
