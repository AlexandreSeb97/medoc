# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_hospital_quartier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='phone_number',
            new_name='phone_number1',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='phone_number',
            new_name='phone_number1',
        ),
        migrations.AddField(
            model_name='hospital',
            name='phone_number2',
            field=models.CharField(default=datetime.datetime(2015, 6, 19, 19, 51, 18, 165334, tzinfo=utc), max_length=16),
            preserve_default=False,
        ),
    ]
