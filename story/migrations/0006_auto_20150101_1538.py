# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_auto_20141231_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growth',
            name='image',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 7, 38, 1, 565176, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
