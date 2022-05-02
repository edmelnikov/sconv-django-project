from django.db import models

# Create your models here.

class Questions(models.Model):
    question_number = models.CharField('Номер критерия для вопроса', max_length=10)
    question = models.CharField('Вопрос', max_length=500)

    def __str__(self):
        return self.question


class Answers(models.Model):
    awswer_number = models.CharField('Представление ответа цифрой', max_length=10)
    answer = models.CharField('Ответ', max_length=500)
    question_id = models.ForeignKey(Questions, related_name='Questions',on_delete=models.CASCADE)

    def __str__(self):
        return self.answer