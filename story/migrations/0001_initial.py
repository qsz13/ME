# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 31, 6, 26, 47, 772344, tzinfo=utc))),
                ('content', models.TextField()),
                ('mood', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('story_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='story.Story')),
                ('wishes', models.TextField()),
            ],
            options={
            },
            bases=('story.story',),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('story_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='story.Story')),
                ('together_with', models.TextField()),
                ('place', models.TextField()),
            ],
            options={
            },
            bases=('story.story',),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('story_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='story.Story')),
                ('image', models.ImageField(upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=('story.story',),
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('story_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='story.Story')),
                ('together_with', models.TextField()),
                ('place', models.TextField()),
            ],
            options={
            },
            bases=('story.story',),
        ),
        migrations.CreateModel(
            name='VideoSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
