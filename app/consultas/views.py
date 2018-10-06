from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from app.usuario.models import *
from app.registros.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q

def ConsultarTrabajador(request):
	usuario = User.objects.all()
	secretaria = Perfil.objects.values('cargo').filter(cargo="Secretaria(o)")
	inspector = Perfil.objects.values('cargo').filter(cargo="Inspector Agrícola")
	return render(request, "consultas/trabajador.html", {"usuarios":usuario, "secretarias":secretaria, "inspectores":inspector})

def ConsultarRubro(request):
	rubro = Rubro.objects.all()
	return render(request, "consultas/rubro.html", {"rubros":rubro})

def ConsultarAsignarTrabajador(request):
	asigtrabajador = Perfil.objects.all()
	return render(request, "consultas/asigtrabajador.html", {"asigtrabajadores":asigtrabajador})

def ConsultarExpediente(request):
	mensaje=""
	expediente = Expediente.objects.all().order_by("id").reverse()
	page = request.GET.get("page", 1)
	paginator = Paginator(expediente, 2)
	try:
		expediente = paginator.page(page)
	except PageNotAnInteger:
		expediente = paginator.page(1)
	except EmptyPage:
		expediente = paginator.page(paginator.num_pages)
	buscador = request.POST
	if "q" in buscador: 
		query = request.POST["q"]
		if query == "" or query == " ":
			mensaje = "Ingrese cédula, nombre o apellido para q."
		else:
			if len(query) < 1:
				mensaje= "Dato invalido."
			else:
				querys = (Q(id__icontains=query) | Q(rif__icontains=query) | Q(solicitante__pri_nombre__icontains=query) | Q(solicitante__pri_apellido__icontains=query))
				expediente = Expediente.objects.filter(querys)
				if len(expediente) == 0:
					mensaje= "No hay resultados para la busqueda."
					expediente = Expediente.objects.all()
				else:
					return render(request, "consultas/expediente.html", {"expedientes":expediente})	
	return render(request, "consultas/expediente.html", {"expedientes":expediente})

def VerExpediente(request, pk):
	expediente = get_object_or_404(Expediente, pk=pk)
	return render(request, "consultas/ver_expediente.html", {"expediente":expediente})