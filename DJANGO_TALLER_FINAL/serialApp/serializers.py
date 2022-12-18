from rest_framework import serializers
from serialApp.models import Participante, Institucion

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'

class ListarParticipanteSerializer(serializers.ModelSerializer):
    fecha_inscripcion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Participante
        fields = '__all__'
        depth = 1

class InsertarParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'
        depth = 0