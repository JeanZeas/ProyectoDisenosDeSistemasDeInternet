from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
# Create your views here.

def Clientes(request):
    return render(request, 'Clientes.html')


def lista_clientes(request):
    clientes = Cliente.objects.all()  # Obtiene todos los clientes de la base de datos
    return render(request, 'Clientes/clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clientes')  # coincide con el name de la URL
    else:
        form = ClienteForm()
    return render(request, 'Clientes/agregar_cliente.html', {'form': form})

