# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-19 16:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroAsistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('registro_dia', models.BooleanField(default=False)),
                ('registro_tarde', models.BooleanField(default=False)),
                ('registro_seminario', models.BooleanField(default=False)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Estudiante')),
            ],
        ),
        migrations.RemoveField(
            model_name='listaasistencia',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='registrodia',
            name='listaAsistencia',
        ),
        migrations.RemoveField(
            model_name='registroseminario',
            name='listaAsistencia',
        ),
        migrations.RemoveField(
            model_name='registrotarde',
            name='listaAsistencia',
        ),
        migrations.DeleteModel(
            name='ListaAsistencia',
        ),
        migrations.DeleteModel(
            name='RegistroDia',
        ),
        migrations.DeleteModel(
            name='RegistroSeminario',
        ),
        migrations.DeleteModel(
            name='RegistroTarde',
        ),
    ]
