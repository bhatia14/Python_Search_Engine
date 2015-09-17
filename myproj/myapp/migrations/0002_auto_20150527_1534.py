# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('numpages', models.IntegerField(blank=True, null=True)),
                ('is_stock', models.BooleanField(verbose_name=True)),
                ('pubyear', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('textbook', models.ForeignKey(to='myapp.Book')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='city',
            field=models.CharField(default='Windsor', max_length=20),
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.CharField(default='Canada', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='myapp.Author'),
        ),
    ]
