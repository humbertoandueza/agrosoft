from django.db import models 
from app.usuario.models import Perfil
from django.contrib.auth.models import User

class Expediente(models.Model):
	municipios = (
		("Araure","Araure"),
		("Esteller","Esteller"),
		("Guanare", "Guanare"),
		("Guanarito","Guanarito"),
		("Ospino","Ospino"),
		("Paez","Paez"),
		("Sucre","Sucre"),
		("Turen","Turen"),
		("Jose Vicente de Unda","Jose Vicente de Unda"),
		("Agua Blanca","Agua Blanca"),
		("Papelon","Papelon"),
		("San Genaro de Boconoito","San Genaro de Boconoito"),
		("San Rafael de Onoto","San Rafael de Onoto"),
		("Santa Rosalia","Santa Rosalia"),	
	)
	parroquias1 = (
		("Araure","Araure"),
		("Rio Acarigua","Rio Acarigua"),
	)
	parroquias2 =(
		("Piritu","Piritu"),
		("Uveral","Uveral"),
	)
	parroquias3 =(
		("Córdoba", "Córdoba"),
		("Guanare", "Guanare"),
		("San José de la Montaña", "San José de la Montaña"),
		("San Juan de Guanaguanare", "San Juan de Guanaguanare"),
		("Virgen de la Coromoto", "Virgen de la Coromoto"),
	)
	parroquias4 =(
		("Guanarito","Guanarito"),
		("Trinidad de la Capilla","Trinidad de la Capilla"),
		("Divina Pastora","Divina Pastora"),
	)
	parroquias5 =(
		("Aparicion","Aparicion"),
		("La Estacion","La Estacion"),
		("Ospino","Ospino"),
	)
	parroquias6 =(
		("Acarigua","Acarigua"),
		("Payara","Payara"),
		("Pimpinela","Pimpinela"),
		("Ramon Peraza","Ramon Peraza"),
	)
	parroquias7 =(
		("Biscucuy","Biscucuy"),
		("Concepción","Concepción"),
		("San José de Saguaz","San José de Saguaz"),
		("San Rafael de Palo Alzado","San Rafael de Palo Alzado"),
		("Uvencio Antonio Velásquez","Uvencio Antonio Velásquez"),
		("Villa Rosa","Villa Rosa"),
	)
	parroquias8 =(
		("Villa Bruzual","Villa Bruzual"),
		("Canelones","Canelones"),
		("Santa Cruz","Santa Cruz"),
		("San Isidro Labrador","San Isidro Labrador"),
	)
	parroquias9 =(
		("Peña Blanca","Peña Blanca"),
	)
	parroquias10 =(
		("Agua Blanca","Agua Blanca"),
	)
	parroquias11 =(
		("Caño Delgaito","Caño Delgaito"),
		("Papelon","Papelon"),
	)
	parroquias12 =(
		("Antolín Tovar Anquino","Antolín Tovar Anquino"),
		("Boconoíto","Boconoíto"),
	)
	parroquias13 =(
		("Santa Fé","Santa Fé"),
		("San Rafael de Onoto","San Rafael de Onoto"),
		("Thermo Morales","Thermo Morales"),
	)
	parroquias14 =(
		("Florida","Florida"),
		("El Playón","El Playón"),
	)
	rif=models.CharField(max_length=10, unique=True, null=True, blank=True)
	municipio = models.CharField(max_length=100, choices=municipios)
	parroquia1 = models.CharField(max_length=100, choices=parroquias1, null=True, blank=True)
	parroquia2 = models.CharField(max_length=100, choices=parroquias2, null=True, blank=True)
	parroquia3 = models.CharField(max_length=100, choices=parroquias3, null=True, blank=True)
	parroquia4 = models.CharField(max_length=100, choices=parroquias4, null=True, blank=True)
	parroquia5 = models.CharField(max_length=100, choices=parroquias5, null=True, blank=True)
	parroquia6 = models.CharField(max_length=100, choices=parroquias6, null=True, blank=True)
	parroquia7 = models.CharField(max_length=100, choices=parroquias7, null=True, blank=True)
	parroquia8 = models.CharField(max_length=100, choices=parroquias8, null=True, blank=True)
	parroquia9 = models.CharField(max_length=100, choices=parroquias9, null=True, blank=True)
	parroquia10 = models.CharField(max_length=100, choices=parroquias10, null=True, blank=True)
	parroquia11 = models.CharField(max_length=100, choices=parroquias11, null=True, blank=True)
	parroquia12 = models.CharField(max_length=100, choices=parroquias12, null=True, blank=True)
	parroquia13 = models.CharField(max_length=100, choices=parroquias13, null=True, blank=True)
	parroquia14 = models.CharField(max_length=100, choices=parroquias14, null=True, blank=True)
	sector = models.CharField(max_length=60)
	solicitante = models.ForeignKey(Perfil)
	nomb_organizacion = models.CharField(max_length=150, null=True, blank=True)

	imagen_cedula = models.ImageField(upload_to='Imagen_Expedientes')
	imagen_rif = models.ImageField(upload_to='Imagen_Expedientes')
	imagen_inti = models.ImageField(upload_to='Imagen_Expedientes')
	imagen_plano = models.ImageField(upload_to='Imagen_Expedientes')
	imagen_ocupacion = models.ImageField(upload_to='Imagen_Expedientes')
	imagen_residencia = models.ImageField(upload_to='Imagen_Expedientes')
	def __str__(self):
		return '%s' %(self.solicitante)

class Rubro(models.Model):
	codigo = models.CharField(max_length=10)
	nombre = models.CharField(max_length=50)
	def __str__(self):
		return '%s - %s' %(self.codigo, self.nombre)
