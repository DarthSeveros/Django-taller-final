from django.db import models

# Create your models here.

ESTADO_CHOICES = (
    ('', 'Seleccione...'),
    ('RESERVADO', 'Reservado'),
    ('COMPLETADO', 'Completado'),
    ('ANULADA', 'Anulada'),
    ('NO ASISTEN', 'No asisten'),
)

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True, 
                    error_messages={"unique": "El nombre de la institución ya existe."})

    def __str__(self):
        return self.nombre

class Participante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    fecha_inscripcion = models.DateTimeField(auto_now_add=True, blank=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    observacion = models.CharField(max_length=100, blank=True)


