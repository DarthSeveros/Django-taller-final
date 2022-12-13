from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    data = {"nombre" : "Pedro", "apellido":"Gaete"}
    return render(request, 'templatesApp/miplantilla.html', data)

def infousuario(request):
    data = {
            "id" : "123",
            "nombre" : "Pedro Gaete",
            "email" : "pedro@pedro.cl"
           }
    return render(request, 'templatesApp/userinfotemplate.html', data)

def index(request):
    return render(request, 'templatesApp/index.html')