
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

Views y url.py
--------------
El hola mundo mas simple de todos

Templates
---------
Entender el concepto y usar los shortcuts

Algo de color
-------------
Agregar bootstrap y hablar de statics
http://getbootstrap.com/

Ahora a navegar a un tablero
----------------------------
Armar url view y el link

Refactoring de template
-----------------------
Acomodar templates, extends

Url fea y url linda
-------------------
cambiar a {% url 'tablero' tablero.id %}

Mas sobre templates
-------------------
extends, los for contra los managers

Mas colorete
------------
Paneles para las columnas
Poner algunas columnas mas, todo doing doit

Tarjeta con forma de tarjeta
----------------------------
Poner mas color al tablero
Agregar mas tarjetas

Javascript del bueno, jqueryui
------------------------------
Incorporamos y despedazamos jqueryui segun como mas nos gusta

Jugar con herramientas en el navegador
--------------------------------------
firebug

Tablero con tarjetas moviles
----------------------------
Agregar los scripts para que las tarjetas se muevan

https://jqueryui.com/

Editar una tarjeta
------------------
Agregar icono para editar tarjeta, crear url y vista

Separar GET y POST
------------------
Crear template y seprar el GET del POST






