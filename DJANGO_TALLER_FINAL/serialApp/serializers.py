from sqlite3 import paramstyle
from rest_framework import serializers
from serialApp.models import Participante, Institucion

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'