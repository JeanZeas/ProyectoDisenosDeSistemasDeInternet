from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect('UsersView')
    return render(request, 'roles/agregar_role.html')  

def UsersListView(request):
    usuarios = Usuarios.objects.all()
    return render(request,'users.html', {'usuarios': usuarios})

# Crear usuario admin predeterminado
def crear_usuario_predeterminado(request):
    role, _ = Roles.objects.get_or_create(Name="Admin", Description="Administrador")
    if not Usuarios.objects.filter(Username='admin').exists():
        user = Usuarios(
            Username='admin',
            EMail='admin@aquiles.com',
            FirstName='Admin',
            LastName='User',
            PhoneNumber='00000000000',
            Role=role
        )
        user.set_password('12345')
        user.save()
    return HttpResponse("Usuario admin creado correctamente")

#  Crear usuario
def CrearUsuarioView(request):
    roles = Roles.objects.all()
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName')
        phone = request.POST.get('PhoneNumber')
        password = request.POST.get('Password')
        role_id = request.POST.get('Role')

        role = Roles.objects.get(id=role_id)
        nuevo_usuario = Usuarios(
            Username=username,
            EMail=email,
            FirstName=first_name,
            LastName=last_name,
            PhoneNumber=phone,
            Role=role
        )
        nuevo_usuario.set_password(password)  # encriptar contraseña
        nuevo_usuario.save()
        return redirect('UsersListView')
    return render(request, 'usuarios/agregar_usuario.html', {'roles': roles})

#  Editar usuario
def EditarUsuarioView(request, user_id):
    usuario = get_object_or_404(Usuarios, id=user_id)
    roles = Roles.objects.all()
    if request.method == 'POST':
        usuario.Username = request.POST.get('Username')
        usuario.EMail = request.POST.get('Email')
        usuario.FirstName = request.POST.get('FirstName')
        usuario.LastName = request.POST.get('LastName')
        usuario.PhoneNumber = request.POST.get('PhoneNumber')
        role_id = request.POST.get('Role')
        usuario.Role = Roles.objects.get(id=role_id)

        # Solo cambiar contraseña si se ingresa una nueva
        new_password = request.POST.get('Password')
        if new_password:
            usuario.set_password(new_password)

        usuario.save()
        return redirect('UsersListView')
    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario, 'roles': roles})

#  Eliminar usuario
def EliminarUsuarioView(request, user_id):
    usuario = get_object_or_404(Usuarios, id=user_id)
    usuario.delete()
    return redirect('UsersListView')

