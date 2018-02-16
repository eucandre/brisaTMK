from django import forms

from .models import *



class FormSegmento(forms.ModelForm):
	nome = forms.CharField(label="Nome do Segmento", max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
	class Meta:
		model = Segmento
		fields = ("nome",)

class FormCliente(forms.ModelForm):
	nome_fantasia = forms.CharField(label="Nome Fantasia",max_length = 150, widget=forms.TextInput(attrs={"class":"form-control"}))		
	cpf_cnpj = forms.CharField(label="CPF/CNPJ",max_length=23, widget=forms.TextInput(attrs={"class":"form-control"}))
	porte = forms.ChoiceField(label="Porte da empresa", choices=PORTE, widget=forms.Select(attrs={"class":"form-control"}))
	segmento = forms.ModelChoiceField(label="Segmento", queryset=Segmento.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
	email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control'}))
	contato = forms.CharField(label="Quem contactar na empresa",max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
	cargo_contato = forms.CharField(label="Cargo do contato",max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
	endereco = forms.CharField(label="Endereco",max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
	# imagem_loja = forms.ImageField(label="Imagem da Loja")
	observacao = forms.CharField(label="Observacao",max_length=300, widget=forms.Textarea(attrs={"class":"form-control"}))
	colaborador = forms.ModelChoiceField(label="Colaborador",queryset=User.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))

	class Meta:
		model = Cliente
		fields = ('nome_fantasia','cpf_cnpj','porte','segmento','email','contato','cargo_contato','endereco','imagem_loja','observacao',
			'colaborador')
			
class FormGrupoClientes(forms.ModelForm):
	nome_grupo = forms.CharField(label="Nome do Grupo",max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
	clientes = forms.ModelMultipleChoiceField(label="Clientes",queryset=Cliente.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))

class FormGrupo(forms.ModelForm):
	nome_grupo = forms.CharField(label="Nome do Grupo",max_length = 150, widget=forms.TextInput(attrs={"class":"form-control"}))
	clientes = forms.ModelMultipleChoiceField(label="Clientes",queryset=Cliente.objects.all() ,widget=forms.SelectMultiple(attrs={"class":"form-control"}))
	class Meta:
		model = Grupo_Clientes
		fields = ('nome_grupo', 'clientes')