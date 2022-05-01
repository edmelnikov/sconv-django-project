from django.shortcuts import render
from django.http import HttpResponse


def trainer_app_test(request):
    return HttpResponse("Hello, this is a trainer app! (Тренажёр развития финансовой грамотности начинающего предпринимателя)")
