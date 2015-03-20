# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20150320_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(max_digits=10, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(max_digits=10, decimal_places=8),
            preserve_default=True,
        ),
    ]
