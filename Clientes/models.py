from django.db import models

# Create your models here.

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(
        max_length=10,
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        blank=True,
        null=True
    )
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True)  # True = Activo, False = Inactivo

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Membresia(models.Model):
    nombre = models.CharField(max_length=50)
    duracion_dias = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True)
    fecha_pago = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Pago de {self.cliente.nombre} el {self.fecha_pago}"
