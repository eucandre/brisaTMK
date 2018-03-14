from django import forms
from .models import *

PORTE = ((u'PEQUENO','PEQUENO'),(u'MEDIO','MEDIO'),(u'GRANDE','GRANDE'))

class FormSegmento(forms.ModelForm):
	nome = forms.CharField(max_length = 150, widget= forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Segmento
		fields = ('nome',)

class FormCliente(forms.ModelForm):
	nome_fantasia = forms.CharField(max_length = 150, widget= forms.TextInput(attrs={'class':'form-control'}))
	cpf_cnpj = forms.CharField(max_length = 23, widget= forms.TextInput(attrs={'class':'form-control'}))
	segmento = forms.ModelChoiceField(queryset = Segmento.objects.all(), widget = forms.Select(attrs={"class":"form-control"}))
	porte_cliente = forms.ChoiceField(choices = PORTE, widget= forms.Select(attrs={'class':'form-control'}))
	telefone = forms.CharField(max_length = 11, widget= forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget= forms.TextInput(attrs={'class':'form-control'}))
	contato  = forms.CharField(max_length = 150, widget= forms.TextInput(attrs={'class':'form-control'}))
	cargo_contato = forms.CharField(max_length = 150, widget= forms.TextInput(attrs={'class':'form-control'}))
	endereco = forms.CharField(max_length = 150, widget= forms.TextInput(attrs={'class':'form-control'}))
	observacoes = forms.CharField(max_length = 150, widget= forms.Textarea(attrs={'class':'form-control'}))
	imagem_loja = forms.FileField()
	colaborador_responsavel = forms.ModelChoiceField(queryset = Usuario.objects.all(), widget = forms.Select(attrs={"class":"form-control"}))

	class Meta:
		model = Cliente
		fields = ('nome_fantasia','cpf_cnpj','segmento','porte_cliente','telefone','email','contato', 'cargo_contato','endereco','observacoes',
		 'imagem_loja','colaborador_responsavel')

