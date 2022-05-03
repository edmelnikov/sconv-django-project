from tkinter.messagebox import QUESTION
from django.shortcuts import render, HttpResponse
from .models import Question, Answer

# Create your views here.

def index(request):
    answers = Answer.objects.all()
    questions = Question.objects.order_by('id')

    if request.method == "POST":
        answer1 = list(request.POST.items())
        print(request.POST.dict())
        return HttpResponse(answer1[1:])
    else:
        return render(request, 'main/index.html', {'questions': questions, 'answers': answers})