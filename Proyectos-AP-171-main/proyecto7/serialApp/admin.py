from django.contrib import admin
from .models import Estudiante

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'puntos']

admin.site.register(Estudiante, EstudianteAdmin)