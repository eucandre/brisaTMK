# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .filter import *

def Cria_segmento(request):
	if request.method == 'POST':
		form = FormSegmento(request.POST)
		if form.is_valid():
			form.save()
			
	else:
		form = FormSegmento()
	return render(request, 'clientes/cria_segmento.html',{'form':form})


def Cria_Cliente(request):
	if request.method == 'POST':
		form = FormCliente(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormCliente()
	return render(request, 'clientes/cria_cliente.html',{'form':form})

def Edita_Cliente(request, nr_item):
	item = Cliente.objects.get(pk = nr_item)
	if request.method == 'POST':
		form = FormCliente(request.POST, request.FILES, instance= item)
		if form.is_valid():
			form.save()
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

