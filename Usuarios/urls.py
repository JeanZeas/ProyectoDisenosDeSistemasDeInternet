from django.urls import path
from . import views
urlpatterns = [
    path('',views.LoginView,name='LoginView'),
    path('Roles View', views.RolesViews, name='UsersView'),
    path('roles/agregar/', views.AgregarRole, name='AgregarRole'),
    path('Users List', views.UsersListView, name='UsersListView'),
    
]

