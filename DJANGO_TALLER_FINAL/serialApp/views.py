from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .models import Participante, Institucion
from .serializers import InstitucionSerializer, ListarParticipanteSerializer, InsertarParticipanteSerializer
from rest_framework.decorators import api_view

class ListaParticipantes(APIView):
    def get(self, request):
        participante = Participante.objects.all()
        serial = ListarParticipanteSerializer(participante, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InsertarParticipanteSerializer(data = request.data)
        print(serial)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleParticipante(APIView):
    def get_object(self, pk):
        try:
            return Participante.objects.get(id=pk)
        except Participante.DoesNotExist:
            return Http404

    def get(self, request, pk):
        participante = self.get_object(pk)
        serial = ListarParticipanteSerializer(participante)
        return Response(serial.data)

    def put(self, request, pk):
        participante = self.get_object(pk)
        serial = InsertarParticipanteSerializer(participante, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        participante = self.get_object(pk)
        participante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##############################################################################################

@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        institucion = Institucion.objects.all()
        serial = InstitucionSerializer(institucion, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    try:
        institucion = Institucion.objects.get(pk=id)
    except institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(institucion)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(institucion, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)