# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def Show(request):
	return render(request, 'index_geral.html')
