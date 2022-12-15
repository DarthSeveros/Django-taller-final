from django.shortcuts import render
import requests

# Create your views here.

def participantes(request):
    response = requests.get('http://localhost:8000/api_participante/')

    participantes = response.json()
    context = {
        'participantes': participantes
    }
    return render(request, 'participantes.html', context)

def instituciones(request):
    response = requests.get('http://localhost:8000/api_institucion/')

    instituciones = response.json()
    context = {
        'instituciones': instituciones
    }
    return render(request, 'instituciones.html', context)

def inicio(request):
    return render(request, 'inicio.html')

