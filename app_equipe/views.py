# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *


def Cria_Lider(request):
	if request.method == 'POST':
		form = FormLideres(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormLideres()
	return render(request, 'equipe/cria_lideres.html',{'form':form})

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
