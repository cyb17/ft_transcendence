from django.shortcuts import render

from django.http import HttpResponse

def home:
	return HttpResponse("you are in home")