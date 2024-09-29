from django.shortcuts import render
from django.http import HttpResponse


def example(request):
	return HttpResponse("client registed successfully")