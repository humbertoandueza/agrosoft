# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20180920_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]