from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pri_nombre = models.CharField(max_length=40)
	seg_nombre = models.CharField(max_length=40, blank=True, null=True)
	pri_apellido = models.CharField(max_length=40)
	seg_apellido = models.CharField(max_length=40, blank=True, null=True)
	telefono = models.CharField(max_length=40, blank=True, null=True)
	direccion = models.CharField(max_length=255)
	cargos = (
		("Inspector Agrícola","Inspector Agrícola"),
		("Secretaria(o)","Secretaria(o)"),
		("Solicitante","Solicitante"),
	)
	cargo = models.CharField(max_length=50, choices=cargos, default="Solicitante", blank=True, null=True)
	generos = (
		("Femenino","Femenino"),
		("Masculino","Masculino"),
	)
	genero = models.CharField(max_length=50, choices=generos)

	def __str__(self):
		return '%s' %(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Perfil.objects.create(user=instance)
	instance.perfil.save()



