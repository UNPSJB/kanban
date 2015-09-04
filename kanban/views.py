from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import models
from . import forms


# --------------- Tableros ---------------
class TableroListView(ListView):
    model = models.Tablero

    def get(self, request, *args, **kwargs):
        messages.info(request, "Hola %s" % request.user.username)
        return super().get(request, *args, **kwargs)

def get_tablero(request, tablero_id):
    tablero = models.Tablero.objects.get(id=tablero_id)
    return render(request, 'kanban/tablero.html', {'tablero': tablero})

@login_required
def tablero(request, tablero_id=None):
    tablero = tablero_id and get_object_or_404(models.Tablero, id=tablero_id) or None
    if request.method == 'POST':
        form = forms.TableroForm(request.POST, instance=tablero)
        if form.is_valid():
            tablero = form.save()
            messages.success(request, "Tablero %s creado" % tablero.titulo)
            return redirect('tablero', tablero.id)
    elif request.method == 'GET':
        form = forms.TableroForm(instance=tablero)
    return render(request, "kanban/forms/tablero.html", {
        "tablero": tablero,
        "form": form
    })

add_tablero = tablero
edit_tablero = tablero

@login_required
def delete_tablero(request, tablero_id):
    tablero = get_object_or_404(models.Tarjeta, id=tablero_id)
    tablero.delete()
    return redirect('tableros')

# --------------- Columnas ---------------
@login_required
def columna(request, tablero_id=None, columna_id=None):
    columna = columna_id and get_object_or_404(models.Columna, id=columna_id) or None
    tablero = tablero_id and get_object_or_404(models.Tablero, id=tablero_id) or None
    if request.method == 'POST':
        form = forms.ColumnaForm(request.POST, instance=columna)
        if form.is_valid():
            columna = form.save(commit=False)
            columna.tablero = tablero or columna.tablero
            columna.save()
            messages.success(request, "Columna %s creada" % columna.titulo)
            return redirect('tablero', columna.tablero.id)
    elif request.method == 'GET':
        form = forms.ColumnaForm(instance=columna)
    return render(request, "kanban/forms/columna.html", {
        "columna": columna,
        "form": form
    })

add_columna = columna
edit_columna = columna

@login_required
def delete_columna(request, columna_id):
    columna = get_object_or_404(models.Columna, id=columna_id)
    columna.delete()
    messages.success(request, "Columna %s borrada" % columna.titulo)
    return redirect('tablero', columna.tablero.id)

# --------------- Tarjetas ---------------
@login_required
def tarjeta(request, columna_id=None, tarjeta_id=None):
    tarjeta = tarjeta_id and get_object_or_404(models.Tarjeta, id=tarjeta_id) or None
    columna = columna_id and get_object_or_404(models.Columna, id=columna_id) or None
    if request.method == 'POST':
        form = forms.TarjetaForm(request.POST, instance=tarjeta)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.columna = columna or tarjeta.columna
            tarjeta.autor = request.user
            tarjeta.save()
            messages.success(request, "Tarjeta %s creada" % tarjeta.titulo)
            return redirect('tablero', tarjeta.columna.tablero.id)
    elif request.method == 'GET':
        form = forms.TarjetaForm(instance=tarjeta)
    return render(request, "kanban/forms/tarjeta.html", {
        "tarjeta": tarjeta,
        "form": form
    })

add_tarjeta = tarjeta
edit_tarjeta = tarjeta

@login_required
def delete_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(models.Tarjeta, id=tarjeta_id)
    tarjeta.delete()
    messages.success(request, "Tarjeta %s borrada" % tarjeta.titulo)
    return redirect('tablero', tarjeta.columna.tablero.id)

@login_required
def modal_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(models.Tarjeta, id=tarjeta_id)
    return render(request, "kanban/modal.html", {
        "tarjeta": tarjeta
    })
