# sconv-django-project

- quest_app - приложение для проекта «Платформа талантов», URL: <домен>/questionnaire

## Initial Setup 
```
$ pip install -r requirements.txt # Its important to have sckikit-learn=1.0.2
$ python manage.py makemigrations <appname>
$ python manage.py migrate

# optional 
$ python manage.py createsuperuser 

```
## Launching
```
$ python manage.py runserver
```
