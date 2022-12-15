from django.contrib import admin
from .models import Institucion

# Register your models here.

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

admin.site.register(Institucion, InstitucionAdmin)
