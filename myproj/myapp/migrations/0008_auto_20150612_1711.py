# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('myapp', '0007_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('webpage', models.URLField(default='')),
                ('office', models.CharField(default='EH 120', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('student_id', models.IntegerField()),
                ('level', models.IntegerField(default=1, choices=[(1, 'Undergrad'), (2, 'Masters'), (3, 'PhD')])),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(null=True, to='myapp.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='myapp.Student'),
        ),
    ]
