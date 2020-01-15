from django.shortcuts import render

# this is for the first iteration text response with no template
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello from django</h1>')

