
Manual
https://docs.djangoproject.com/en/1.8/

Proyecto

Organizador
-----------
django-admin startproject organizador

Kanban app
----------
python manage.py startapp kanban

Modelo Base
-----------

Tablero
Columna
Tarjeta

Conectar kanban
---------------
settings.py

Crear la migracion y migrar
---------------------------
python manage.py makemigrations kanban
python manage.py migrate

Completar modelo
----------------
Poner Atributos y armar las relaciones segun teoria de base de datos.

Jugar con la api
----------------
python manage.py shell

Algo de vida al modelo
----------------------
Ahora saben su nombre y hacer algo

Ahora si mas api y tunear algunas cosas
---------------------------------------

Hablar de queryset
------------------
Mostrar como se arman las queries

Activar la admin
----------------
Cuac!! ya viene activada por defecto :D (soy viejo)
python manage.py createsuperuser

Ponerle admin a kanban
----------------------
Agregar los modelos a la admin para ver el efecto en la admin


