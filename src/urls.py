"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Inicio, name="Inicio"),
    url(r'^dashboard$', Dashboard, name="Dashboard"),
    url(r'^usuario/recuperarclave',password_reset,{'template_name':'usuario/clave/recuperarclave.html','email_template_name':'registration/password_reset_email.html'},name="RecuperarClaveUsuario"),
    url(r'^password_reset_done',password_reset_done,{'template_name':'registration/password_reset_done.html'},name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-94-Za-z_\-]+)/(?P<token>.+)/$',password_reset_confirm,{'template_name':'registration/password_reset_confirm.html'},name="password_reset_confirm"),
    url(r'^reset/done',password_reset_complete,{'template_name':'registration/password_reset_complete.html'},name="password_reset_complete"),
    url(r'^usuario/', include("app.usuario.urls", namespace="Usuarios")),
    url(r'^registro/', include("app.registros.urls", namespace="Registros")),
    url(r'^consulta/', include("app.consultas.urls", namespace="Consultas")),
]
