# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-29 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0004_auto_20180926_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rif', models.IntegerField(blank=True, null=True, unique=True)),
                ('municipio', models.CharField(choices=[('Araure', 'Araure'), ('Esteller', 'Esteller'), ('Guanare', 'Guanare'), ('Guanarito', 'Guanarito'), ('Ospino', 'Ospino'), ('Paez', 'Paez'), ('Sucre', 'Sucre'), ('Turen', 'Turen'), ('Jose Vicente de Unda', 'Jose Vicente de Unda'), ('Agua Blanca', 'Agua Blanca'), ('Papelon', 'Papelon'), ('San Genaro de Boconoito', 'San Genaro de Boconoito'), ('San Rafael de Onoto', 'San Rafael de Onoto'), ('Santa Rosalia', 'Santa Rosalia')], max_length=100)),
                ('parroquia1', models.CharField(blank=True, choices=[('Araure', 'Araure'), ('Rio Acarigua', 'Rio Acarigua')], max_length=100, null=True)),
                ('parroquia2', models.CharField(blank=True, choices=[('Piritu', 'Piritu'), ('Uveral', 'Uveral')], max_length=100, null=True)),
                ('parroquia3', models.CharField(blank=True, choices=[('Córdoba', 'Córdoba'), ('Guanare', 'Guanare'), ('San José de la Montaña', 'San José de la Montaña'), ('San Juan de Guanaguanare', 'San Juan de Guanaguanare'), ('Virgen de la Coromoto', 'Virgen de la Coromoto')], max_length=100, null=True)),
                ('parroquia4', models.CharField(blank=True, choices=[('Guanarito', 'Guanarito'), ('Trinidad de la Capilla', 'Trinidad de la Capilla'), ('Divina Pastora', 'Divina Pastora')], max_length=100, null=True)),
                ('parroquia5', models.CharField(blank=True, choices=[('Aparicion', 'Aparicion'), ('La Estacion', 'La Estacion'), ('Ospino', 'Ospino')], max_length=100, null=True)),
                ('parroquia6', models.CharField(blank=True, choices=[('Acarigua', 'Acarigua'), ('Payara', 'Payara'), ('Pimpinela', 'Pimpinela'), ('Ramon Peraza', 'Ramon Peraza')], max_length=100, null=True)),
                ('parroquia7', models.CharField(blank=True, choices=[('Biscucuy', 'Biscucuy'), ('Concepción', 'Concepción'), ('San José de Saguaz', 'San José de Saguaz'), ('San Rafael de Palo Alzado', 'San Rafael de Palo Alzado'), ('Uvencio Antonio Velásquez', 'Uvencio Antonio Velásquez'), ('Villa Rosa', 'Villa Rosa')], max_length=100, null=True)),
                ('parroquia8', models.CharField(blank=True, choices=[('Villa Bruzual', 'Villa Bruzual'), ('Canelones', 'Canelones'), ('Santa Cruz', 'Santa Cruz'), ('San Isidro Labrador', 'San Isidro Labrador')], max_length=100, null=True)),
                ('parroquia9', models.CharField(blank=True, choices=[('Peña Blanca', 'Peña Blanca')], max_length=100, null=True)),
                ('parroquia10', models.CharField(blank=True, choices=[('Agua Blanca', 'Agua Blanca')], max_length=100, null=True)),
                ('parroquia11', models.CharField(blank=True, choices=[('Caño Delgaito', 'Caño Delgaito'), ('Papelon', 'Papelon')], max_length=100, null=True)),
                ('parroquia12', models.CharField(blank=True, choices=[('Antolín Tovar Anquino', 'Antolín Tovar Anquino'), ('Boconoíto', 'Boconoíto')], max_length=100, null=True)),
                ('parroquia13', models.CharField(blank=True, choices=[('Santa Fé', 'Santa Fé'), ('San Rafael de Onoto', 'San Rafael de Onoto'), ('Thermo Morales', 'Thermo Morales')], max_length=100, null=True)),
                ('parroquia14', models.CharField(blank=True, choices=[('Florida', 'Florida'), ('El Playón', 'El Playón')], max_length=100, null=True)),
                ('sector', models.CharField(max_length=60)),
                ('nomb_organizacion', models.CharField(blank=True, max_length=150, null=True)),
                ('imagen_cedula', models.ImageField(upload_to='Imagen_Expedientes')),
                ('imagen_rif', models.ImageField(upload_to='Imagen_Expedientes')),
                ('imagen_inti', models.ImageField(upload_to='Imagen_Expedientes')),
                ('imagen_plano', models.ImageField(upload_to='Imagen_Expedientes')),
                ('imagen_ocupacion', models.ImageField(upload_to='Imagen_Expedientes')),
                ('imagen_residencia', models.ImageField(upload_to='Imagen_Expedientes')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
