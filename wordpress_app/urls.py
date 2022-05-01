from django.urls import path
import wordpress_app.views
from . import views


urlpatterns = [
    path("", wordpress_app.views.wordpress_app_test)
]