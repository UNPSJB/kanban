from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TableroListView.as_view(), name='tableros'),
    url(r'^tablero/$', views.add_tablero, name='add_tablero'),
    url(r'^tablero/(?P<tablero_id>[0-9]+)/$', views.edit_tablero, name='edit_tablero'),
    url(r'^tablero/(?P<tablero_id>[0-9]+)/delete/$', views.delete_tablero, name='delete_tablero'),
    url(r'^(?P<tablero_id>[0-9]+)/$', views.get_tablero, name='tablero'),
    url(r'^(?P<tablero_id>[0-9]+)/tarjeta/$', views.add_tarjeta, name='add_tarjeta'),
    url(r'^(?P<tablero_id>[0-9]+)/tarjeta/(?P<tarjeta_id>[0-9]+)/$', views.edit_tarjeta, name='edit_tarjeta'),
    url(r'^tarjeta/(?P<tarjeta_id>[0-9]+)/delete/$', views.delete_tarjeta, name='delete_tarjeta'),
    url(r'^tarjeta/(?P<tarjeta_id>[0-9]+)/modal/$', views.modal_tarjeta, name='modal_tarjeta'),
]
