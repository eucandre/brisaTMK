import django_filters
from .models import *
from .forms import *

class ClienteFilter(django_filters.FilterSet):
    nome_fantasia = django_filters.CharFilter(label='Nome Fantasia',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
    cpf_cnpj = django_filters.CharFilter(label='Cpf/Cnpj',lookup_expr='icontains' ,widget= forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Cliente
        fields = ['nome_fantasia','cpf_cnpj']
