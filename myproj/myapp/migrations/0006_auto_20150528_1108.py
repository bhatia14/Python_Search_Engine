# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20150528_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='bithdate',
            new_name='birthdate',
        ),
        migrations.AddField(
            model_name='author',
            name='lastname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
