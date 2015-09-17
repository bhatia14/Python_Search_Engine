# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150527_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bithdate',
            field=models.CharField(max_length=20),
        ),
    ]
