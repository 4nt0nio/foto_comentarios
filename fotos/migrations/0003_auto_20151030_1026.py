# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0002_auto_20151030_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(upload_to='fotografias/'),
        ),
    ]
