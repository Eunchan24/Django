from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def TellHello(requests):
    html= "<h1> 식사하러 시다.<h1>"
    return HttpResponse(html)