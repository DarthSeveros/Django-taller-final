from django import forms
from .models import Institucion, Participante

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'