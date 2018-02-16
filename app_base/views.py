from django.shortcuts import render

def apresentacao(request):
	
	return render(request, 'index.html')
