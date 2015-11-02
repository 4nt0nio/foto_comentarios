# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cometario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cometario', models.TextField()),
                ('foto', models.ForeignKey(to='fotos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, default='Sin titulo')),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('fecha_pulic', models.DateField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('favorito', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(null=True, to='fotos.Categoria')),
            ],
        ),
    ]
