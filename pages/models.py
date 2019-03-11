from django.db import models

# Create your models here.

# every time we change this file, we must run the following commands:
# python manage.py makemigrations
# python manage.py migrate

# class Pages inherits from the default Django class 'Model'
class Pages(models.Model):
	data = models.TextField()