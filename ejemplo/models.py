from django.db import models
from django.shortcuts import render
import datetime 

class Familiar(models.Model):

    nombre= models.CharField(max_length=100)
    direccion= models.CharField(max_length=200)
    numero_pasaporte= models.IntegerField()
    #nacimiento= models.DateField(NO SÉ)
    
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}, {self.nacimiento}"
    