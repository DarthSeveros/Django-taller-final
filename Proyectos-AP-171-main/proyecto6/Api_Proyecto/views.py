from django.shortcuts import render
from django.http import JsonResponse
from Api_Proyecto.models import Empleado

# Create your views here.
def verempleados(request):
    emp = {
        'id': 123,
        'nombre': 'pedro',
        'email': 'pedro@gmail.com',
        'sueldo': '5000000000'
    }
    return JsonResponse(emp)

def empleadosDB(request):
    emple = Empleado.objects.all()
    data = {'empleados' : list(emple.values('nombre', 'sueldo'))}
    
    return JsonResponse(data)