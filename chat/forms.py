from django import forms

from .models import *

class FormConversa(forms.ModelForm):
	# grupo = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control'}))
	class Meta:
		model = Conversa
		fields = ('grupo','mensagem','data','hora')