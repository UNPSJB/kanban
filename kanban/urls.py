from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tableros, name='index'),
    url(r'^(?P<tablero_id>[0-9]+)/$', views.tablero, name='tablero'),
    url(r'^tarjeta/$', views.tarjeta, name='tarjeta'),
    url(r'^tarjeta/(?P<tarjeta_id>[0-9]+)/$', views.tarjeta, name='tarjeta'),
]
