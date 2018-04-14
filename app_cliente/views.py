# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .filter import *

def Cria_segmento(request):
	if request.method == 'POST':
		form = FormSegmento(request.POST)
		if form.is_valid():
			form.save()	
			return redirect('/lista_segmentos/')		
	else:
		form = FormSegmento()
	return render(request, 'clientes/cria_segmento.html',{'form':form})

def lista_segmento(request):
	segmento = Segmento.objects.all()
	paginacao_segmentos = Paginator(segmento,5)
	segmento_filter = SegmentoFilter(request.GET, queryset=segmento)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_segmentos.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'clientes/lista_segmento.html', {"segmentos":lista, 'search':segmento_filter})

def Cria_Cliente(request):
	if request.method == 'POST':
		form = FormCliente(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/lista_clientes/')
	else:
		form = FormCliente()
	return render(request, 'clientes/cria_cliente.html',{'form':form})

def Edita_Cliente(request, nr_item):
	item = Cliente.objects.get(pk = nr_item)
	if request.method == 'POST':
		form = FormCliente(request.POST, request.FILES, instance= item)
		if form.is_valid():
			form.save()
			return redirect('/lista_clientes/')
	else:
		form = FormCliente(instance= item)
	return render(request, 'clientes/cria_cliente.html',{'form':form})

def detalha_Cliente(request, nr_item):
	try:
		item = Cliente.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "clientes/item_clientes.html", {'item': item})

def lista_clientes(request):
	cliente = Cliente.objects.all()
	paginacao_clientes = Paginator(cliente,5)
	cliente_filter = ClienteFilter(request.GET, queryset=cliente)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_clientes.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'clientes/lista_clientes.html', {"clientes":lista, 'search':cliente_filter})

def Cria_Grupo(request):
	if request.method == 'POST':
		form = FormGrupo(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/lista_grupos/')
	else:
		form = FormGrupo()
	return render(request, 'clientes/cria_grupo.html',{'form':form})

def lista_grupo(request):
	grupo = Grupo.objects.all()
	paginacao_grupos = Paginator(grupo,5)
	grupo_filter = GrupoFilter(request.GET, queryset=grupo)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_grupos.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'clientes/lista_grupos.html', {"grupos":lista, 'search':grupo_filter})

def edita_grupo(request, nr_item):
	item = Grupo.objects.get(pk = nr_item)
	if request.method == 'POST':
		form = FormGrupo(request.POST, request.FILES, instance= item)
		if form.is_valid():
			form.save()
			return redirect('/lista_grupos/')
	else:
		form = FormGrupo(instance= item)
	return render(request, 'clientes/cria_grupo.html',{'form':form})

def detalha_Grupo(request, nr_item):
	try:
		item = Grupo.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "clientes/item_grupos.html", {'item': item})

@login_required
def deleta_cliente(request, nr_item):
  	doc = get_object_or_404(Cliente, pk=nr_item)
  	doc.delete()
  	return redirect("/lista_clientes/")

@login_required
def deleta_grupo(request, nr_item):
  	doc = get_object_or_404(Grupo, pk=nr_item)
  	doc.delete()
  	return redirect("/lista_grupos/")
