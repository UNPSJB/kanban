from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Tablero

def index(request):
    tableros = Tablero.objects.all()
    template = loader.get_template('kanban/index.html')
    context = RequestContext(request, {
        'tableros': tableros,
    })
    return HttpResponse(template.render(context))

