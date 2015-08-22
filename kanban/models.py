from django.db import models
from markupfield.fields import MarkupField
from django.contrib.auth import models as authmodels

# Create your models here.

class Tablero(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

    def nueva_columna(self, titulo):
        c = Columna(titulo=titulo, tablero=self)
        c.save()
        return c

class Columna(models.Model):
    titulo = models.CharField(max_length=200)
    tablero = models.ForeignKey(Tablero, related_name='columnas')

    def __str__(self):
        return "%s - %s" % (self.titulo, self.tablero)

    def nueva_tarjeta(self, titulo, descripcion):
        t = Tarjeta(titulo=titulo, descripcion=descripcion, columna=self)
        t.save()
        return t

class Postit(models.Model):
    titulo = models.CharField(max_length=200)
    columna = models.ForeignKey(Columna, related_name='tarjetas')
    autor = models.ForeignKey(authmodels.User)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Tarjeta(Postit):
    descripcion = MarkupField()
    participantes = models.ManyToManyField(authmodels.User)

    def __str__(self):
        return self.titulo

class Recurso(models.Model):
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='recursos')
    tarjeta = models.ForeignKey(Tarjeta)
