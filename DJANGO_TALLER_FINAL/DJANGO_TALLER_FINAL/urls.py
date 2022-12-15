"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from serialApp import views as serialViews
from seminario import views as seminarioViews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', seminarioViews.inicio, name='inicio'),

    path('api_institucion/', serialViews.institucion_list, name='api_institucion'),
    path('api_institucion/<int:id>', serialViews.institucion_detalle, name='api_institucion_detalle'),

    path('api_participante/', serialViews.ListaParticipantes.as_view(), name='api_participante'),
    path('api_participante/<int:id>', serialViews.DetalleParticipante.as_view(), name='api_participante_detalle'),

    path('participantes/', seminarioViews.participantes, name='participantes'),

    path('instituciones/', seminarioViews.instituciones, name='instituciones'),
]
