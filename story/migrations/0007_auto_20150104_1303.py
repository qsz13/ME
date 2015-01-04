# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_auto_20150101_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 4, 5, 3, 39, 336929, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
