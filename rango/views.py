from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dic = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context= context_dic)
	

	
def about(request):
	context_dic = {'boldmessage' : 'This tutorial has been put together by PEILIN!'}
	return render(request, 'rango/about.html', context= context_dic) 