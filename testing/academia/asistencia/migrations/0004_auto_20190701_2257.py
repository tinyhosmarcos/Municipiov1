# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-02 03:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0003_auto_20190701_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroasistencia',
            name='fecha',
            field=models.DateField(default=datetime.date.today, unique_for_date=True),
        ),
    ]
