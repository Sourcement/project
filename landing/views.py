from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vfunc(request):
    return HttpResponse('<h1>Privet</h1>')