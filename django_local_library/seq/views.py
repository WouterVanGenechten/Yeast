from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Yeast Sequence Analyser. \n We are currently constructing the website.")