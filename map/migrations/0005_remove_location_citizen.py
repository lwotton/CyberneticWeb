# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_location_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='citizen',
        ),
    ]
