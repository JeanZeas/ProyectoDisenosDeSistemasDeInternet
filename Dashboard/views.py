from django.shortcuts import render

# Create your views here.

def MainView(request):
    return render(request, 'main.html')

def Reports(request):
    return render(request, 'reports.html')
