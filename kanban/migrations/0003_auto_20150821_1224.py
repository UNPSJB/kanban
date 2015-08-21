# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_auto_20150821_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='columna',
            name='tablero',
            field=models.ForeignKey(default=0, to='kanban.Tablero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='columna',
            field=models.ForeignKey(default=0, to='kanban.Columna'),
            preserve_default=False,
        ),
    ]
