# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_project_days_later'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='days_later',
            field=models.IntegerField(default=0),
        ),
    ]
