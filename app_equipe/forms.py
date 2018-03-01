from django import forms

from .models import *

class FormLideres(forms.ModelForm):
	
	lider = forms.ModelChoiceField(queryset = Lideres.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model = Lideres
		fields = ('lider',)

class FormColaboradores(forms.ModelForm):

	colaborador = forms.ModelChoiceField(queryset = Colaboradores.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model = Colaboradores
		fields = ('colaborador',)

class FormEquipe(forms.ModelForm):

	nome = forms.CharField(max_length = 150, widget= forms.TextInput(attrs={'class':'form-control'}))
	lideres = forms.ModelMultipleChoiceField(queryset=Lideres.objects.all(), widget=forms.CheckboxSelectMultiple())
	colaboradores = forms.ModelMultipleChoiceField(queryset=Colaboradores.objects.all(), widget=forms.CheckboxSelectMultiple())
	
	class Meta:
		model = Equipe
		fields = ('nome','lideres','colaboradores')