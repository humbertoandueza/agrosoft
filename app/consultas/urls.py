from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^trabajador/$', ConsultarTrabajador, name="ConsultarTrabajador"),
	url(r'^rubro/$', ConsultarRubro, name="ConsultarRubro"),
	url(r'^asigtrabajador/$', ConsultarAsignarTrabajador, name="ConsultarAsignarTrabajador"),
	url(r'^expediente/$', ConsultarExpediente, name="ConsultarExpediente"),
	url(r'^expediente/(?P<pk>[0-9]+)/$', VerExpediente, name="VerExpediente"),
]