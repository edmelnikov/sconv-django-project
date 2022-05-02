from tkinter.messagebox import QUESTION
from django.shortcuts import render, HttpResponse
from .models import Questions, Answers

# Create your views here.

def index(request):
    answers = Answers.objects.all()
    questions = Questions.objects.order_by('id')


    if request.method == "POST":
        answer1 = list(request.POST.items())
        return HttpResponse(answer1[1:])
    else:
        return render(request, 'main/index.html', {'questions':questions, 'answers':answers})