from django.shortcuts import render
from .forms import *
from .models import *


def chat(request):
	if request.method== 'POST':
		form = FormConversa(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = FormConversa()
	return render(request, 'chat/chat.html',{'form':form})
