from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello iwa, You\'re at the bookstore index </h1>')


def index2(request):
    return HttpResponse('<h1>index2 </h1>')

# Create your views here.
