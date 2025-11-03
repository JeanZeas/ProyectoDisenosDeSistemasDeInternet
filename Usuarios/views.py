from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios, Roles

# Login
def LoginView(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Usuarios.objects.get(Username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id
                return redirect('MainView')  
            else:
                error = "Contraseña incorrecta"
        except Usuarios.DoesNotExist:
            error = "Usuario no encontrado"
    return render(request, 'login.html', {'error': error})

# Roles
def RolesViews(request):
    roles = Roles.objects.all()
    return render(request, 'roles.html', {'roles': roles})

# Agregar rol
def AgregarRole(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        description = request.POST.get('Description')
        Roles.objects.create(Name=name, Description=description)
        return redirect('UsersView')  # coincide con name='UsersView'
    return render(request, 'roles/agregar_role.html')

# Lista de usuarios
def UsersListView(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('LoginView')
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
        user.set_password('12345')  # encriptación
        user.save()
    return HttpResponse("Usuario admin creado correctamente")
