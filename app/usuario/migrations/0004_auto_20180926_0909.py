# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20180926_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='direccion',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]