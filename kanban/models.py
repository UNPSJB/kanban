from django.db import models

# Create your models here.

class Tablero(models.Model):
    titulo = models.CharField(max_length=200)
    
class Columna(models.Model):
    titulo = models.CharField(max_length=200)
    tablero = models.ForeignKey(Tablero)

class Tarjeta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    columna = models.ForeignKey(Columna)