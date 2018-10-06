from django.contrib import admin
from .models import *

class AdminPerfil(admin.ModelAdmin):
	list_display = [
		"id",
		"user",
		"pri_nombre",
		"seg_nombre",
		"pri_apellido",
		"seg_apellido",
		"genero",
		"telefono",
		"direccion",
		"cargo",
	]

admin.site.register(Perfil, AdminPerfil)

