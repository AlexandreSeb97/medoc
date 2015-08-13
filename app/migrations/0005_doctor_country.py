# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150619_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='country',
            field=models.CharField(default=datetime.datetime(2015, 8, 13, 15, 42, 51, 139283, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
