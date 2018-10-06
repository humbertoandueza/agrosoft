from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^registro/$', RegUsuario, name="RegUsuario"),
	url(r'^contraseña/$', EditarClave, name="EditarClave"),
	url(r'^informacion/$', EditarPerfil, name="EditarPerfil"),
	url(r'^login/$', Login.as_view(), name="LoginUsuario"),
	url(r'^logout/$', LogoutView.as_view(), name="LogoutUsuario"),	
]