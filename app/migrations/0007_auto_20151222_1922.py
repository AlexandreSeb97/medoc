# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_mydoctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydoctor',
            name='country',
            field=models.CharField(max_length=255, default='None'),
        ),
        migrations.AddField(
            model_name='mydoctor',
            name='specialite',
            field=models.CharField(max_length=255, default='None'),
        ),
    ]
