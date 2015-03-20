# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('citizenID', models.CharField(max_length=200)),
                ('rec_date', models.DateTimeField(verbose_name=b'date recieved')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.IntegerField(max_length=200)),
                ('citizen', models.ForeignKey(to='map.Citizen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
