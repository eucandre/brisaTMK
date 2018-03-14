# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import *
from .models import *
from .filter import *

def Cria_Lider(request):
	if request.method == 'POST':
		form = FormLideres(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormLideres()
	return render(request, 'equipe/cria_lideres.html',{'form':form})

def detalha_lider(request, nr_item):
	try:
		item = Lideres.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "equipe/item_lider.html", {'item': item})

def detalha_colaborador(request, nr_item):
	try:
		item = Colaboradores.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "equipe/item_colaboradores.html", {'item': item})

def detalha_equipe(request, nr_item):
	try:
		item = Equipe.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "equipe/item_equipe.html", {'item': item})


def Cria_Colaborador(request):
	if request.method == 'POST':
		form = FormColaboradores(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormColaboradores()
	return render(request, 'equipe/cria_promotores.html',{'form':form})

def Cria_Equipe(request):
	if request.method == 'POST':
		form = FormEquipe(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormEquipe()
	return render(request, 'equipe/cria_equipe.html',{'form':form})

def lista_equipe(request):
	equipe = Equipe.objects.all()
	paginacao_equipes = Paginator(equipe,5)
	equipe_filter = EquipeFilter(request.GET, queryset=equipe)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_equipes.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'equipe/lista_equipe.html', {"equipes":lista, 'search':equipe_filter})
