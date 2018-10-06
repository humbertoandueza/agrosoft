from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from .forms import *
from .models import *

def RegUsuario(request):
	if request.method == 'POST':
		form = PerfilForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # cargar la instancia de perfil creada por la señal
			user.perfil.pri_nombre = form.cleaned_data.get('pri_nombre')
			user.perfil.seg_nombre = form.cleaned_data.get('seg_nombre')
			user.perfil.pri_apellido = form.cleaned_data.get('pri_apellido')
			user.perfil.seg_apellido = form.cleaned_data.get('seg_apellido')
			user.perfil.telefono = form.cleaned_data.get('telefono')
			user.perfil.direccion = form.cleaned_data.get('direccion')
			user.perfil.genero = form.cleaned_data.get('genero')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('Dashboard')
	else:
		form = PerfilForm()
	return render(request, 'usuario/registro.html', {'usuarios': form})

class Login(FormView):
	model = User
	form_class = AuthenticationForm
	template_name = "usuario/login.html"
 
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, { 'form': form, 'message':'' })

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Dashboard')
		else:
			mensaje= "El Usuario o la Contraseña son Incorrectos."
			return render(request, self.template_name, {'form':self.form_class ,'message':mensaje })

class LogoutView(FormView):
	def get(self, request):
		logout(request)
		return redirect('/')

def EditarClave(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			logout(request)
			return redirect('Inicio')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'usuario/clave/editarclave.html', {"form": form})

def EditarPerfil(request):
	content = {}
	profile = request.user.get_username()
	print(profile)
	if request.method == 'POST':
		form1 = EditarPerfilForm(request.POST, instance=request.user.perfil)
		form2 = EditarUsuarioForm(request.POST, instance=request.user)
		content['form1'] = form1
		content['form2'] = form2
		if form1.is_valid() and form2.is_valid():
			usuario1 = form1.save()
			usuario2 = form2.save()
			return redirect("Dashboard")
	else:
		form1 = EditarPerfilForm(instance=request.user.perfil)
		form2 = EditarUsuarioForm(instance=request.user)
		content['form1'] = form1
		content['form2'] = form2
	return render(request, 'usuario/editarperfil.html', content)