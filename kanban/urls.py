from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tableros, name='index'),
    url(r'^(?P<tablero_id>[0-9]+)/$', views.tablero, name='tablero'),
    url(r'^tarjeta/$', views.add_tarjeta, name='add_tarjeta'),
    url(r'^tarjeta/(?P<tarjeta_id>[0-9]+)/$', views.edit_tarjeta, name='edit_tarjeta'),
    url(r'^tarjeta/(?P<tarjeta_id>[0-9]+)/delete/$', views.delete_tarjeta, name='delete_tarjeta'),
]
