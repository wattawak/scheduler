# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('design_approval', models.DateTimeField(default=django.utils.timezone.now)),
                ('programming_complete', models.DateTimeField(default=django.utils.timezone.now)),
                ('qa_complete', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
