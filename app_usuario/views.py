from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import *
from .models import *
from app_usuario.filter import *

def Cria_usuario(request):
	if request.method == "POST":
		form = FormUser(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormUser()
	return render(request, "usuarios/cadastro_usuario.html",{"form":form})

def lista_usuarios(request):
	usuarios = User.objects.all()
	paginacao_usuarios = Paginator(usuarios,5)
	user_filter = ColaboradorFilter(request.GET, queryset=usuarios)

	try:
		page = int(request.GET.get('page', '1'))
		lista = paginacao_usuarios.page(page)
	except (EmptyPage, InvalidPage):
		lista = paginator.page(paginator.num_pages)	

	return render(request,'usuarios/lista_usuarios.html', {"usuarios":lista, 'search':user_filter})

def detalha_usuario(request, nr_item):
	try:
		item = User.objects.get(pk=nr_item)
	except:
		raise Http404('Sem Registro!')
	return render(request, "usuarios/item_usuario.html", {'item': item})
	
def edita_usuario(request, nr_item):
	item = User.objects.get(pk=nr_item)
	if request.method == "POST":
		form = FormUser(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormUser(instance=item)
	return render(request, "usuarios/cadastro_usuario.html",{"form":form})
