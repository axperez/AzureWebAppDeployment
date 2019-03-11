from django.shortcuts import render

from django.http import HttpResponse

from .models import Pages
from .forms import UploadDataForm

# Create your views here.

# View - a place that handles various web pages

def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello World!</h1>")

	# obj = Pages.objects.get(id=1)
	
	form = UploadDataForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = UploadDataForm()

	# context = {'object' : obj, 'form': form}

	context = {'form': form}

	return render(request, "pages/home.html", context)