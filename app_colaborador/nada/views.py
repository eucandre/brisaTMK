# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *

def cria_colaborador(request):
	if request.method == 'POST':
		form = FormColaborador(request.POST)
		if form.is_valid():
			
			form.save()
	else:
		form = FormColaborador()
	return render(request, 'index.html', {'form':form})		