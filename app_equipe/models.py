# -*- coding: utf-8 -*-
# -*- coding:cp1252 -*-

from __future__ import unicode_literals

from django.db import models
from app_usuario.models import *

class Lideres(models.Model):
	
	lider = models.ForeignKey(Usuario)

	def __unicode__(self):
		return self.lider.__unicode__()

class Colaboradores(models.Model):
	
	colaborador =	models.ForeignKey(Usuario)	

	def __unicode__(self):
		return self.colaborador.__unicode__()

class Equipe(models.Model):

	nome = models.CharField(max_length = 150)
	lideres = models.ManyToManyField(Lideres)
	colaboradores = models.ManyToManyField(Colaboradores)

	def __unicode__(self):
		return self.nome