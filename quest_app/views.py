from tkinter.messagebox import QUESTION
from django.shortcuts import render, HttpResponse
from .models import Question, Answer, Trajectory, SuccessStory
from django.http import Http404
from django.shortcuts import get_object_or_404

from .ml_models.main import predict_trajectory
import time
import random
# import ml_models
import os

def home(request):
    return render(request, 'quest_app/home.html')


def questionnaire(request):
    answers = Answer.objects.all()
    questions = Question.objects.order_by('id')

    if request.method == "POST":  # if a user makes a POST request (i. e. answers the questionnaire)
        user_answers = request.POST.dict()  # get answers from the form
        trajectory_num = predict_trajectory(user_answers, verbose=True)  # predict the trajectory

        try:  # check if the trajectory exists
            trajectory = Trajectory.objects.get(number=trajectory_num)
        except Trajectory.DoesNotExist:
            trajectory = None

        years_to_success = -1
        if trajectory is not None:
            years_to_success = int(trajectory.initial_success_age) - int(user_answers['15'])  # calculate years to success, if the predicted trajectory exists

        context = {
            'trajectory': trajectory,  # either a predicted trajectory or a random success story
            'years_to_success': years_to_success
        }

        if years_to_success < 0:  # search for a random success story
            num_stories = SuccessStory.objects.all().count()
            rand_story_id = random.randint(1, num_stories)
            rand_story = SuccessStory.objects.get(id=rand_story_id)
            context['trajectory'] = rand_story  # add the story to the context

        return render(request, 'quest_app/trajectory_descr.html', context)  # return a page with the predicted trajectory
    else:  # if a user makes a GET request
        context = {'questions': questions, 'answers': answers}
        return render(request, 'quest_app/questionnaire.html', context)  # render a page with questions and answers


def results(request):
    return render(request, 'quest_app/trajectory_descr.html')


def about(request):
    return render(request, 'quest_app/about.html')
