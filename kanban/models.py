from django.db import models

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
        return self.titulo

    def nueva_tarjeta(self, titulo, descripcion):
        t = Tarjeta(titulo=titulo, descripcion=descripcion, columna=self)
        t.save()
        return t

class Tarjeta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    columna = models.ForeignKey(Columna, related_name='tarjetas')
    
    def __str__(self):
        return self.titulo