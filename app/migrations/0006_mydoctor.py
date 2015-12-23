# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_doctor_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDoctor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=255, unique=True)),
                ('owner_first_name', models.CharField(max_length=120)),
                ('owner_last_name', models.CharField(max_length=120)),
                ('is_member', models.BooleanField(verbose_name='Is Paid Member', default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
