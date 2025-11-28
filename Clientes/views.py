from django.shortcuts import render, redirect, get_object_or_404
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

def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('Clientes')


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('Clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'Clientes/editar_cliente.html', {'form': form})