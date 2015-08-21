# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='columna',
            name='titulo',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablero',
            name='titulo',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='descripcion',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='titulo',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
