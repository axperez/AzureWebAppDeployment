from django.contrib import admin

# Register your models here.

# import the Pages class from models.py
from .models import Pages

admin.site.register(Pages)