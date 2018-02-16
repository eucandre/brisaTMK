from django import forms
from .models import *

PROPIEDADE = ((u'Empresa', 'Empresa'), (u'Colaborador','Colaborador'), (u'Terceiros', 'Terceiros'))

class FormUser(forms.ModelForm):
	username = forms.CharField(label="Nome de Usuario",max_length=15, widget=forms.TextInput(attrs={"class":"form-control"}))
	first_name = forms.CharField(label="Primeiro Nome", max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
	last_name = forms.CharField(label="Ultimo Nome", max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
	cpf = forms.CharField(label="CPF", max_length=11,widget=forms.TextInput(attrs={"class":"form-control"}))
	email = forms.EmailField(label="Email", max_length=255,widget=forms.TextInput(attrs={"class":"form-control"}))
	telphone = forms.CharField(label="Telefone", max_length=10,widget=forms.TextInput(attrs={"class":"form-control"}))
	property_telphone = forms.ChoiceField(label="Propriedade do Telefone",choices=PROPIEDADE, widget=forms.Select(attrs={"class":"form-control"}))
	office = forms.CharField(label="Cargo", max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
	birt_day = forms.DateField(label="Data de Nascimento",widget=forms.TextInput(attrs={"type":"date", "class":"form-control"}))
	date_joined = forms.DateField(label="Data de Registro",widget=forms.TextInput(attrs={"type":"date", "class":"form-control"}))
	password = forms.CharField(label="Senha", max_length=10,widget=forms.PasswordInput(attrs={"class":"form-control"}))
	class Meta:
		model = User
		fields = ('username','first_name','last_name','cpf','email','telphone','property_telphone','office','birt_day','is_staff',
			'is_active','date_joined','password')
		   