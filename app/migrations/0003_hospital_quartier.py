# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_hospital_quartier'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='quartier',
            field=models.CharField(default=datetime.datetime(2015, 4, 11, 0, 41, 49, 75736, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
    ]
