from django.conf.urls import url

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def recommendations(request):
    return render(request, 'recommendations.html')