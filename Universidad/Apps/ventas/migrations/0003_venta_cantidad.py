# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20180815_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
