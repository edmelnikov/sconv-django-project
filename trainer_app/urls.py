from django.urls import path
import trainer_app.views
from . import views


urlpatterns = [
    path("", trainer_app.views.trainer_app_test)
]