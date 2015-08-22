# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0003_auto_20150821_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='_descripcion_rendered',
            field=models.TextField(editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='descripcion_markup_type',
            field=models.CharField(max_length=30, choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain')], default=''),
        ),
        migrations.AlterField(
            model_name='columna',
            name='tablero',
            field=models.ForeignKey(to='kanban.Tablero', related_name='columnas'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='columna',
            field=models.ForeignKey(to='kanban.Columna', related_name='tarjetas'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='descripcion',
            field=markupfield.fields.MarkupField(rendered_field=True),
        ),
    ]
