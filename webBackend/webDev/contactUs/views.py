from django.shortcuts import render

# Create your views here.

def contactUsPage(request):
	return render(request, 'contactUs/contactUsTemplate.html');