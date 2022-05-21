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

        #trajectory_num = predict_trajectory(user_answers, verbose=True)  # predict the trajectory
        trajectory_num = 1
        #success_age = predict_success_age(user_answers, verbose=True)  # predict the age of initial success
        success_age = 25
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
        return render(request, 'quest_app/trajectory_descr.html', context)  # return a page with the predicted trajectory

    else:  # if a user makes a GET request
        # answers = Answer.objects.all()
        questions = Question.objects.order_by('number').filter(number__lte=14)  # get all 14 questions used in predictions

        # the next segment is devoted to different checks of questions and answers
        # yes, it is slow
        # yes, it contains nested loops
        # yes, it is hard to read
        # yes, it is hard to maintain and modify
        # but we have to present the completed app in 2 days, so I don't have enough time to write cleaner code
        # I'm really sorry for this code, please don't be furious

        # check number of questions for the ml model
        if questions.count() != 14:
            return HttpResponse(f"ОШИБКА. <br>"
                                f"Не хватает вопросов для модели. Проверьте, все ли 14 вопросов внесены "
                                f"в базу и правильно ли они пронумерованы.")

        elif questions.count() == 14:
            # check all the answers
            possible_answers = {  # possible answer number representations for questions
                '1': (0, 1, 2, 3),  # R1
                '2': (0, 1),  # R2
                '3': (0, 1),  # R3
                '4': (0, 1),  # R4
                '5': (0, 1),  # R5
                '6': (0, 1),  # R6
                '7': (0, 1),  # R7
                '8': (0, 1, 2),  # R8
                '9': (0, 1),  # R9
                '10': (0, 1, 2),  # R10
                '11': (0, 1),  # R11
                '12': (1, 2),  # R12
                '13': (0, 1),  # R13
                '14': (1, 2, 3, 4, 5),  # R14
            }
            for question_num in range(0, 14):
                question_answers = questions[question_num].answer_set.all()  # available answers for a specified questions represented as numbers
                if question_answers.count() == 0:
                    return HttpResponse(
                        f"ОШИБКА. <br>"
                        f"Не найдены варианты ответов для вопроса N{question_num + 1} '{questions[question_num].text}'")

                for question_answer in question_answers:
                    if question_answer.number not in possible_answers[str(question_num + 1)]:
                        return HttpResponse(
                            f"ОШИБКА. <br>"
                            f"Ответ '{question_answer.text}' <br>"
                            f"имеет недопустимое значение числового представления ({question_answer.number}) <br>"
                            f"для вопроса N{question_num + 1} '{questions[question_num].text}'<br>"
                            f"(список доступных числовых представлений ответов для этого вопроса: {possible_answers[str(question_num + 1)]})")

        # if all checks have passed, show the page
        context = {'questions': questions}
        return render(request, 'quest_app/questionnaire.html', context)  # render a page with questions and answers


def results(request):
    return render(request, 'quest_app/trajectory_descr.html')


def about(request):
    return render(request, 'quest_app/about.html')
