# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(default=b'/media/upload/1', upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 31, 6, 29, 3, 858838, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
