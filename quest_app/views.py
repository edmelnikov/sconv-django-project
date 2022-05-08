from tkinter.messagebox import QUESTION
from django.shortcuts import render, HttpResponse
from .models import Question, Answer, Trajectory
from .ml_model.ml_model import dummy_model
from django.http import Http404
from django.shortcuts import get_object_or_404

# import ml_model


def home(request):
    return render(request, 'quest_app/home.html')


def questionnaire(request):
    answers = Answer.objects.all()
    questions = Question.objects.order_by('id')

    if request.method == "POST":

        print(request.POST)
        user_answers = request.POST.dict()  # get answers from the form
        trajectory_num = dummy_model(user_answers)  # predict the trajectory
        # trajectory = Trajectory.objects.get(number=trajectory_num)

        # return render(request, 'quest_app/trajectory_descr.html', {'trajectory': trajectory})  # and return the page with the predicted trajectory
        return HttpResponse(list(request.POST.items())[1:])
    else:
        return render(request, 'quest_app/questionnaire.html', {'questions': questions, 'answers': answers})


def results(request):
    return render(request, 'quest_app/trajectory_descr.html')


def about(request):
    return render(request, 'quest_app/about.html')
