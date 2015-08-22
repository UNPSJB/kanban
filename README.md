
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

Crear la migración y migrar
---------------------------
python manage.py makemigrations kanban
python manage.py migrate

Completar modelo
----------------
Poner Atributos y armar las relaciones según teoría de base de datos.

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
Incorporamos y despedazamos jqueryui según como mas nos gusta

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
Crear template y separar el GET del POST

Crear el formulario
-------------------
En forms.py
Mejorar el template
{% csrf_token %}

Como se ven los fk
------------------
Agregar el fk al formulario de tarjeta y mejorar la vista de la columna __str__
Mejorar el estilo del formulario hora de incluir apps de terceros
django-bootstrap3

Alta de tarjetas
----------------
Reusar la view para hacer el alta de tarjetas
mencionar algunos detalles o problemas que estamos teniendo por no tener bien las urls

Icono de eliminar tarea
-----------------------
Hora de refactorizar urls

Icono para ver el contenido de la tarjeta
-----------------------------------------

Algo de javascript
------------------
Ahora la tarjeta esta en una modal, uso de data en html
que tal algo de markdown?  django-markupfield filters






