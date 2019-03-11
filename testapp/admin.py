from django.contrib import admin

# Register your models here.

# import the TestApp class from models.py
from .models import TestApp

admin.site.register(TestApp)