from django.shortcuts import render
from django.http import HttpResponse


def wordpress_app_test(request):
    return HttpResponse("Hello, this is a wordpress app! (Главная страница с вордпрессом)")
