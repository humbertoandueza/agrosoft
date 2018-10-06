from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class PerfilForm(UserCreationForm):
	pri_nombre = forms.CharField(max_length=40)
	seg_nombre = forms.CharField(max_length=40)
	pri_apellido = forms.CharField(max_length=40)
	seg_apellido = forms.CharField(max_length=40)
	seg_apellido = forms.CharField(max_length=40)
	telefono = forms.CharField(max_length=40)
	direccion = forms.CharField(max_length=255)
	email = forms.EmailField(max_length=254)
	generos = (
		("Femenino","Femenino"),
		("Masculino","Masculino"),
	)
	genero = forms.ChoiceField(choices=generos)
	User._meta.get_field('email')._unique = True

	class Meta:
		model = User
		User._meta.get_field('email')._unique = True
		fields = ('username', 'pri_nombre', 'seg_nombre', 'pri_apellido', 'seg_apellido', 'telefono', 'direccion', 'email', 'genero', 'password1', 'password2', )

class EditarPerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields= (
			'pri_nombre',
			'seg_nombre',
			'pri_apellido',
			'seg_apellido',
			'telefono',
			'direccion',
			'genero',
			'cargo'
		)

	def __init__(self, *args, **kwargs):
		super(EditarPerfilForm, self).__init__(*args, **kwargs)
		f = self.fields.get('user_permissions', None)
		if f is not None:
			f.queryset = f.queryset.select_related('content_type')

class EditarUsuarioForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email',)

	def __init__(self, *args, **kwargs):
		super(EditarUsuarioForm, self).__init__(*args, **kwargs)
		f = self.fields.get('user_permissions', None)
		if f is not None:
			f.queryset = f.queryset.select_related('content_type')