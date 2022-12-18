from django import forms

ESTADO_CHOICES = (
    ('', 'Seleccione...'),
    ('RESERVADO', 'Reservado'),
    ('COMPLETADO', 'Completado'),
    ('ANULADA', 'Anulada'),
    ('NO ASISTEN', 'No asisten'),
)

class InstitucionForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Institución',
                    'style': 'max-width: 300px;'
                }))
                
class ParticipanteForm(forms.Form):
    def __init__(self, *args, choices=[], **kwargs, ):
        super(ParticipanteForm, self).__init__(*args, **kwargs)
        instituciones = list(map(lambda x: (str(x['id']),x['nombre']), choices))
        instituciones.insert(0,("", "Seleccione..."))
        self.fields['institucion'].choices = instituciones
    
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Juan',
                    'style': 'max-width: 300px;'
                }))
    apellido = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
                    'class': 'form-control',
                    'placeholder': 'Perez',
                    'style': 'max-width: 300px;'
                }
    ))
    telefono = forms.IntegerField(widget=forms.NumberInput(
        attrs={
                    'class': 'form-control',
                    'placeholder': '12345678',
                    'style': 'max-width: 300px;'
                }
    ))
    institucion = forms.ChoiceField(widget=forms.Select(
        attrs={
                    'class': 'form-select',
                    'style': 'max-width: 300px;'
                }
    ))
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(
        attrs={
                    'class': 'form-select',
                    'style': 'max-width: 300px;'
                }
    ))
    observacion = forms.CharField(max_length=100, required=False, widget=forms.Textarea(
        attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe...',
                    'style': 'max-width: 300px;',
                    'rows': 3
                }
    ))