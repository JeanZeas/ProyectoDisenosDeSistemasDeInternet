from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Usuarios'

    def ready(self):
        from .models import Usuarios, Roles

        role, _ = Roles.objects.get_or_create(Name="Admin", Description="Administrador")
        if not Usuarios.objects.filter(Username='admin').exists():
            user = Usuarios(
                Username='admin',
                EMail='admin@aquiles.com',
                FirstName='Admin',
                LastName='User',
                PhoneNumber='00000000000',
                Role=role
            )
            user.set_password('12345')  # contraseña encriptada
            user.save()
