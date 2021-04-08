from django.shortcuts import render

# Create your views here.
from graph.models import City
from django.http import JsonResponse
from django.db.models import Sum

