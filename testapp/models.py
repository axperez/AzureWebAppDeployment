from django.db import models

# Create your models here.

# every time we change this file, we must run the following commands:
# python manage.py makemigrations
# python manage.py migrate

# class TestApp inherits from the default Django class 'Model'
class TestApp(models.Model):
	title = models.TextField()
	description = models.TextField()
	price = models.TextField()
	summary = models.TextField(default='this is cool!')