# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20141231_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Growth',
            fields=[
                ('story_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='story.Story')),
                ('wishes', models.TextField()),
                ('age', models.CharField(max_length=16)),
                ('weight', models.CharField(max_length=16)),
                ('height', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=('story.story',),
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='story_ptr',
        ),
        migrations.DeleteModel(
            name='Milestone',
        ),
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 31, 6, 38, 0, 54475, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
