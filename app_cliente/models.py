# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models
from django.contrib.auth import *
from app_usuario.models import *


PORTE = ((u'PEQUENO','PEQUENO'),(u'MEDIO','MEDIO'),(u'GRANDE','GRANDE'))


class Segmento(models.Model):
	nome = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nome.__str__()

class Cliente(models.Model):
	nome_fantasia = models.CharField(max_length = 150)
	cpf_cnpj = models.CharField(max_length = 23, unique=True)
	porte_cliente = models.CharField(max_length=8, choices= PORTE)
	segmento = models.ForeignKey(Segmento)
	telefone = models.CharField(max_length = 11)
	email = models.EmailField()
	contato = models.CharField(max_length=150, help_text = 'Pessoa que deve responder pelo cliente')
	cargo_contato = models.CharField(max_length=150)
	endereco = models.CharField(max_length=150,blank=True, null=True)
	observacoes = models.TextField()
	imagem_loja = models.FileField(upload_to= 'loja_clientes/%Y/%m/%d/')
	colaborador_responsavel = models.ForeignKey(Usuario)

	def __unicode__(self):
		return self.nome_fantasia.__str__()

	class Meta:
		verbose_name_plural = 'CLientes do nosso Sistema'


class Grupo(models.Model):
	nome = models.CharField(max_length = 150)
	clientes = models.ManyToManyField(Cliente)

	def __unicode__(self):
		return self.nome.__str__()