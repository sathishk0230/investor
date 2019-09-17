from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    
    return HttpResponse("<h1>this is the front page of order book</h1>")