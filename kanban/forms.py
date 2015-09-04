from django import forms
from . import models

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = models.Tarjeta
        fields = ['titulo', 'descripcion', 'descripcion_markup_type', 'participantes']

class TableroForm(forms.ModelForm):
    class Meta:
        model = models.Tablero
        fields = ['titulo']