# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20141231_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='growth',
            name='image',
            field=models.ImageField(default=b'/media/upload/1', upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 31, 6, 58, 42, 971229, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
