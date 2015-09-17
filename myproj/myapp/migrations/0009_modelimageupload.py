# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20150612_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelImageUpload',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to='userimage')),
                ('name', models.ForeignKey(null=True, to='myapp.Instructor')),
            ],
        ),
    ]
