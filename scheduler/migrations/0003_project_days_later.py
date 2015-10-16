# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20151016_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='days_later',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
