# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from .forms import *

def Cria_Usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormUsuario()
    return render(request, 'cadastra.html',{'form':form})