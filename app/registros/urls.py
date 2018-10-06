from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^expediente/$', RegExpediente, name="RegExpediente"),
	url(r'^expediente/(?P<pk>[0-9]+)/editar/$', EditarExpediente, name="EditarExpediente"),
	url(r'^rubro/$', RegRubro, name="RegRubro"),
	url(r'^rubro/(?P<pk>[0-9]+)/editar/$', EditarRubro, name="EditarRubro"),
	url(r'^asigtrabajador/(?P<pk>[0-9]+)/editar/$', AsignarTrabajador, name="AsignarTrabajador"),
]