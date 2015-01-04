# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0009_auto_20150102_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('story_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='story.Story')),
                ('image', models.ImageField(default=b'/upload/adf.jpg', upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=('story.story',),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('story_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='story.Story')),
                ('image', models.ImageField(default=b'/upload/adf.jpg', upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=('story.story',),
        ),
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 2, 15, 56, 28, 872033, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.ImageField(default=b'/upload/adf.jpg', upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
