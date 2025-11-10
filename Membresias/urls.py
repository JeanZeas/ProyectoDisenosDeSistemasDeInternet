from django.urls import path
from . import views

urlpatterns = [
    path('Membresias/',views.Membresias, name='Membresias')
]