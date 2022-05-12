from tkinter.messagebox import QUESTION
from django.shortcuts import render, HttpResponse
from .models import Question, Answer, Trajectory, SuccessStory
from .ml_model.ml_model import dummy_model
from django.http import Http404
from django.shortcuts import get_object_or_404

import time
import random
# import ml_model


def home(request):
    return render(request, 'quest_app/home.html')


def questionnaire(request):
    answers = Answer.objects.all()
    questions = Question.objects.order_by('id')

    if request.method == "POST":  # if a user makes a POST request (i. e. answers the questionnaire)
        # print(request.POST)
        user_answers = request.POST.dict()  # get answers from the form
        trajectory_num = dummy_model(user_answers)  # predict the trajectory
        trajectory_num = 1
        try:
            trajectory = Trajectory.objects.get(number=trajectory_num)  # check if the trajectory exists
        except Trajectory.DoesNotExist:
            trajectory = None

        if trajectory is not None:
            years_to_success = int(trajectory.initial_success_age) - int(user_answers['15'])  # calculate years to success, if the trajectory exists
        else:
            years_to_success = -1

        context = {'trajectory': trajectory, 'years_to_success': years_to_success}
        if years_to_success < 0:  # search for a random success story
            num_stories = SuccessStory.objects.all().count()
            rand_story_id = random.randint(1, num_stories)
            rand_story = SuccessStory.objects.get(id=rand_story_id)
            context['trajectory'] = rand_story

        return render(request, 'quest_app/trajectory_descr.html', context)  # and return a page with the predicted trajectory
        # return HttpResponse(list(request.POST.items())[1:])
    else:  # if a user make a GET request
        context = {'questions': questions, 'answers': answers}
        return render(request, 'quest_app/questionnaire.html', context)  # render a page with questions and answers


def results(request):
    return render(request, 'quest_app/trajectory_descr.html')


def about(request):
    return render(request, 'quest_app/about.html')
