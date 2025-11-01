from django.urls import path
from . import views

urlpatterns = [
    path('MainView', views.MainView, name='MainView'),
    path('Reports', views.Reports, name='Reports')
]