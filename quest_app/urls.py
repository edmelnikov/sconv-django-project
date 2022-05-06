from django.urls import path
from . import views 

urlpatterns = [
    path('', views.start_page),
    path('questionnaire', views.index),
    path('results', views.results)
]