from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedido(models.Model):
    nropedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()



# python manage.py check gestionPedido_APP

# python manage.py makemigrations

# python manage.py migrate   

#python manage.py shell  -> Abre Consola BD
#from gestionPedido_APP.models import Producto  -> Importa Tabla a utilizar

# INSERTAR DATOS
#pro=Producto(nombre='lapiz', categoria='libreria', precio=1000)
#pro1=Producto(nombre='martillo', categoria='ferreteria', precio=4500)
#pro2=Producto.objects.create(nombre='CocaCola', categoria='bebidas', precio=500) 

#MODIFICAR DATOS
#pro1.precio=4000
#pro1.save()

#BUSCAR PRODUCTO ID 3
#pro2=Producto.objects.get(id=3)

#BUSCA y ELIMINA ID 3
#pro2=Producto.objects.get(id=3)
#pro2.delete()
