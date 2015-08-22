from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Tablero, Tarjeta
from .forms import TarjetaForm
from django.views.generic import ListView

class TableroListView(ListView):
    model = Tablero

def tablero(request, tablero_id):
    tablero = Tablero.objects.get(id=tablero_id)
    return render(request, 'kanban/tablero.html', {'tablero': tablero})

def tarjeta(request, tarjeta_id=None):
    tarjeta = tarjeta_id and get_object_or_404(Tarjeta, id=tarjeta_id) or None
    if request.method == 'POST':
        form = TarjetaForm(request.POST, instance=tarjeta)
        if form.is_valid():
            tarjeta = form.save()
            return redirect('tablero', tarjeta.columna.tablero.id)
    elif request.method == 'GET':
        form = TarjetaForm(instance=tarjeta)
    return render(request, "kanban/tarjeta.html", {
        "tarjeta": tarjeta,
        "form": form
    })

add_tarjeta = tarjeta
edit_tarjeta = tarjeta
def delete_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    tarjeta.delete()
    return redirect('tablero', tarjeta.columna.tablero.id)

def modal_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    return render(request, "kanban/modal.html", {
        "tarjeta": tarjeta
    })


