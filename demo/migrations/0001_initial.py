# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('station_name', models.CharField(unique=True, max_length=256, verbose_name=b'Station Name')),
                ('alias', models.CharField(max_length=256, verbose_name=b'Station Alias')),
                ('city', models.CharField(max_length=256, verbose_name=b'Station City')),
                ('country', models.CharField(max_length=256, null=True, verbose_name=b'Station Country', blank=True)),
            ],
        ),
    ]
