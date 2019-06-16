# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-16 20:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_tipo', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('nota', models.FloatField(default=0)),
                ('codigo', models.CharField(max_length=100)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('numero_alumnos', models.IntegerField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Area')),
            ],
        ),
        migrations.CreateModel(
            name='ListaAsistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('promedio', models.FloatField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Area')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroDia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('listaAsistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.ListaAsistencia')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroSeminario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('listaAsistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.ListaAsistencia')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroTarde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('listaAsistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.ListaAsistencia')),
            ],
        ),
        migrations.AddField(
            model_name='examen',
            name='ranking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Ranking'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Grupo'),
        ),
    ]
