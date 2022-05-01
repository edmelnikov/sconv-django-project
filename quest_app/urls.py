from django.urls import path
import quest_app.views
from . import views


urlpatterns = [
    path("", quest_app.views.quest_app_test)
]