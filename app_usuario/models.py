#-*- coding: utf-8 -*-
from django.contrib.auth.models import *
from multiselectfield import MultiSelectField

PROPRIEDADE = ((u'Proprio','Proprio'),(u'Empresa','Empresa'))
DIAS =  (('segunda','segunda'),('terca','terca'), ('quarta','quarta'),
	('quinta','quinta'),('sexta','sexta'),('sabado','sabado'),('domingo','domingo'))
TIPO_REMUNERACAO = ((u'HORISTA','HORISTA'),(u'MENSALISTA','MENSALISTA'))
PERFIL = ((u'Administrador do sistema','Administrador do sistema'),(u'Lider de equipe','Lider de equipe'),
	(u'Promotor de Venda','Promotor de Venda')) 

class Usuario(User):
	nome = models.CharField(max_length= 150)
	cpf=models.CharField(max_length=11)
	data_nascimento=models.DateField()
	perfil=models.CharField(max_length=150, choices= PERFIL)
	cargo=models.CharField(max_length=150)
	telefone=models.CharField(max_length=11)	
	propiedade=models.CharField(max_length=150, choices=PROPRIEDADE)	
	dias_jornada=MultiSelectField(choices=DIAS)
	de=models.TimeField()	
	ate=models.TimeField() 	
	inica_almoco=models.TimeField()	
	fim_almoco=models.TimeField()	
	matricula=models.CharField(max_length=15)	
	data_admissao=models.DateField()	
	tipo_remuneracao = models.CharField(max_length=150, choices=TIPO_REMUNERACAO)

	def __unicode__(self):
		return self.nome