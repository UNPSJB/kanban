from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Tablero

def index(request):
    tableros = Tablero.objects.all()
    return render(request, 'kanban/index.html', {'tableros': tableros})

