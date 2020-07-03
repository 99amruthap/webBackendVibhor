from django.urls import path
from . import views

urlpatterns = [
	path('', views.joinUsPage, name='joinUsPage')
]