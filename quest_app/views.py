from django.shortcuts import render, HttpResponse
from .models import Question, Answer, Trajectory, SuccessStory
from django.http import Http404
from django.shortcuts import get_object_or_404

from .ml_models.main import predict_trajectory, predict_success_age
import time
import random
import os


def home(request):
    return render(request, 'quest_app/home.html')


def questionnaire(request):
    if request.method == "POST":  # if a user makes a POST request (i. e. answers the questionnaire)
        user_answers = request.POST.dict()  # get answers from the form

        context = {
            'trajectory': None,
            'success_story': None,
            'success_age': None,
            'years_to_success': None
        }

        trajectory_num = predict_trajectory(user_answers, verbose=True)  # predict the trajectory
        # trajectory_num = 3
        success_age = predict_success_age(user_answers, verbose=True)  # predict the age of initial success
        context['success_age'] = success_age
        context['years_to_success'] = success_age - int(user_answers['15'])

        try:  # check if the trajectory exists
            trajectory = Trajectory.objects.get(number=trajectory_num)
            context['trajectory'] = trajectory
        except Trajectory.DoesNotExist:
            trajectory = None

        if trajectory is not None:  # search for a random success story related to the predicted trajectory
            stories = trajectory.successstory_set.all()
        else:  # if the trajectory has not been found, then look for any random story (unused feature)
            stories = SuccessStory.objects.all()

        num_stories = stories.count()
        if num_stories > 0:
            rand_story_id = random.randint(0, num_stories - 1)
            context['success_story'] = stories[rand_story_id]

        # context['years_to_success'] = int(success_age) - int(user_answers['15'])  # calculate years to success
        # Trajectory.objects.get(id=1).successstory_set.all()

        return render(request, 'quest_app/trajectory_descr.html', context)  # return a page with the predicted trajectory
    else:  # if a user makes a GET request
        # answers = Answer.objects.all()
        questions = Question.objects.order_by('number')

        context = {'questions': questions}
        return render(request, 'quest_app/questionnaire.html', context)  # render a page with questions and answers


def results(request):
    return render(request, 'quest_app/trajectory_descr.html')


def about(request):
    return render(request, 'quest_app/about.html')
