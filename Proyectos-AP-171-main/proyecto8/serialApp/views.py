from django.shortcuts import render
from .serialiazers import EstudianteSerializer
from .models import Estudiante
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class ListaEstudiantes(APIView):
    def get(self, request):
        estu = Estudiante.objects.all()
        serial = EstudianteSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = EstudianteSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleEstudiante(APIView):
    def get_object(self, pk):
        try:
            return Estudiante.objects.get(id=pk)
        except Estudiante.DoesNotExist:
            return Http404

    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = EstudianteSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = EstudianteSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)