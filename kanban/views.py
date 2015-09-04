from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from . import models
from . import forms
from django.views.generic import ListView

class TableroListView(ListView):
    model = models.Tablero

def get_tablero(request, tablero_id):
    tablero = models.Tablero.objects.get(id=tablero_id)
    return render(request, 'kanban/tablero.html', {'tablero': tablero})

def columna(request, tablero_id, columna_id=None):
    columna = columna_id and get_object_or_404(models.Columna, id=columna_id) or None
    tablero = get_object_or_404(models.Tablero, id=tablero_id)
    if request.method == 'POST':
        form = forms.ColumnaForm(request.POST, instance=columna)
        if form.is_valid():
            columna = form.save(commit=False)
            columna.tablero = tablero
            columna.save()
            return redirect('tablero', columna.tablero.id)
    elif request.method == 'GET':
        form = forms.ColumnaForm(instance=columna)
    return render(request, "kanban/forms/columna.html", {
        "columna": columna,
        "form": form
    })

add_columna = columna
edit_columna = columna

def tarjeta(request, columna_id, tarjeta_id=None):
    tarjeta = tarjeta_id and get_object_or_404(models.Tarjeta, id=tarjeta_id) or None
    columna = get_object_or_404(models.Columna, id=columna_id)
    if request.method == 'POST':
        form = forms.TarjetaForm(request.POST, instance=tarjeta)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.columna = columna
            tarjeta.save()
            return redirect('tablero', tarjeta.columna.tablero.id)
    elif request.method == 'GET':
        form = forms.TarjetaForm(instance=tarjeta)
    return render(request, "kanban/forms/tarjeta.html", {
        "tarjeta": tarjeta,
        "form": form
    })

add_tarjeta = tarjeta
edit_tarjeta = tarjeta
def delete_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(models.Tarjeta, id=tarjeta_id)
    tarjeta.delete()
    return redirect('tablero', tarjeta.columna.tablero.id)

def modal_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    return render(request, "kanban/modal.html", {
        "tarjeta": tarjeta
    })

def tablero(request, tablero_id=None):
    tablero = tablero_id and get_object_or_404(models.Tablero, id=tablero_id) or None
    if request.method == 'POST':
        form = forms.TableroForm(request.POST, instance=tablero)
        if form.is_valid():
            tablero = form.save()
            return redirect('tablero', tablero.id)
    elif request.method == 'GET':
        form = forms.TableroForm(instance=tablero)
    return render(request, "kanban/forms/tablero.html", {
        "tablero": tablero,
        "form": form
    })

add_tablero = tablero
edit_tablero = tablero
def delete_tablero(request, tablero_id):
    tablero = get_object_or_404(models.Tarjeta, id=tablero_id)
    tablero.delete()
    return redirect('tableros')
