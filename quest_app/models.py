from django.db import models


class Question(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    number = models.IntegerField(unique=True, verbose_name='Номер критерия')
    text = models.TextField(verbose_name='Текст вопроса')
    image = models.ImageField(null=True, blank=True, upload_to='quest_app/img', verbose_name='Картинка')

    def __str__(self):
        return self.text


class Answer(models.Model):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    number = models.IntegerField(verbose_name='Представление ответа цифрой')
    text = models.TextField(verbose_name='Текст ответа')
    related_question_number = models.ForeignKey(Question,
                                            # to_field='number',
                                            on_delete=models.CASCADE,
                                            verbose_name='Соответствующий вопрос')

    def __str__(self):
        return self.text


class Trajectory(models.Model):
    class Meta:
        verbose_name = 'Траектория'
        verbose_name_plural = 'Траектория'

    number = models.IntegerField(unique=True, verbose_name='Номер траектории')
    name = models.CharField(max_length=128, verbose_name='Название траектории')
    description = models.TextField(verbose_name='Описание траектории')
    image = models.ImageField(null=True, blank=True, upload_to='quest_app/img', verbose_name='Картинка')

    def __str__(self):
        return self.name


class SuccessStory(models.Model):
    class Meta:
        verbose_name = 'История успеха'
        verbose_name_plural = 'Истории успеха'

    name = models.CharField(max_length=128, verbose_name='Имя личности')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='quest_app/img', verbose_name='Картинка')
    related_trajectory_number = models.ForeignKey(Trajectory,
                                              # to_field='number',
                                              on_delete=models.CASCADE,
                                              verbose_name='Соответствующая траектория')

    def __str__(self):
        return self.name
