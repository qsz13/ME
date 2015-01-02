# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0008_auto_20150102_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 2, 10, 7, 22, 80607, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.ImageField(default=b'upload/adf.jpg', upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
