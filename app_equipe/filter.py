import django_filters
from .models import *
from .forms import *

class EquipeFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(label='Nome',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Equipe
        fields = ['nome',]

class LideresFilter(django_filters.FilterSet):
    lider = django_filters.CharFilter(label='Nome',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Lideres
        fields = ['lider',]

class ColaboradoresFilter(django_filters.FilterSet):
    colaborador = django_filters.CharFilter(label='Nome',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Colaboradores
        fields = ['colaborador',]

