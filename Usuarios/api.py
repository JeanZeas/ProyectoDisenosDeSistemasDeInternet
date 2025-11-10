from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Usuarios, Roles
from django.contrib.auth.hashers import make_password
import json

# Obtener todos los usuarios
def usuarios_list(request):
    if request.method == 'GET':
        usuarios = list(Usuarios.objects.values())
        return JsonResponse({'usuarios': usuarios}, safe=False)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Obtener usuario por ID
def usuario_detail(request, id):
    if request.method == 'GET':
        usuario = get_object_or_404(Usuarios, id=id)
        data = {
            'id': usuario.id,
            'Username': usuario.Username,
            'EMail': usuario.EMail,
            'FirstName': usuario.FirstName,
            'LastName': usuario.LastName,
            'PhoneNumber': usuario.PhoneNumber,
            'Role': usuario.Role.Name
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Crear usuario
@csrf_exempt
def usuario_create(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        role = Roles.objects.get(id=body['Role'])
        nuevo_usuario = Usuarios.objects.create(
            Username=body['Username'],
            Password=make_password(body['Password']),
            EMail=body['EMail'],
            FirstName=body['FirstName'],
            LastName=body['LastName'],
            PhoneNumber=body['PhoneNumber'],
            Role=role
        )
        return JsonResponse({'mensaje': f'Usuario {nuevo_usuario.Username} creado correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Eliminar usuario
@csrf_exempt
def usuario_delete(request, id):
    if request.method == 'DELETE':
        usuario = get_object_or_404(Usuarios, id=id)
        usuario.delete()
        return JsonResponse({'mensaje': 'Usuario eliminado correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)
