# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanban', '0005_auto_20150822_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('columna', models.ForeignKey(to='kanban.Columna', related_name='tarjetas')),
            ],
        ),
        migrations.RenameField(
            model_name='tarjeta',
            old_name='usuarios',
            new_name='participantes',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='columna',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='titulo',
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='postit_ptr',
            field=models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, default=0, to='kanban.Postit'),
            preserve_default=False,
        ),
    ]
