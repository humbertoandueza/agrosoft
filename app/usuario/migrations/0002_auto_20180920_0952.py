# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-20 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='seg_apellido',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
