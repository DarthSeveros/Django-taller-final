from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    fono = models.CharField(max_length=20)

class proyecto(models.Model):
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    prioridad = models.IntegerField()