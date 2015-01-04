# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_auto_20150102_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 2, 10, 0, 17, 691916, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
