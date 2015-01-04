# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='parent_account',
            field=models.ForeignKey(related_name='child_account', default=None, blank=True, to='account.Profile', null=True),
            preserve_default=True,
        ),
    ]
