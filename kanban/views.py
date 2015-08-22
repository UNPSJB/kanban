from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Tablero, Tarjeta

def tableros(request):
    tableros = Tablero.objects.all()
    return render(request, 'kanban/tableros.html', {'tableros': tableros})

def tablero(request, tablero_id):
    tablero = Tablero.objects.get(id=tablero_id)
    return render(request, 'kanban/tablero.html', {'tablero': tablero})

def editar_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    if request.method == 'POST':
        metodo = 'POST'
    elif request.method == 'GET':
        metodo = 'GET'
    return render(request, "kanban/tarjeta.html", {
        "tarjeta": tarjeta,
        "metodo": metodo
    })

