from django.shortcuts import render, redirect
import requests
from django.views import View
from .forms import InstitucionForm, ParticipanteForm
from django.http import JsonResponse
from django.urls import reverse
import datetime

API_PARTICIPANTE = 'http://localhost:8000/api_participante/'
API_INSTITUCION = 'http://localhost:8000/api_institucion/'

class ListaParticipante(View):
    def get(self, request):
        response = requests.get(API_PARTICIPANTE)

        participantes = response.json()
        context = {
            'participantes': participantes
        }
        return render(request, 'participantes.html', context)

class EliminarParticipante(View):
    def post(self, request, id):
        requests.delete(f'http://localhost:8000/api_participante/{id}')
        return redirect(reverse('participantes'))

class IngresarParticipante(View):
    def get(self, request):
        institucionResponse = requests.get(API_INSTITUCION)
        instituciones = institucionResponse.json()
        form = ParticipanteForm(choices=instituciones)
        context = {
            'form': form
        }
        return render(request, 'ingresar_participante.html', context)

    def post(self, request):
        institucionResponse = requests.get(API_INSTITUCION)
        instituciones = institucionResponse.json()
        form = ParticipanteForm(request.POST, choices=instituciones)
        if form.is_valid():
            data = form.cleaned_data
            requests.post(API_PARTICIPANTE, data=data)
            return redirect(reverse('participantes'))
        context = {
            'form': form
        }
        return render(request, 'ingresar_participante.html', context)

class ActualizarParticipante(View):
    def get(self, request, id):
        institucionResponse = requests.get(API_INSTITUCION)
        instituciones = institucionResponse.json()
        form = ParticipanteForm(request, choices=instituciones)
        response = requests.get(f'http://localhost:8000/api_participante/{id}')
        participante = response.json()
        form.data = participante
        form.data['institucion'] = form.data['institucion']['id']
        context = {
            'form': form,
            'id_participante': participante['id']
        }
        return render(request, 'actualizar_participante.html', context)

    def post(self, request, id):
        institucionResponse = requests.get(API_INSTITUCION)
        instituciones = institucionResponse.json()
        form = ParticipanteForm(request.POST, choices=instituciones)
        if form.is_valid():
            data = form.cleaned_data
            requests.put(API_PARTICIPANTE+str(id), data=data)
            return redirect(reverse('participantes'))
        context = {
            'form': form,
            'id_participante': form.data['id']
        }
        return render(request, 'actualizar_participante.html', context)

#########################################################################

def instituciones(request):
    response = requests.get(API_INSTITUCION)

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
            response = requests.post(API_INSTITUCION, data=data)
            return redirect(reverse('instituciones'))
    context = {
        'form': form
    }

    return render(request, 'ingresar_institucion.html', context)

def eliminar_institucion(request, id):
    requests.delete(f'http://localhost:8000/api_institucion/{id}')
    return redirect(reverse('instituciones'))

###########################################################################    

def inicio(request):
    return render(request, 'inicio.html')

