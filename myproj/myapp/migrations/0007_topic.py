# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20150528_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('subject', models.CharField(max_length=100, unique=True)),
                ('intro_course', models.BooleanField(default=True)),
                ('time', models.IntegerField(default=0, choices=[(0, 'No preference'), (1, 'Morning'), (2, 'Afternoon'), (3, 'Evening')])),
                ('num_responses', models.IntegerField(default=0)),
                ('avg_age', models.IntegerField(default=20)),
            ],
        ),
    ]
