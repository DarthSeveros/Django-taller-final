from django.db import models

# Create your models here.

class Empleado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)