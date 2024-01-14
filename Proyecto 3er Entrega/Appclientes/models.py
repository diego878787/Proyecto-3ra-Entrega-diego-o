from django.db import models

# Create your models here.

class dpersonales(models.Model):
    nombre = models.CharField (max_length = 30)
    apellido = models.CharField (max_length = 30)
    dni = models.IntegerField ()
    sexo = models.CharField (max_length = 10)
    fnacimiento = models.DateField ()

class ddomicilio(models.Model):
    direccion = models.CharField (max_length = 40)
    localidad = models.CharField (max_length = 30)
    provincia = models.CharField (max_length = 20)
    codigopostal = models.IntegerField ()

class dcontacto(models.Model):
    telefonofijo = models.CharField (max_length = 20)
    telcelular = models.IntegerField ()
    celectronico = models.EmailField ()

class productos(models.Model):
    producto = models.CharField (max_length = 30)
    color = models.CharField (max_length = 20)
    cantidad = models.IntegerField ()