# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-10 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Papellido', models.CharField(max_length=20)),
                ('Sapellido', models.CharField(max_length=20)),
                ('Nombres', models.CharField(max_length=20)),
                ('DNI', models.CharField(max_length=10)),
                ('Fechanacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Creditos', models.PositiveSmallIntegerField()),
                ('Estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaMatricula', models.DateTimeField(auto_now_add=True)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.Alumno')),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.Curso')),
            ],
        ),
    ]
