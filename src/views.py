from django.shortcuts import render
from django.contrib.auth.models import User
from app.usuario.models import *
from app.registros.models import *

def Inicio(request):
	return render(request, "index.html", {})

def Dashboard(request):
	solicitante = Perfil.objects.values('cargo').filter(cargo="Solicitante")
	expediente = Expediente.objects.all()
	return render(request, "dashboard.html", {"solicitantes":solicitante, "expedientes":expediente})