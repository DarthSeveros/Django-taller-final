from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    carrera = models.CharField(max_length=50)
    puntos = models.DecimalField(max_digits=5, decimal_places=2)


