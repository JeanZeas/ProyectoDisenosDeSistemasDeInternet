from django.shortcuts import render

# Create your views here.
def Clientes(request):
    return render(request, 'Clientes.html')