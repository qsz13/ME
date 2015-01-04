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
        migrations.RemoveField(
            model_name='travel',
            name='together_with',
        ),
        migrations.AddField(
            model_name='travel',
            name='image',
            field=models.ImageField(default=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 2, 9, 50, 26, 245304, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
