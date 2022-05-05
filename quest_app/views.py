from tkinter.messagebox import QUESTION
from django.shortcuts import render, HttpResponse
from .models import Question, Answer, Trajectory
from .ml_model.ml_model import dummy_model
#import ml_model

# Create your views here.

def index(request):
    answers = Answer.objects.all()
    questions = Question.objects.order_by('id')

    if request.method == "POST":

        print(request.POST)
        user_answers = request.POST.dict()  # get answers from the form
        trajectory_num = dummy_model(user_answers)  # predict the trajectory
        trajectory = Trajectory.objects.get(number=trajectory_num)

        return render(request, 'quest_app/trajectory_descr.html', {'trajectory': trajectory})  # and return the page with the predicted trajectory
    else:
        return render(request, 'quest_app/questionnaire.html', {'questions': questions, 'answers': answers})