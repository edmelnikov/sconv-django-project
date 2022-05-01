from django.shortcuts import render
from django.http import HttpResponse


def quest_app_test(request):
    return HttpResponse("Hello, this is a questionnaire app! (Анкета Платформа талантов)")