# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='rif',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
