from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm

# class FormColaborador(UserCreationForm):
# 	class Meta:
# 		model = Colaboradores
# 		fields = ['nome','cpf']
# 	# 	fields = ('nome','cpf'),'data_nascimento','perfil','cargo','telefone',	'propiedade',	'senha','dias_jornada', 
# 	# 'de',	'ate', 	'inica_almoco',	'fim_almoco',	'matricula',	'data_admissao',	'tipo_remuneracao') 