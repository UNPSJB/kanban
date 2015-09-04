from django.contrib import admin

# Register your models here.

from .models import Tablero, Columna, Tarjeta, Postit, Recurso

admin.site.register(Tablero)
admin.site.register(Columna)
admin.site.register(Tarjeta)
admin.site.register(Postit)
admin.site.register(Recurso)