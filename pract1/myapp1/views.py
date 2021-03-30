from django.shortcuts import render
from django.http import HttpResponse
def home(request):
	return HttpResponse("<h3>Hello, This is <i>Prasad Joshi</i> from <i>T2</i> batch and my PRN is <i>1841023</i></h3>")
