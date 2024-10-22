from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello world')
def index2(request):
    return HttpResponse('I am very happy')
#to tell /product call this index funtion