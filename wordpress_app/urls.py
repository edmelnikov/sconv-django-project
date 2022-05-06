from django.urls import path
import wordpress_app.views
from django.urls import path, include


urlpatterns = [
    path("33", wordpress_app.views.wordpress_app_test),
    path("", include('quest_app.urls'))
]