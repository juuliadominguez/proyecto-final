from django.db import models
from django.shortcuts import render
from datetime import datetime

class Familiar(models.Model):

    nombre= models.CharField(max_length=100)
    direccion= models.CharField(max_length=200)
    numero_pasaporte= models.IntegerField()
    fecha_de_nacimiento= models.DateField()
    
    def __str__(self):
      return f"{self.id}, {self.nombre}, {self.direccion}, {self.numero_pasaporte}, {self.fecha_de_nacimiento}"


class Gatos(models.Model):

  nombre= models.CharField(max_length=100)
  edad= models.IntegerField()
  sexo= models.CharField(max_length=100)

  def __str__(self):
    return f"{self.id}, {self.nombre}, {self.edad}, {self.sexo}"


class Perros(models.Model):

  nombre= models.CharField(max_length=100)
  edad= models.IntegerField()
  sexo= models.CharField(max_length=100)

  def __str__(self):
    return f"{self.id}, {self.nombre}, {self.edad}, {self.sexo}"




    