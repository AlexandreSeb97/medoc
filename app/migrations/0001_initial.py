# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=150)),
                ('specialite', models.CharField(max_length=50)),
                ('adresse', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=16)),
                ('anecdote', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(max_length=200)),
                ('quartier', models.CharField(max_length=75)),
                ('adresse', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=16)),
                ('specialite', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
