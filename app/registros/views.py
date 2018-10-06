from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from .forms import *
from app.usuario.models import *
from app.usuario.forms import *

def RegExpediente(request):
	if request.method == 'POST':
		form = RegExpedienteForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/dashboard')
	else:
		form = RegExpedienteForm()
	return render(request, 'registros/expediente.html', {'expedientes': form})

def EditarExpediente(request, pk):
	expediente = get_object_or_404(Expediente, pk=pk)
	if request.method == "POST":
		form = RegExpedienteForm(request.POST, instance=expediente)
		if form.is_valid():
			expediente = form.save(commit=False)
			expediente.save()
			return redirect('/consulta/expediente/')
		else:
			return render(request, "modificacion/expediente.html", {"editar_expediente":form, "ver_expediente":expediente})	
	else:
		form = RegExpedienteForm(instance=expediente)
	return render(request, "modificacion/expediente.html", {"editar_expediente":form, "ver_expediente":expediente})		

def RegRubro(request):
	if request.method == 'POST':
		form = RegRubroForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/dashboard')
	else:
		form = RegRubroForm()
	return render(request, 'registros/rubro.html', {'rubros': form})

def EditarRubro(request, pk):
	rubro = get_object_or_404(Rubro, pk=pk)
	if request.method == "POST":
		form = RegRubroForm(request.POST, instance=rubro)
		if form.is_valid():
			rubro = form.save(commit=False)
			rubro.save()
			return redirect('/consulta/rubro/')
		else:
			return render(request, "modificacion/rubro.html", {"editar_rubro":form, "ver_rubro":rubro})	
	else:
		form = RegRubroForm(instance=rubro)
	return render(request, "modificacion/rubro.html", {"editar_rubro":form, "ver_rubro":rubro})

def AsignarTrabajador(request, pk):
	usuario = get_object_or_404(Perfil, pk=pk)
	if request.method == "POST":
		form = EditarPerfilForm(request.POST, instance=usuario)
		if form.is_valid():
			usuario = form.save(commit=False)
			usuario.save()
			return redirect('consulta/asigtrabajador/')
	else:
		form = EditarPerfilForm(instance=usuario)
	return render(request, "registros/asignartrabajador.html", {"asignar_trabajador":form, "ver_trabajador":usuario})