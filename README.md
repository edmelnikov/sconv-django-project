# sconv-django-project

Сейчас тут три приложения:
- wordpress_app - главная страница на Вордпрессе, URL: <домен>
- quest_app для проекта «Платформа талантов», URL: <домен>/questionnaire
- trainer_app для проекта «Тренажёр развития финансовой грамотности начинающего предпринимателя» URL: <домен>/trainer

TODO: разобраться, как интегрировать сайт на вордпрессе 

## Initial Setup 
```
$ python manage.py createsuperuser 
$ python manage.py makemigrations <appname>
```
## Launching
```
$ python manage.py runserver
```
