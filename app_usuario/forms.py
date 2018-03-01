from django import forms

from .models import *
from django.contrib.auth.forms import *

PROPRIEDADE = ((u'Empresa','Empresa'),(u'Proprio','Proprio'))
DIAS =  (('segunda','segunda'),('terca','terca'), ('quarta','quarta'),
	('quinta','quinta'),('sexta','sexta'),('sabado','sabado'),('domingo','domingo'))
TIPO_REMUNERACAO = ((u'HORISTA','HORISTA'),(u'MENSALISTA','MENSALISTA'))
PERFIL = ((u'Administrador do sistema','Administrador do sistema'),(u'Lider de equipe','Lider de equipe'),
	(u'Promotor de Venda','Promotor de Venda')) 


class FormUsuario(UserCreationForm):
	nome = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
	cpf = forms.CharField(max_length = 11,widget=forms.TextInput(attrs={'class':'form-control'}))
	username = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
	data_nascimento = forms.DateField(widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))
	perfil = forms.ChoiceField(choices = PERFIL, widget = forms.Select(attrs={'class':'form-control'}))
	cargo = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
	telefone = forms.CharField(max_length = 11, widget=forms.TextInput(attrs={'class':'form-control'}))
	propiedade = forms.ChoiceField(choices = PROPRIEDADE, widget = forms.Select(attrs={'class':'form-control'}))
	dias_jornada = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple(), choices = DIAS)
	de = forms.TimeField(widget = forms.TextInput(attrs={'type':'time','class':'form-control'}))
	ate = forms.TimeField(widget = forms.TextInput(attrs={'type':'time','class':'form-control'}))
	inica_almoco = forms.TimeField(widget = forms.TextInput(attrs={'type':'time','class':'form-control'}))
	fim_almoco = forms.TimeField(widget = forms.TextInput(attrs={'type':'time','class':'form-control'}))
	matricula = forms.CharField(max_length = 15,widget=forms.TextInput(attrs={'class':'form-control'}))
	data_admissao = forms.DateField(widget=forms.TextInput(attrs={'type':'date', 'class':'form-control'}))
	tipo_remuneracao = forms.ChoiceField(choices = TIPO_REMUNERACAO, widget = forms.Select(attrs={'class':'form-control'}))
	class Meta:
		model = Usuario
		fields = ('nome','cpf', 'username','is_staff','data_nascimento','perfil','cargo','telefone','propiedade',
			'dias_jornada','de','ate','inica_almoco','fim_almoco','matricula','data_admissao','tipo_remuneracao')	