# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAcademica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(blank=True, max_length=50, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField()),
                ('fecha_crea', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
