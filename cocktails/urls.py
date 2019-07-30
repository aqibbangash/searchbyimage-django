from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'post', views.postimage),
    url(r'getcocktails', views.getcocktails),
]