from django.contrib import admin
from .models import Question, Answer, Trajectory, SuccessStory
# Register your models here.


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Trajectory)
admin.site.register(SuccessStory)