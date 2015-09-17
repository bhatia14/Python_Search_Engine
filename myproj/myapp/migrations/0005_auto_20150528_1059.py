# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20150527_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bithdate',
            field=models.DateField(),
        ),
    ]
