# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('texto', models.TextField(verbose_name='Texto de feedback')),
                ('endereco_origem', models.TextField(verbose_name='Endereço de origem')),
                ('endereco_destino', models.TextField(verbose_name='Endereço de destino')),
                ('ponto_origem', django.contrib.gis.db.models.fields.PointField(verbose_name='Coordenada de origem', srid=4326)),
                ('ponto_destino', django.contrib.gis.db.models.fields.PointField(verbose_name='Coordenada de destino', srid=4326)),
                ('rota_tracada', django.contrib.gis.db.models.fields.LineStringField(verbose_name='Rota traçada pelo aplicativo', srid=4326)),
            ],
        ),
    ]
