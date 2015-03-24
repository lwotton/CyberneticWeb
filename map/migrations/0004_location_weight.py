# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20150320_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='weight',
            field=models.DecimalField(default=1, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
    ]
