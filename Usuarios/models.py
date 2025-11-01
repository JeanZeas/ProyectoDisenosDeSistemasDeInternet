from django.db import models

# Create your models here.

class Roles(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=255)


class Usuarios(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    EMail = models.EmailField(max_length=250)
    FirstName  = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=11)
    Role = models.ForeignKey('Roles', on_delete=models.CASCADE)

