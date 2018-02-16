from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def Cria_segmento(request):
	if request.method == 'POST':
		form = FormSegmento(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormSegmento()
	return render(request,"clientes/Cria_segmento.html",{"form":form})

def lista_segmento(request):
	segmentos = Segmento.objects.all()

	paginacao_segmento = Paginator(segmentos,5)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_segmento.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'clientes/lista_segmento.html', {"segmento":lista})

def detalha_segmento(request, nr_item):
	try:
		item = Segmento.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "clientes/item_segmento.html", {'item': item})

def Cria_Cliente(request):
	if request.method == 'POST':
		form = FormCliente(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Cliente Salvo!')
	else:
		form = FormCliente()
	return render(request,"clientes/Cria_cliente.html",{"form":form})

def lista_cliente(request):

	clientes = Cliente.objects.all()
	paginacao_clientes = Paginator(clientes,5)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_clientes.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'clientes/lista_clientes.html', {"clientes":lista})

def detalha_cliente(request, nr_item):
	try:
		item = Cliente.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "clientes/item_clientes.html", {'item': item})


def Cria_Grupo(request):
	if request.method == 'POST':
		form = FormGrupo(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Cliente Salvo!')
	else:
		form = FormGrupo()
	return render(request,"clientes/Cria_grupo.html",{"form":form})

def lista_grupo(request):
	grupo = Grupo_Clientes.objects.all()
	paginacao_grupo = Paginator(grupo,5)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_grupo.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'clientes/lista_grupos.html', {"grupos":lista})


def detalha_grupo(request, nr_item):
	try:
		item = Grupo_Clientes.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "clientes/item_grupos.html", {'item': item})
