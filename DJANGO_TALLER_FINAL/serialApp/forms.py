from django import forms
from .models import Institucion, Participante
from django.forms import TextInput, Textarea, NumberInput, Select

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        labels = {
            "nombre": "Nombre institución"
        }
        widgets = {
            "nombre": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Institución',
                    'style': 'max-width: 300px;'
                }
            )
        }
        fields = '__all__'

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        widgets = {
            "nombre": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Juan',
                    'style': 'max-width: 300px;'
                }
            ),
            "apellido": TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Perez',
                    'style': 'max-width: 300px;'
                }
            ),
            "telefono": NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '12345678',
                    'style': 'max-width: 300px;'
                }
            ),
            "institucion": Select(
                attrs={
                    'class': 'form-select',
                    'style': 'max-width: 300px;'
                }
            ),
            "estado": Select(
                attrs={
                    'class': 'form-select',
                    'style': 'max-width: 300px;'
                }
            ),
            "observacion": Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe...',
                    'style': 'max-width: 300px;',
                    'rows': 3
                }
            )
        }
        fields = '__all__'