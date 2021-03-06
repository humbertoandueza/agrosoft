# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-05 14:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pri_nombre', models.CharField(max_length=40)),
                ('seg_nombre', models.CharField(blank=True, max_length=40, null=True)),
                ('pri_apellido', models.CharField(max_length=40)),
                ('seg_apellido', models.CharField(max_length=40)),
                ('cargo', models.CharField(blank=True, choices=[('Inspector Agrícola', 'Inspector Agrícola'), ('Secretaria(o)', 'Secretaria(o)'), ('Solicitante', 'Solicitante')], default='Solicitante', max_length=50, null=True)),
                ('genero', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
