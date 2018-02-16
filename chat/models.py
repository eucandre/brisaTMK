from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Conversa(models.Model):
	grupo  = models.ManyToManyField(settings.AUTH_USER_MODEL)
	mensagem = models.TextField()
	data  = models.DateField()
	hora = models.TimeField()

	def __unicode__(self):
		return self.grupo.__str__()

	class Meta:
		verbose_name_plural = "Grupo de conversa para o chat do sistema"
