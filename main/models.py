from abc import abstractclassmethod
from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.
class UserCustom (AbstractUser):
    categoria = models.CharField(max_length= 20)

class AreasMedicasabs (models.Model):
    area = models.CharField(max_length=50)
    jefe_area = models.CharField(max_length=250)

class Pasiente (models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    fecha_alta = models.DateField()
    diacnostico = models.TextField()
    peso = models.IntegerField()
    estatura_cm = models.IntegerField()


class Medico(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=50)
    pasientes = models.ManyToManyField(Pasiente)
    area = models.ManyToManyField(AreasMedicasabs)

class Recetas (models.Model):
    medico = models.OneToOneField(Medico,on_delete=models.DO_NOTHING)
    Pasiente = models.OneToOneField(Pasiente,on_delete=models.DO_NOTHING)
    descripcion = models.TextField()