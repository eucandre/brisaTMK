from django.shortcuts import render

from .forms import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def Cria_Dia(request):
	if request.method == "POST":
		form = FormDias(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormDias()

	return render(request, "equipe/cria_dia.html", {"form":form})

def lista_Dia(requst):
		dias = Dias.objects.all()
		paginacao_dias = Paginator(dias, 5)

		try:
			page = int(request.GET.get('page', '1'))
			lista = paginacao_dias.page(page)
		except (EmptyPage, InvalidPage):
			lista = paginator.page(paginator.num_pages)	

		return render(request,'equipe/lista_dias.html', {"dias":lista})

def detalha_dia(request, nr_item):
	try:
		item = Dias.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "equipe/item_dia.html", {'item': item})


def Cria_lideres(request):
	if request.method == "POST":
		form = FormLideres(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormLideres()

	return render(request, "equipe/cria_lideres.html", {"form":form})

def lista_lideres(request):
		lider = Lideres.objects.all()
		paginacao_lider = Paginator(lider, 5)

		try:
			page = int(request.GET.get('page', '1'))
			lista = paginacao_lider.page(page)
		except (EmptyPage, InvalidPage):
			lista = paginator.page(paginator.num_pages)	

		return render(request,'equipe/lista_lider.html', {"lideres":lista})


def Cria_promotores(request):
	if request.method == "POST":
		form = FormPromotores(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormPromotores()

	return render(request, "equipe/cria_promotores.html", {"form":form})

def Cria_equipe(request):
	if request.method == "POST":
		form = FormEquipe(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormEquipe()

	return render(request, "equipe/cria_equipe.html", {"form":form})

def Cria_jornada(request):
	if request.method == "POST":
		form = FormJornada(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FormJornada()

	return render(request, "equipe/cria_jornada.html", {"form":form})
