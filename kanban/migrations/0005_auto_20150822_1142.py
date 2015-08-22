# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanban', '0004_auto_20150822_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('archivo', models.FileField(upload_to='recursos')),
            ],
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 22, 11, 42, 59, 913205, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='usuarios',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='descripcion_markup_type',
            field=models.CharField(choices=[('', '--'), ('markdown', 'markdown')], default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='recurso',
            name='tarjeta',
            field=models.ForeignKey(to='kanban.Tarjeta'),
        ),
    ]
