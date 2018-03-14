import django_filters
from .models import *
from .forms import *
class UserFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(label='Nome',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
    telefone = django_filters.CharFilter(label='Telefone',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
    cargo = django_filters.CharFilter(label='Cargo',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'cargo']


# import django_filters
# from django.contrib.auth.models import User
# from .models import User
# from django import forms
# class ColaboradorFilter(django_filters.FilterSet):
#     username = django_filters.CharFilter(label='Usuario',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
#     telphone = django_filters.CharFilter(label='Usuario',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
#     office = django_filters.CharFilter(label='Usuario',lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ['username', 'telphone', 'office', ]