from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('questionnaire', views.questionnaire, name="questionnaire"),
    path('results', views.results, name="results"),
    path('about', views.about, name="about"),
    # path('<int:question_number>', views.get_question, name="question_by_number"),
]
