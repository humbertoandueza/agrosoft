from django import forms
from .models import *

class RegExpedienteForm(forms.ModelForm):
	class Meta:
		model = Expediente
		fields = [
			"rif",
			"nomb_organizacion",
			"imagen_cedula",
			"imagen_rif",
			"imagen_inti",
			"imagen_plano",
			"imagen_ocupacion",
			"imagen_residencia",
			"solicitante",
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

class RegRubroForm(forms.ModelForm):
	class Meta:
		model = Rubro
		fields = [
			"codigo",
			"nombre"
		]	