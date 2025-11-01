from django.urls import path
from . import views

urlpatterns = [
    path('Products/',views.Productos, name='Products')
]