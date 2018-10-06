from django.contrib import admin
from .models import *

class AdminExpediente(admin.ModelAdmin):
	list_display = [
		"id",
		"solicitante",
		"rif",
		"nomb_organizacion",
		"imagen_cedula",
		"imagen_rif",
		"imagen_inti",
		"imagen_plano",
		"imagen_ocupacion",
		"imagen_residencia",
		"municipio",
		"parroquia1",
		"parroquia2",
		"parroquia3",
		"parroquia4",
		"parroquia5",
		"parroquia6",
		"parroquia7",
		"parroquia8",
		"parroquia9",
		"parroquia10",
		"parroquia11",
		"parroquia12",
		"parroquia13",
		"parroquia14",
		"sector"
	]

admin.site.register(Expediente, AdminExpediente)

class AdminRubro(admin.ModelAdmin):
	list_display = [
		"codigo",
		"nombre"
	]

admin.site.register(Rubro, AdminRubro)