from django.shortcuts import render
import requests
from django.views import View
from serialApp.forms import ParticipanteForm, InstitucionForm
from django.http import JsonResponse


# Create your views here.

class ListaParticipante(View):
    def get(self, request):
        url = 'http://localhost:8000/api_participante/'
        response = requests.get(url)

        participantes = response.json()
        context = {
            'participantes': participantes
        }
        return render(request, 'participantes.html', context)

class IngresarParticipante(View):
    def get(self, request):
        form = ParticipanteForm()
        context = {
            'form': form
        }
        return render(request, 'ingresar_participante.html', context)

    def post(self, request):
        form = ParticipanteForm(request.POST)
        return render(request, 'ingresar_participante.html')

#########################################################################

def instituciones(request):
    response = requests.get('http://localhost:8000/api_institucion/')

    instituciones = response.json()
    context = {
        'instituciones': instituciones
    }
    return render(request, 'instituciones.html', context)

def ingresar_institucion(request):
    form = InstitucionForm()
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post('http://localhost:8000/api_institucion/', data=data)
            
    context = {
        'form': form
    }

    return render(request, 'ingresar_institucion.html', context)

###########################################################################    

def inicio(request):
    return render(request, 'inicio.html')

