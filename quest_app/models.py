from django.db import models


class Question(models.Model):
    number = models.IntegerField('Номер критерия', unique=True)
    text = models.TextField('Текст вопроса')

    def __str__(self):
        return self.text


class Answer(models.Model):
    number = models.IntegerField('Представление ответа цифрой')
    text = models.TextField('Текст ответа')
    question_id = models.ForeignKey(Question, related_name='Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Trajectory(models.Model):
    number = models.IntegerField('Номер траектории', unique=True)
    name = models.CharField('Название траектории', max_length=128)
    description = models.TextField('Описание траектории')
    initial_success_age = models.IntegerField('Возраст первого успеха')

    def __str__(self):
        return self.name


class SuccessStory(models.Model):
    name = models.CharField('Имя личности', max_length=128)
    description = models.TextField('Описание первой истории успеха')

    def __str__(self):
        return self.name
