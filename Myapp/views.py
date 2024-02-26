from django.shortcuts import render
from django.http import HttpResponse

def karibu(request):
    return HttpResponse("<h1>Karibu Django<h1>")

# Create your views here.
