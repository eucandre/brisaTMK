# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin.models import LogEntry

from django.shortcuts import render

def Show(request):
	logs = LogEntry.objects.all()
	return render(request, 'index_geral.html',{'log':logs})
