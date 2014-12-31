# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20141231_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 31, 6, 38, 22, 546642, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
