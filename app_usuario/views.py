# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .filter import *
from .forms import *
from .models import *

def Cria_Usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormUsuario()
    return render(request, 'cadastra.html',{'form':form})

def lista_usuarios(request):
	usuarios = Usuario.objects.all()
	paginacao_usuarios = Paginator(usuarios,5)
	user_filter = UserFilter(request.GET, queryset=usuarios)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_usuarios.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'usuarios/lista_usuarios.html', {"usuarios":lista, 'search':user_filter})

def detalha_usuario(request, nr_item):
	try:
		item = Usuario.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "usuarios/item_usuario.html", {'item': item})

def edita_usuario(request, nr_item):
	item = Usuario.objects.get(pk=nr_item)
	if request.method == 'POST':
		form = FormUsuario(request.POST, instance = item)
		if form.is_valid():
			form.save()
	else:
		form = FormUsuario(instance= item)
	return render(request, 'cadastra.html',{'form':form})

@login_required
def deleta_usuario(request, nr_item):
  	doc = get_object_or_404(Usuario, pk=nr_item)
  	doc.delete()
  	return redirect("/lista_usuarios/")
