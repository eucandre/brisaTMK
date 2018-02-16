from __future__ import unicode_literals

from django.db import models
from app_usuario.models import *

PORTE = ((u'Pequeno','Pequeno'),(u'Medio','Medio'),(u'Grande','Grande'))

class Segmento(models.Model):
	'''
	 Classe para cadastrar o segmento a quem o cliente atende
	'''
	nome = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nome
	class Meta:
		verbose_name_plural = "Segmento a que se enquadra o cliente"

class Cliente(models.Model):
	'''
		Classe para cadastro dos clientes, estabelecimentos, para atendimento do projeto.
	'''
	nome_fantasia = models.CharField(max_length = 150)		
	cpf_cnpj = models.CharField(max_length=23)
	porte = models.CharField(max_length=8, choices=PORTE)
	segmento = models.ForeignKey(Segmento)
	email = models.EmailField()
	contato = models.CharField(max_length=150)
	cargo_contato = models.CharField(max_length=150)
	endereco = models.CharField(max_length=150)
	latitude = models.CharField(max_length=15)
	longitude = models.CharField(max_length=15)
	imagem_loja = models.ImageField(upload_to='documents/%Y/%m/%d')
	observacao = models.TextField()
	colaborador = models.ForeignKey(User)

	def __unicode__(self):
		return self.nome_fantasia

	class Meta:
		verbose_name_plural = "Clientes atendidos por colaboradores"
	
	def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
		self.__init__(self.latitude, self.longitude)
	
class Grupo_Clientes(models.Model):
	'''
		Classe para cadastro de grupos de clientes.
	'''
	nome_grupo = models.CharField(max_length=150)
	clientes = models.ManyToManyField(Cliente)

	def __unicode__(self):
		return self.nome_grupo

	class Meta:
		verbose_name_plural = "Grupo de Clientes atendidos"
		