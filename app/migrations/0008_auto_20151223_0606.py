# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151222_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydoctor',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mydoctor',
            name='specialite',
            field=models.CharField(max_length=255),
        ),
    ]
