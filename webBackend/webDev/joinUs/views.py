from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def joinUsPage(request):
	return render(request, 'joinUsTemplate.html');