from django.shortcuts import render

# Create your views here.

def Productos(request):
    return render(request, 'Productos.html')
